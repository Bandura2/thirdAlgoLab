import unittest
import main


class TestTreeBalance(unittest.TestCase):
    left_root = main.BinaryTree(1)
    left_root.left = main.BinaryTree(0)
    left_root.right = main.BinaryTree(2)

    right_root = main.BinaryTree(5)
    right_root.left = main.BinaryTree(4)
    right_root.right = main.BinaryTree(6)
    right_root.right.right = main.BinaryTree(7)

    main_root = main.BinaryTree(3)
    main_root.left = left_root
    main_root.right = right_root

    def test_tree_balanced(self):
        self.assertEqual(main.is_tree_balanced(self.main_root), True)

    def test_tree_balanced_2(self):
        test_binary_tree = self.main_root
        test_binary_tree.right.right.right.right = main.BinaryTree(20)
        self.assertEqual(main.is_tree_balanced(test_binary_tree), False)

    def test_empty_tree(self):
        empty_tree = main.BinaryTree(None)
        self.assertEqual(main.is_tree_balanced(empty_tree), True)