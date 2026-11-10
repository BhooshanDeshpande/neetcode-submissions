# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        dct = defaultdict(list)
        while queue:
            curr = queue.popleft()
            dct[curr[1]].append(curr[0].val)

            if curr[0].left:
                queue.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                queue.append((curr[0].right, curr[1]+1))

        ans = []
        for k, v in dct.items():
            ans.append(v)

        return ans