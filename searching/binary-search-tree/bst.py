from collections import deque


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
        """Cases:
        1) Node to be deleted is leaf: Simply remove from the tree.
        2) Node to be deleted has only one child: Copy the child to the node and delete the child
        3) Node to be deleted has two children: Find inorder successor of the node.
           "Copy contents" of the inorder successor to the node and delete the inorder successor.
           Note that inorder predecessor can also be used.
           Successor: an inorder successor of a node in BST is the next node in inorder traversal
              (an inorder successor is the node with the smallest val in it's right subtree)
           Predecessor: inorder predecessor of a node in BST is the previous node in in-order traversal of it.
        ref: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/"""
        if self.contains(val):
            self.root = self._delete(self.root, val)

    def _delete(self, current, val):

        if current is None:
            return None

        # traverse the tree until you find the node to delete
        if val < current.val:
            current.left = self._delete(current.left, val)
        elif val > current.val:
            current.right = self._delete(current.right, val)

        # val is same as current's val so this is the node to be deleted
        else:
            # Case 1 and 2: a node with only one child or no child:
            # copy child node/None to current node (not returning it deletes it's current place)
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 3: the node has two children so we get the inorder successor (smallest in the "right" subtree)
            # get min val node of right subtree
            min_node = self._min_val_node(current.right)
            # copy inorder successor's content to this node (current)
            current.val = min_node.val
            # delete inorder successor
            current.right = self._delete(current.right, min_node.val)

        return current

    def min_val_node(self):
        """Keep moving left down the tree until we find the min val node."""
        return self._min_val_node(self.root)

    def _min_val_node(self, current):
        if current.left is None:
            return current
        return self._min_val_node(current.left)

    def max_value_node(self):
        """Keep moving right down the tree until we find the max val node."""
        return self._max_value_node(self.root)

    def _max_value_node(self, current):
        if current.right is None:
            return current
        return self._max_value_node(current.right)

    def height(self):
        return self._height(self.root)

    def _height(self, current):
        if not current:
            return 0
        # get height from each subtree
        lh = self._height(current.left)
        rh = self._height(current.right)
        # return the greater subtree height
        if lh > rh:
            return lh + 1
        else:
            return rh + 1

###  BREADTH FIRST TRAVERSAL  ###################################################################################################################

    def bfs_recursive_traversal(self):
        # Recursive breadth first traversal / level order traversal
        res = ""
        height = self.height()
        for i in range(1, height + 1):
            res += self._bfs_recursive_traversal(self.root, i)
        return res.rstrip(', ')

    def _bfs_recursive_traversal(self, root, level):
        if not root:
            return ''
        if level == 1:
            return str(root.val) + ', '
        elif level > 1:
            return self._bfs_recursive_traversal(root.left, level - 1) + \
                self._bfs_recursive_traversal(root.right, level - 1)

    def bfs_iterative_traversal(self):
        # Iterative BFS / level order traversal
        queue = deque()  # pop() and appendleft(x)
        current = self.root
        res = ''
        while current:
            res += str(current.val) + ', '
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)
            if len(queue) > 0:
                current = queue.pop()
            else:
                current = None
        return res.rstrip(', ')

##############################################################################################################################################

###  DEPTH FIRST TRAVERSAL  ##################################################################################################################

    def preorder_iterative_traversal(self):
        if self.root is None:
            return None

        stack = []
        current = self.root
        res = []
        while stack or current:
            if current:
                # push to stack and move left until current is None
                # res.append(current.val) # preorder traversal
                stack.append(current)
                current = current.left
            else:
                # pop off stack and move right
                current = stack.pop()
                # res.append(current.val) inorder traversal
                current = current.right

        return res

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

    def postorder_print(self):
        self._postorder_print(self.root)

    def _postorder_print(self, current):
        if current:
            self._postorder_print(current.left)
            self._postorder_print(current.right)
            print(current.val)

###################################################################################################################################

    def max_depth(self):
        """The max depth is the number of nodes along the longest path from the root node
           down to the farthest leaf node."""
        return self._max_depth(self.root)

    def _max_depth(self, current):
        if current is None:
            return -1  # -1 because we are counting the root node level as level 0
        return 1 + max(self._max_depth(current.left), self._max_depth(current.right))

    def min_depth(self):
        """The minimum depth is the number of nodes along the shortest path from the root node
           down to the nearest leaf node."""
        return self._max_depth(self.root)

    def _min_depth(self, current):
        if current is None: return 0

        if current.left is None:
            return 1 + self._min_depth(current.right)

        if current.right is None:
            return 1 + self._min_depth(current.left)

        return 1 + min(self._min_depth(current.left), self._min_depth(current.right))

    def sum_tree(self):
        return self._sum_tree(self.root)

    def _sum_tree(self, current):
        if current is None:
            return 0
        return current.val + self._sum_tree(current.left) + self._sum_tree(current.right)

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, current):
        if current is None:
            return 0
        elif current.left is None and current.right is None:
            return 1
        return self._count_leaves(current.left) + self._count_leaves(current.right)

    def is_symmetric(self):

        if self.root is None:
            return True

        def mirror(r1, r2):
            if r1 is None and r2 is None:
                return True

            if r1 and r2 and r1.val == r2.val:
                return mirror(r1.left, r2.right) and mirror(r1.right, r2.left)
            # if either node is None or not equal, the tree isn't symmetric
            return False

        return mirror(self.root, self.root)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(4)
    tree.add(1)
    tree.add(8)
    tree.add(6)
    tree.add(6)  # Note this won't be added
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # print('in-order traversal: ' + str(tree.inorder_traversal()))
    # print('post-order traversal: ' + str(tree.postorder_traversal()))
    # print('max level: ' + str(tree.max_depth()))
    # print('min level: ' + str(tree.min_depth()))
    # print('contains 1: ' + str(tree.contains(1)))
    # print('contains 5: ' + str(tree.contains(5)))
    # print('contains 8: ' + str(tree.contains(8)))
    # print('contains 99: ' + str(tree.contains(99)))
    # Case 1: delete a two leaf nodes test
    # tree.delete(1)
    #print('pre-order traversal: ' + str(tree.preorder_traversal()))
    #print('pre-order iterative traversal: ' + str(tree.preorder_iterative_traversal()))
    # tree.delete(4)
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # Case 2: delete a node with only one child node (8 is the only in this category)
    # tree.delete(8)
    # print('pre-order traversal: ' + str(tree.preorder_traversal()))
    # Case 3: delete a node with two children (3 and 5 work for this)
    # tree.delete(3)
    # print('in-order traversal: ' + str(tree.preorder_traversal()))
    # print('min val node:' + str(tree.min_val_node(tree.root).val))
    # print('max val node: ' + str(tree.max_value_node().val))
    # print('sum val: ' + str(tree.sum_tree()))
    # print('leaf count: ' + str(tree.count_leaves()))
    #tree.postorder_print()
    print(tree.height())
    print(tree.bfs_recursive_traversal())
    print()
    print(tree.bfs_iterative_traversal())

#   ROOT      5      LEVEL = 0
#           /   \
#          3     8
#         / \   /
#        1   4 6
