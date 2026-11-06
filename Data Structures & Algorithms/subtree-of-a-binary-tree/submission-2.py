# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Level order traversal
        queue = deque()

        queue.append(root)
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.val == subRoot.val:
                    print(f"Matched {curr.val} {subRoot.val}")
                    if self.isSameTree(curr, subRoot):
                        return True
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        none_count=[p,q].count(None)
        if none_count == 1:
            return False
        elif none_count == 2:
            return True

        if (p.val != q.val):
            return False

        b1 = self.isSameTree(p.left, q.left)
        b2 = self.isSameTree(p.right, q.right)

        return (b1 and b2)



        