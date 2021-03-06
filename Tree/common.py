from typing import List  # This ensures the compile can accept Leetcode Python 3 syntax: https://leetcode.com/discuss/general-discussion/270755/in-python-3-the-parameter-type-define-list-always-reports-an-error-in-ide

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    '''
    Breath first search to locate nodes in order and put them in result string. Put 'null' for empty left or right unless no value after.
    O(n) runtime both for serilaize and deserialize. O(n) storage for both as well.
    Beat 89% runtime, 63% storage of all Leetcode submissions.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        layer,out = [root],[]
        while layer:
            new_layer = []
            is_all_none = True
            for node in layer:
                if node != None: 
                    is_all_none = False
                    break
            for node in layer:
                if node == None:
                    if not is_all_none: out.append('null')
                else:
                    out.append(str(node.val))
                    new_layer.append(node.left)
                    new_layer.append(node.right)
            layer = new_layer
        while out and out[-1] == 'null':
            out.pop()
        return '[{}]'.format(','.join(out))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i,n = 1,len(data)-1
        root,layer = None,[]
        while i < n:
            if root == None:
                j = data.find(',',i)
                if j == -1: j = n
                root = TreeNode(int(data[i:j]))
                layer.append(root)
                i = j+1
            else:
                new_layer = []
                for node in layer:
                    if i >= n: break
                    j = data.find(',',i)
                    if j == -1: j = n
                    k = data.find(',',j+1)
                    if k == -1: k = n
                    if j > i and data[i:j] != 'null': 
                        node.left = TreeNode(int(data[i:j]))
                        new_layer.append(node.left)
                    if k > j+1 and data[j+1:k] != 'null': 
                        node.right = TreeNode(int(data[j+1:k]))
                        new_layer.append(node.right)
                    i = k+1
                layer = new_layer
        return root
        
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

# Assert a sequence of calls return expected results.
def assert_call_sequence(context, calls, args, expected_outputs):
    assert(len(calls) == len(args) == len(expected_outputs[0]))
    assert(len(calls) >= 1)
    output = []
    # Default first item in calls is to create the class object of the solution and the remaining is to call methods of the object.
    solution = context[calls[0]](*args[0])
    output.append(None)
    for i in range(1,len(calls)):
        call = getattr(solution, calls[i])
        output.append(call(*args[i]))
    assert(output in expected_outputs)