# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and not q:
            return False
        
        if q and not p:
            return False

        if p == q == None:
            return True

        if p.left == p.right == None and q.left == q.right == None:
            return p.val == q.val


        b1 = self.isSameTree(p.left, q.left)
        b2 = self.isSameTree(p.right, q.right)

        return (b1 and b2)