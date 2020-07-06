import ast
import astor
import glob
import math
import numpy
import os.path
import zss
from typing import List, Dict, Optional
from collections import defaultdict


class ASTWrapper:
    
    def __init__(self, ast_node, ignore_assignments=False, parent=None):
        self.ast_node = ast_node
        self.label = ast_node.__class__.__name__
        self.children: List[ASTWrapper] = []
        self.parent = parent
        self.operation = None
        for child_ast in ast.iter_child_nodes(ast_node):
            if ignore_assignments:
                if self.label not in ['Assign', 'AugAssign']:
                    self.children.append(ASTWrapper(child_ast, ignore_assignments, self))
            else:
                self.children.append(ASTWrapper(child_ast, ignore_assignments, self))

    def lineno(self):
        if not hasattr(self.ast_node, 'lineno'):
            if self.parent is None:
                # It can happen that we can't determine line no for AST node Module
                return -1
            return self.parent.lineno()
        return self.ast_node.lineno


def find_functions(node: ASTWrapper, names: List[str]) -> Dict[str, ASTWrapper]:
    G = {}
    if node.label == 'FunctionDef':
        if len(names) == 0 or node.ast_node.name in names:
            G[node.ast_node.name] = node
    else:
        for child in node.children:
            G.update(find_functions(child, names))
    return G


class Submission:
    path: str
    functions: Dict[str, ASTWrapper]

    def __init__(self,
                 path: str,
                 functions: Dict[str, ASTWrapper]):
        self.path = path
        self.functions = functions


class Assignment:
    glob: str
    scaffolds: List[str]
    submissions: List[Submission]
    comparison_table: Optional[numpy.array]

    def __init__(self,
                 glob: str,
                 scaffolds: List[str],
                 submissions: List[Submission],
                 comparison_table: Optional[numpy.array]):
        self.glob = glob
        self.scaffolds = scaffolds
        self.submissions = submissions
        self.comparison_table = comparison_table


def calculate_edit_distance(files: tuple,
                            scaffold_path: str,
                            output_path: str) -> Assignment:
    root = ASTWrapper(astor.parse_file(scaffold_path), True)
    scaffold_functions: List[str] = list(find_functions(root, []).keys())
    print("Scaffold functions:")
    for name in scaffold_functions:
        print(f' - {name}')
    assignment = Assignment(None,
                            scaffold_functions,
                            [], None)
    for source in files:
        root = ASTWrapper(astor.parse_file(source), True)
        functions = find_functions(root, assignment.scaffolds)
        is_incomplete = False
        for scaffold in assignment.scaffolds:
            if scaffold not in functions:
                print(f"Skipping {source} as {scaffold} is not found.")
                is_incomplete = True
        if not is_incomplete:
            assignment.submissions.append(Submission(source, functions))
    os.makedirs(output_path, exist_ok=True)
    comparison_path = os.path.join(output_path, "comparison.npy")
    assignment.comparison_table = get_comparison_table(assignment, comparison_path)
    print(assignment.comparison_table)
    print(len(assignment.comparison_table))
    return assignment


# ZSS
def get_children(node: ASTWrapper) -> List[ASTWrapper]:
    return node.children


def insert_cost(node: ASTWrapper) -> int:
    return 1


def delete_cost(node: ASTWrapper) -> int:
    return 1


def update_cost(node1: ASTWrapper, node2: ASTWrapper) -> float:
    if node1.label == node2.label:
        return 0
    return math.inf


def get_distance(node1: ASTWrapper,
                 node2: ASTWrapper,
                 return_operations: bool=False) -> int:
    return zss.distance(node1,
                        node2,
                        get_children, 
                        insert_cost, 
                        delete_cost, 
                        update_cost,
                        return_operations=return_operations)


def get_comparison_table(assignment: Assignment, file_path: Optional[str]) -> List[List[int]]:
    if file_path is not None and os.path.exists(file_path):
        return numpy.load(file_path)
    N = len(assignment.submissions)
    table = [[0]*N for _ in range(N)]
    for i in range(N):
        print(f'{i+1}/{N}')
        for j in range(i+1, N):
            total = 0
            for scaffold in assignment.scaffolds:
                total += get_distance(assignment.submissions[i].functions[scaffold],
                                      assignment.submissions[j].functions[scaffold])
            table[j][i] = table[i][j] = total
    result = numpy.array(table, dtype=int)
    if file_path is not None:
        numpy.save(file_path, result)
    return result

