'''给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1中，使得 num1 成为一个有序数组。

注意:

你可以假设 nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。在 nums1 和 nums2 中初始化的元素的数量分别是 m 和 n。
 '''
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # while n > 0:
        #     if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
        #         nums1[m + n - 1] = nums2[n - 1]
        #         n -= 1
        #     else:
        #         nums1[m + n - 1] = nums1[m - 1]
        #         m -= 1
        nums1.extend(nums2)
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

a = Solution()
nums2 = [5,6,7,8,9]
nums1 = [1,2,3,4]
a.merge(nums1,4,nums2,5)
print(nums1)