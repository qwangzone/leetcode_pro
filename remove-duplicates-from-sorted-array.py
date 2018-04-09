import unittest
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_start = 0
        a = len(nums)
        for i in range(1, a):
            print(i)
            if nums[i] != nums[index_start]:
                index_start = index_start + 1
                nums[index_start] = nums[i]
            # else:
            #     nums.remove(i)
            #     a = a-1
            #     index_start = index_start + 1
        return index_start + 1



a = Solution()
lis = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
a.removeDuplicates(lis)
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
