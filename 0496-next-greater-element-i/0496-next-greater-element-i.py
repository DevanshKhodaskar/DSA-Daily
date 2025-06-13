class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        for i in range(len(nums2)):
            a[nums2[i]] = -1
            for j in range(i,len(nums2)):
                if nums2[j]> nums2[i]:
                    a[nums2[i]] = nums2[j]
                    break
        ans = []
        for k in nums1:
            ans.append(a[k])
        return ans