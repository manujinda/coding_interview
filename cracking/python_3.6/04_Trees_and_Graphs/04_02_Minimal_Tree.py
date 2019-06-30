# Author: Manujinda Wathugala
# Cracking the Coding Interview
# Chapter 4 - Trees and Graphs
# 4.2 - Minimal Tree

from Tree import Tree_Node, print_tree


def min_tree(value_list):
    if len(value_list) == 0:
        return None

    mid = len(value_list) // 2

    tree = Tree_Node(value_list[mid])
    tree.left = min_tree(value_list[0:mid])
    tree.right = min_tree(value_list[mid+1:])

    return tree


if __name__ == '__main__':
    tree = min_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print_tree(tree)