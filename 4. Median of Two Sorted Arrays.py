class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # thought: binary search

        total = len(nums1) + len(nums2)
        half = total / 2
        if total & 1 == 1:
            return self.findKthLargestNum(nums1, nums2, half + 1)
        left = self.findKthLargestNum(nums1, nums2, half)
        right = self.findKthLargestNum(nums1, nums2, half + 1)
        return (left + right) / 2.0

    def findKthLargestNum(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKthLargestNum(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        left = min(len(nums1), k/2)
        right = k - left
        if nums1[left-1] < nums2[right-1]:
            return self.findKthLargestNum(nums1[left:], nums2, right)
        else:
            return self.findKthLargestNum(nums1, nums2[right:], left)

# test
nums1 = [5]
nums2 = [1,2,3,8,9]
print Solution().findKthLargestNum(nums1, nums2, 4)

nums1 = [1, 3]
nums2 = [2]
print Solution().findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2]
nums2 = [3, 4]
print Solution().findMedianSortedArrays(nums1, nums2)
