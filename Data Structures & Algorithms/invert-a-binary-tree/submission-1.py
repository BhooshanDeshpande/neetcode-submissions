class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root 
        
        if not root.right and not root.left:
            return root
        
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        root.left = right_inverted
        root.right = left_inverted

        return root