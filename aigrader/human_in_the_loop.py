import astor

def print_submission(submission):
    with open(submission) as f:
        for line in f:
            print(line, end='')

def find_representative(comparison_table, cluster):
    submission_comparison = comparison_table[cluster][:,cluster]
    distances = submission_comparison.sum(axis=0)
    ix_with_min = distances.argmin()
    return cluster[ix_with_min]

def create_tree(linkage_matrix, list_size):
    dct = dict()

    counter = list_size
    for n1, n2, d, _ in linkage_matrix:
        n1 = int(n1)
        n2 = int(n2)
        if n1 >= list_size:
            n1 = dct[n1]
        if n2 >= list_size:
            n2 = dct[n2]
        tup = (n1, n2)
        dct[counter] = tup
        counter += 1

    return dct[counter - 1]

text_black = '\u001b[30m'
# red, green, yellow, blue, magenta, cyan
print_tree_colors = ['\u001b[31m', '\u001b[32m', '\u001b[33m', '\u001b[34m', '\u001b[35m', '\u001b[36m']

# tree is a binary tree shaped like ((a, (b, c)), d)
# highlights is a 2D array shaped like [[n0, n1, n2], [n3, n4], [n5, n6, n7]],
# where n0,n1,n2 have the same colour, n3 and n4 have the same colour, etc.
def print_tree(tree, highlights=[[]], depth=0):
    if not isinstance(tree, tuple):
        print_color = text_black
        for color, nodes in zip(print_tree_colors, highlights):
            if tree in nodes:
                print_color = color
                break
        print(f'{"  " * depth}{print_color}{tree: 2d}{text_black}')
        return
    else:
        l_tree, r_tree = tree
        print_tree(l_tree, highlights, depth + 1)
        print_tree(r_tree, highlights, depth + 1)
        return

def pprint_tree(tree, file=None, _prefix="", _last=True):
    print(_prefix, '`- ' if _last else '|- ', sep='', end='')
    if not isinstance(tree, tuple):
        print_color = text_black
        for color, nodes in zip(print_tree_colors, highlights):
            if tree in nodes:
                print_color = color
                break
        print(f'{print_color}{tree: 2d}{text_black}')
    else:
        print('')
        _prefix += '   ' if _last else '|  '
        l_tree, r_tree = tree
        print_tree(l_tree, highlights, _prefix, False)
        print_tree(r_tree, highlights, _prefix, True)
    return

def get_tree_members(tree):
    gather = []
    try:
        for item in tree:
            if isinstance(item, tuple):
                gather.extend(get_tree_members(item))            
            else:
                gather.append(item)
    except:
        # tree has only one member
        return [tree]
    return sorted(gather)

# returns True if the tree should be split, False otherwise
def try_split(submissions, comparison_table, tree):
    try:
        l_tree, r_tree = tree
    except:
        return False
    l_members = get_tree_members(l_tree)
    r_members = get_tree_members(r_tree)
    l_rep = find_representative(comparison_table, l_members)
    r_rep = find_representative(comparison_table, r_members)
    print(' Tree '.center(64, '#') + '\n')
    print_tree(tree, [[l_rep], get_tree_members(l_tree), [r_rep], get_tree_members(r_tree)])
    print(' Code '.center(64, '#') + '\n')
    print(f' Submission {l_rep} '.center(64, '#') + '\n')
    print_submission(submissions[l_rep])
    print(f' Submission {r_rep} '.center(64, '#') + '\n')
    print_submission(submissions[r_rep])
    print('#' * 64 + '\n')
    similar = input('Are these to submissions similar enough to be given the same comments?\n')
    if similar.lower() in ['y', 'yes', 't', 'true']:
        return False
    else:
        return True

def split_tree(submissions, comparison_table, tree):
    if try_split(submissions, comparison_table, tree):
        l_tree, r_tree = tree
        return split_tree(submissions, comparison_table, l_tree) + split_tree(submissions, comparison_table, r_tree)
    else:
        return [get_tree_members(tree)]
