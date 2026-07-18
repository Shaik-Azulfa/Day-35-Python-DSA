class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.data == t2.data and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))
        
        if not root:
            return True
        return isMirror(root.left, root.right)
class Solution:
    def hasPathSum(self, root, targetSum):
        # Base case: empty tree
        if not root:
            return False
        
        # Check if it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.data
        
        # Recur for left and right subtree with reduced sum
        remainingSum = targetSum - root.data
        return (self.hasPathSum(root)
