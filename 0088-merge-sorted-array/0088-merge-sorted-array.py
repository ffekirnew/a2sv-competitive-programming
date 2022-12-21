class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums2[j] < nums1[i]:
                nums1.pop()
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            else:
                i += 1
        i = len(nums1) - (len(nums2) - j)
        while i < len(nums1) and j < len(nums2):
            nums1.pop()
            nums1.insert(i, nums2[j])
            j += 1
            i += 1
                
        return nums1
            