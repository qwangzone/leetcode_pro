'''假设你有 n 个版本 [1, 2, ..., n]，你想找出第一个错误的版本，导致下面所有的错误。

你可以通过 bool isBadVersion(version) 的接口来判断版本号 version 是否在单元测试中出错。
实现一个函数来查找第一个错误的版本。您应该尽量减少对 API 的调用次数。
'''


class Solution(object):
    def firstBadVersion(self, nums):
        """
        :type n: int
        :rtype: int
        """
        left_index = 0
        right_index = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if nums[0] == False:
            return nums[0]
        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            #print(mid)

            if nums[mid] == False:
                if nums[mid-1] == True:
                    return mid
                else:
                    right_index = mid - 1
            else:
                left_index = mid + 1
import bisect
bisect.bisect()


a=Solution()
print(a.firstBadVersion([True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,
                         True,True,True,True,True,True,True,
                         True,True,True,True,True,
                         True,True,
                         True,True,True,True,True,False,False,False,False,False,False,False,False,False,False]))