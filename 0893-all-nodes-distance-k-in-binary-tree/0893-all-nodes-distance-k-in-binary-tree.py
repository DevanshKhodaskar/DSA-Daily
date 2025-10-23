# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = self.parentarray(root, [])
        ans = []
        visited = set([target])
        temp = set([target])
        for i in range(k):
            temp =set( self.helper(parent,temp,visited))
               

        ans = [node.val for node in temp]

        return ans

        


        

    def parentarray(self,root,a):
        
        if root == None:
            return a
        else:
            if root.left !=  None:
                a.append([root,root.left])
            if root.right != None:
                a.append([root,root.right])
            if root.left !=  None:
                self.parentarray(root.left,a)
            if root.right != None:
                self.parentarray(root.right,a)

        return a
            

    def helper(self,parent,arr,visited):
        ans = []
        for i in arr:
            if i.left and i.left not in visited:
                ans.append(i.left)
                visited.add(i.left)
            if i.right and i.right not in visited:
                ans.append(i.right)
                visited.add(i.right)
            for par,child in parent:
                if i == child  and par not in visited:
                    ans.append(par)
                    visited.add(par)
                    break
            
        return ans

         
        