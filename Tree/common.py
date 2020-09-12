class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Check if two trees are the same.
def assert_tree(root1, root2):
    if root1 == None:
        assert(root2 == None)
    else:
        assert(root1 != None and root2 != None and root1.val == root2.val)
        if root1.left == None:
            assert(root2.left == None)
        else:
            assert_tree(root1.left, root2.left)
        if root1.right == None: 
            assert(root2.right == None)
        else:
            assert_tree(root1.right, root2.right)