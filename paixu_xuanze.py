class Solution:
    def xuanzepaixu(self, nums):
        for i in range(len(nums)):
            max_index = 0
            for j in range(len(nums) - i):
                if nums[max_index] < nums[j]:
                    max_index = j
                    print(nums)
            nums[max_index], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[max_index]
        return nums
a=Solution()
print(a.xuanzepaixu([1,4,2,7,5]))