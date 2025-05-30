class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final_ans = []

        def helper(candidates, Sum, target, ans, i, final_ans):
            if Sum > target:
                return
            if Sum == target:
                final_ans.append(ans[:])
                return
            if i >= len(candidates):
                return

            ans.append(candidates[i])
            helper(candidates, Sum + candidates[i], target, ans, i + 1, final_ans)
            ans.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            helper(candidates, Sum, target, ans, i + 1, final_ans)

        helper(candidates, 0, target, [], 0, final_ans)
        return final_ans