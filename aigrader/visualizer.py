import ast

import zss
import math
import astor
import showast
from zss import compare as zss_compare
from collections import defaultdict
from itertools import zip_longest
from assignment_helper import ASTWrapper, get_distance, ASSIGNMENTS

def read_lines(file_path):
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]

def reverse(arr):
    return list(reversed(list(arr)))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def find_submission(source):
    for assignment in ASSIGNMENTS:
        for submission in assignment.submissions:
            if submission.path == source:
                return assignment, submission


def print_submission(submission):
    for function in submission.functions.values():
        print(astor.to_source(function.ast_node))


def get_distance_source(source1, source2):
    assignment1, submission1 = find_submission(source1)
    assignment2, submission2 = find_submission(source2)
    if assignment1.id != assignment2.id:
        raise Exception("Sources are not from same assignment")
    cost, operations = 0, []
    for scaffold in assignment1.scaffolds:
        c1, o1 = get_distance(submission1.functions[scaffold], 
                              submission2.functions[scaffold],
                              return_operations=True)
        cost += c1
        operations += o1
    return cost, operations
    

def visualize_differences(source1, source2):
    """Prints source1 and necessary changes which needs to be
    applied in order to turn source1 into source2.
    """
    cost, operations = get_distance_source(source1, source2)
    print(f"Cost: {cost}")
    print(f"""
{bcolors.OKGREEN}I - Insertions{bcolors.FAIL}
{bcolors.FAIL}R - Removals{bcolors.ENDC}
    """)
    # line number to list of node removals e.g 1 -> [If, Else]
    removed_lines = defaultdict(list)
    # line number to list of node insertions e.g 1 -> [If, Elif, Else]
    inserted_lines = defaultdict(list)
    # line matching. lineno in source-1 to lineno in source-2
    matched_lines = {0: 0}
    for op in operations:
        if op.type == zss_compare.REMOVE:
            removed_lines[op.arg1.lineno()-1].append(op.arg1.label)
        elif op.type == zss_compare.INSERT:
            inserted_lines[op.arg2.lineno()-1].append(op.arg2.label)
        else:
            line1_no = op.arg1.lineno()
            line2_no = op.arg2.lineno()
            if line1_no != -1:
                matched_lines[line1_no] = line2_no
                
    lines1 = read_lines(source1)
    lines2 = read_lines(source2)
    # sort matching lines in increasing order. so that we can see see
    # which set of lines in source-1 aligns with which set of lines in source-2
    matched_lines = sorted([(k, v) for (k, v) in matched_lines.items()])
    if len(matched_lines) != 0 and matched_lines[-1][0] != len(lines1):
        matched_lines.append((len(lines1), len(lines2)))
    
    for i in range(1, len(matched_lines)):
        # segment1 is continous set of lines in source-1
        segment1 = lines1[matched_lines[i-1][0]:matched_lines[i][0]]
        # segment2 is corresponding set of lines in source-2 against segment1
        segment2 = lines2[matched_lines[i-1][1]:matched_lines[i][1]]
        # removeals and insertions which happened in the segment1 and segment2
        removals = []
        insertions = []
        for line1_no in range(matched_lines[i-1][0], matched_lines[i][0]):
            removals.extend(removed_lines.get(line1_no, []))
        for line2_no in range(matched_lines[i-1][1], matched_lines[i][1]):
            insertions.extend(inserted_lines.get(line2_no, []))
        if removals:
            print(f'{bcolors.FAIL}R: {", ".join(reverse(removals))}{bcolors.ENDC}')
        if insertions:
            print(f'{bcolors.OKGREEN}I: {", ".join(reverse(insertions))}{bcolors.ENDC}')
        for line1, line2 in reverse(zip_longest(reverse(segment1), reverse(segment2), fillvalue='')):
            if line1 == line2 == '':
                continue
            print('{:40.40} {:40.40}'.format(line1, line2))
        print('-'*81)
