class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # thought 1: O(n^2) time, O(1) space
        # for each value in the list, iterate the list again and find the sum equal to the target

        # thought 2: O(n*log(n)) time, O(n) space to record the index of the original list
        # sort the list first, and for each value in the list, use binary search to find the pair

        # thought 3: O(n) time, O(n) space
        # make a map, for each value in the list, if not in the map, put the {pair, index} in the map;
        # if in the map, return the index

        pair = {}
        i = 0
        for num in nums:
            if pair.get(num) is not None: # or: if nums[i] in pair:
                return [pair[num], i]
            pair[target - num] = i
            i += 1
        return []

# test
print Solution().twoSum([2, 7, 11, 15], 9)