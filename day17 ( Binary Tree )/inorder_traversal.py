# Date Completed: 26th June 2022
# Problem Link: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# References
# 1. https://zhenyu0519.github.io/2020/03/10/lc94/#code-2-iteratively
# 2. https://www.youtube.com/watch?v=lxTGsVXjwvM&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=13

############################
# ITERATIVE SOLUTION
############################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else:
                if stack:
                    node = stack.pop()
                    res.append(node.val)
        return res


# Success
# Details
# Runtime: 43 ms, faster than 57.11% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 12.90% of Python3 online submissions for Binary Tree Inorder Traversal.


############################
# RECURSIVE SOLUTION
############################
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None: return []
#         def dfs(root,res):
#             if root is None: return
#             dfs(root.left,res)
#             res.append(root.val)
#             dfs(root.right,res)
#             return res
#         return dfs(root,[])
