# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue=[root]
        next_level=[]
        level=[]
        result=[]
        while queue:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_level.append(root.left)
                if root.right is not None:
                    next_level.append(root.right)

            queue=next_level
            result.append(level)
            level=[]
            next_level=[]

        return result


        
