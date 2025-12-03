# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()

        q.append(root)
        ans = []
        while q:
        
            a = q.popleft()
            if a == None:
                ans.append("null")
            

            else:
                ans.append(f"{a.val}")
                q.append(a.left)
                q.append(a.right)

        while ans and ans[-1] == "null":
            ans.pop()

        return ",".join(ans)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        arr =deque(list(data.split(",")))
        s = deque()
        a = arr.popleft()
        if a == "null":
            return None
        ans = TreeNode(a)
        s.append(ans)
        while arr:
           root2 = s.popleft()
           l = arr.popleft()
           l = int(l) if l !="null" else  "null"
           left = TreeNode(l) 
           root2.left = left
           s.append(left)

           if arr:
           
            r = arr.popleft()
            r = int(r) if r !="null" else  "null"
            right = TreeNode(r)

            root2.right  = right

            s.append(right)

        return ans

         


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))