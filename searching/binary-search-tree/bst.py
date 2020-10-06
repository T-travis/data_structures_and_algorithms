
class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root = self._add(self.root, val)

    def _add(self, current, val):
        if current is None:
            current = TreeNode(val)
        elif val < current.val:  # < guarantees no duplicates
            current.left = self._add(current.left, val)
        elif val > current.val:
            current.right = self._add(current.right, val)
        return current

    def contains(self, val):
        return self._contains(self.root, val)

    def _contains(self, current, val):
        if current is None:
            return False
        elif current.val == val:
            return True
        else:
            return self._contains(current.left, val) or self._contains(current.right, val)

    def delete(self, val):
        # Cases:
        # 1) Node to be deleted is leaf: Simply remove from the tree.
        # 2) Node to be deleted has only one child: Copy the child to the node and delete the child
        # 3) Node to be deleted has two children: Find inorder successor of the node.
        #    "Copy contents" of the inorder successor to the node and delete the inorder successor.
        #    Note that inorder predecessor can also be used.
        #    Successor: an inorder successor of a node in BST is the next node in inorder traversal
        #       (an inorder successor is the node with the smallest val in it's right subtree)
        #    Predecessor: inorder predecessor of a node in BST is the previous node in in-order traversal of it.
        # ref: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        if self.contains(val):
            self.root = self._delete(self.root, val)

    def _delete(self, current, val):

        if current is None:
            return None

        if val < current.val:
            current.left = self._delete(current.left, val)
        elif val > current.val:
            current.right = self._delete(current.right, val)

        # val is same as current's val so this is the node to be deleted
        else:
            # a node with only one child or no child
            # copy child node/None to current node (not returning it deletes it's current place)
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # the node has two children so we get the inorder successor (smallest in the "right" subtree)
            # get min val node
            min_node = self.min_val_node(current.right)
            # copy inorder successor's content to this node (current)
            current.val = min_node.val
            # delete inorder successor
            current.right = self._delete(current.right, min_node.val)

        return current

    def min_val_node(self, current):
        if current.left is None:
            return current
        return self.min_val_node(current.left)

    def preorder_traversal(self):
        if self.root is None:
            return None
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, current):
        if current:
            return [current.val] + self._preorder_traversal(current.left) + self._preorder_traversal(current.right)
        return []

    def inorder_traversal(self):
        if self.root is None:
            return None
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, current):
        if current:
            return self._inorder_traversal(current.left) + [current.val] + self._inorder_traversal(current.right)
        return []

    def postorder_traversal(self):
        if self.root is None:
            return None
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, current):
        if current:
            return self._postorder_traversal(current.left) + self._postorder_traversal(current.right) + [current.val]
        return []

    def max_depth(self):
        return self._max_depth(self.root)

    def _max_depth(self, current):
        if current is None:
            return -1  # -1 because we are counting the root node level as level 0
        return 1 + max(self._max_depth(current.left), self._max_depth(current.right))

    def min_depth(self):
        return self._max_depth(self.root)

    def _min_depth(self, current):
        pass  # TODO

    def sum_tree(self):
        return self._sum_tree(self.root)

    def _sum_tree(self, current):
        pass  # TODO

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, current):
        pass  # TODO

    def min_value(self):
        return self._min_value(self.root)

    def _min_value(self, current):
        pass  # TODO

    def max_value(self):
        return self._max_value(self.root)

    def _max_value(self, current):
        pass  # TODO


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(4)
    tree.add(1)
    tree.add(8)
    tree.add(6)
    tree.add(6)  # Note this won't be added
    print('pre-order traversal: ' + str(tree.preorder_traversal()))
    print('in-order traversal: ' + str(tree.inorder_traversal()))
    print('post-order traversal: ' + str(tree.postorder_traversal()))
    print('max level: ' + str(tree.max_depth()))
    print('contains 1: ' + str(tree.contains(1)))
    print('contains 5: ' + str(tree.contains(5)))
    print('contains 8: ' + str(tree.contains(8)))
    print('contains 99: ' + str(tree.contains(99)))
    # Case 1: delete a two leaf nodes test
    # tree.delete(1)
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # tree.delete(4)
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # Case 2: delete a node with only one child node (8 is the only in this category)
    # tree.delete(8)
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # Case 3: delete a node with two children (3 is the only category for this
    tree.delete(3)
    print('in-order traversal: ' + str(tree.preorder_traversal()))
    print('min val node:' + str(tree.min_val_node(tree.root).val))

#   ROOT      5
#           /   \
#          3     8
#         / \   /
#        1   4 6
