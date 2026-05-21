class Solution:

    class Tree:
        def __init__(self, ele):
            self.ele = ele
            self.roots = []

        def insert(self, strr):
            root = self

            for ch in strr:
                found = None

                for child in root.roots:
                    if child.ele == ch:
                        found = child
                        break

                if found:
                    root = found
                else:
                    new_node = Solution.Tree(ch)
                    root.roots.append(new_node)
                    root = new_node

        def search(self, strr):
            root = self
            ans = 0

            for ch in strr:
                found = False

                for child in root.roots:
                    if ch == child.ele:
                        found = True
                        root = child
                        ans += 1
                        break

                if not found:
                    return ans

            return ans

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        root = self.Tree(-1)

        for i in arr1:
            root.insert(str(i))

        ans = 0

        for i in arr2:
            ans = max(ans, root.search(str(i)))

        return ans