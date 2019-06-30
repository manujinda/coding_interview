# Define a simple tree data-structure


class Tree_Node():
    value = 0
    left = None
    right = None

    def __init__(self, value):
        self.value = value


def make_tree(value_list):
    if len(value_list) == 0:
        return None

    mid = len(value_list) // 2

    tree = Tree_Node(value_list[mid])
    tree.left = make_tree(value_list[0:mid])
    tree.right = make_tree(value_list[mid+1:])

    return tree


def print_tree(tree):
    print_tree_rec(tree, 0)


def print_tree_rec(tree, depth):
    if tree is not None:
        print("\t" * depth, tree.value)
        print_tree_rec(tree.left, depth+1)
        print_tree_rec(tree.right, depth+1)


if __name__ == '__main__':
    tree = make_tree([1, 2, 3, 4, 5, 6, 7, 8])
    print_tree(tree)
