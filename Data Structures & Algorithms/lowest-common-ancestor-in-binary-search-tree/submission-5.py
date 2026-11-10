# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        stack = deque([root])

        while stack:
            curr = stack.popleft()
            if p.val < curr.val and q.val < curr.val:
                if curr.left:
                    lca = curr.left
                    stack.append(curr.left)
            elif p.val > curr.val and q.val > curr.val:
                if curr.right:
                    lca = curr.right
                    stack.append(curr.right)
            else:
                break
            
        return lca
                


    
        

        


        