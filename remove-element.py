'''给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。'''
#My solusion
class Solution1:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(nums.count(val)):
            nums.remove(i)
        return len(nums)

#更优做法
class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
#最优做法(原地删除最佳做法）
class Solution3:
    def removeElement(self, nums, val):
        nums_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nums_index] = nums[i]
                nums_index += 1
        return nums_index
a = Solution3()
b=[3,2,2,3]
print(a.removeElement(b,2))
print(b)
