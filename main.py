class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# def is_tree_balanced(node: BinaryTree):
#
#     if node.left is None and node.right is None:
#         return True
#     elif node.left is None or node.right is None:
#         return False
#     else:
#         is_left_tree_balanced = is_tree_balanced(node.left)
#         is_right_tree_balanced = is_tree_balanced(node.right)
#
#     if is_left_tree_balanced and is_right_tree_balanced:
#         return True
#     elif is_left_tree_balanced or is_right_tree_balanced:
#         return False
#     else:
#         return False


def is_tree_balanced(node: BinaryTree) -> bool:
    return tree_height(node) != -1


def tree_height(current_node: BinaryTree):
    if current_node is None:
        return 0

    left_subtree_height = tree_height(current_node.left)
    if left_subtree_height == -1:
        return -1

    right_subtree_height = tree_height(current_node.right)
    if right_subtree_height == -1:
        return -1

    if abs(left_subtree_height - right_subtree_height) > 1:
        return -1

    return max(left_subtree_height, right_subtree_height) + 1


# left_root = BinaryTree(1)
# left_root.left = BinaryTree(0)
# left_root.right = BinaryTree(2)
#
# right_root = BinaryTree(5)
# right_root.left = BinaryTree(4)
# right_root.right = BinaryTree(6)
# right_root.right.right = BinaryTree(7)
#
# main_root = BinaryTree(3)
# main_root.left = left_root
# main_root.right = right_root

# print(f"Is binary tree balanced: {is_tree_balanced(main_root)}")
#
#
# def print_binary_tree(node: BinaryTree):
#     if node.left is not None:
#         print_binary_tree(node.left)
#
#     print(f"Elem {node.value}")
#     if node.right is not None:
#         print_binary_tree(node.right)
#
#
# print_binary_tree(main_root)
