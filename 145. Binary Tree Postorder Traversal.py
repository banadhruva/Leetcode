# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left_side=self.postorderTraversal(root.left)
        right_side=self.postorderTraversal(root.right)
        mid=[root.val]
        return left_side+right_side+mid
