'''给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。'''
import unittest
#第一种做法，不符合要求，数组很长时会超时
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # index_start = 0
        # a = len(nums)
        # for i in range(1, a):
        #     print(i)
        #     if nums[i] != nums[index_start]:
        #         index_start = index_start + 1
        #         nums[index_start] = nums[i]
            # else:
            #     nums.remove(i)
            #     a = a-1
            #     index_start = index_start + 1

        for i in nums:
            for j in range(nums.count(i) - 1):
                nums.remove(i)
        return len(nums)
        #return index_start + 1

#更优做法
class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = 0

        if len(nums) == 0:
            return 0
        nums_len = nums_len + 1
        last_node = nums[0]
        for i in range(len(nums)):
            if nums[i] != last_node:
                last_node = nums[i]
                nums[nums_len] = nums[i]
                nums_len = nums_len + 1
        return nums_len

a = Solution2()
lis = [0,1,1,]
print(a.removeDuplicates(lis))
print(lis)

# class TestSolution(unittest.TestCase):
#     def setUp(self):
#         self.so = Solution()
#         print("start=====")
#
#     def test_case(self):
#         data = [1, 1, 2]
#         result = self.so.removeDuplicates(data)
#         print(data)
#         lis_len = len(data)
#         self.assertEqual(result, lis_len)
#         self.assertEqual(data, [1, 2])
#
#     def tearDown(self):
#         print("end===")
#
# if __name__ == '__main__':
#     unittest.main()
