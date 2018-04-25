class Solution:
    def maopao(self, nums):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    print(nums)
        return nums

a=Solution()
print(a.maopao([100, 20, 43, 21, 20]))

