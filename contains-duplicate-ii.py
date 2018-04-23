'''
给定一个整数数组和一个整数 k，
判断数组中是否存在两个不同的索引 i 和 j，使 nums [i] = nums [j]，并且 i 和 j 的绝对差值最大为 k。
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if not nums:
        #     return False
        # elif len(nums) == len(set(nums)):
        #     return False
        # max_index = len(nums)-1
        # if k > max_index:
        #     return False
        # while max_index > 0 and max_index >=k:
        #     df = max_index-k
        #     if nums[df]!=nums[max_index]:
        #         max_index=max_index-1
        #     else:
        #         return True
        # return False
        dic = {}
        for index, value in enumerate(nums):
            if value in dic and abs(index-dic[value])<=k:
                return True

            dic[value] = index
        return False



a=Solution()
print(a.containsNearbyDuplicate([1,2,3,4],3))