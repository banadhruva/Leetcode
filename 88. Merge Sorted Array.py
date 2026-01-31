class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = nums1[:m] + nums2[:n]
        new.sort()
        for i in range(len(new)): 
            nums1[i] = new[i]
        return nums1 
