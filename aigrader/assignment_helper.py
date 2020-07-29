import ast
import astor
import glob
import math
import numpy as np
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


def find_functions(node: ASTWrapper, names: List[str] = None) -> Dict[str, ASTWrapper]:
    G = {}
    if node.label == 'FunctionDef':
        if names is None or node.ast_node.name in names:
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
    comparison_table: Optional[np.array]

    def __init__(self,
                 glob: str,
                 scaffolds: List[str],
                 submissions: List[Submission],
                 comparison_table: Optional[np.array]):
        self.glob = glob
        self.scaffolds = scaffolds
        self.submissions = submissions
        self.comparison_table = comparison_table

def parse_file(path, ignore_assignments):
    with open(path) as f:
        return ASTWrapper(ast.parse(f.read()), ignore_assignments=ignore_assignments)


def print_progress(total, current):
    print('{}/{}'.format(current, total))


def calculate_edit_distance(submissions : List[ASTWrapper], match_functions : bool, scaffold : List[str] = None) -> np.array:
    N = len(submissions)
    table = np.array([[0] * N] * N, dtype=int)
    total_computations = math.comb(N, 2)
    progress = 0
    if not match_functions:
        for i in range(N):
            for j in range(i + 1, N):
                table[j][i] = table[i][j] = get_distance(submissions[i], submissions[j])
                progress += 1
                print_progress(total_computations, progress)
    else:
        if scaffold is not None:
            # use scaffold
            submission_functions = [find_functions(submission, scaffold) for submission in submissions]
            for i in range(N):
                for j in range(i + 1, N):
                    total = 0
                    for scaffold_function in scaffold:
                        total += get_distance(submission_functions[i][scaffold_function], submission_functions[j][scaffold_function])
                    table[j][i] = table[i][j] = total
                    progress += 1
                    print_progress(total_computations, progress)
            return table
        else:
            # don't use scaffold, try all function combinations?
            return table
    return table

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
