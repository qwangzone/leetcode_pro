'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，
使 nums [i] 和 nums [j] 的绝对差值最大为 t，并且 i 和 j 之间的绝对差值最大为 ķ。
'''
import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False

a=Solution()
#a.containsNearbyAlmostDuplicate([-3,3,2,1,2],2,4)
print(a.containsNearbyAlmostDuplicate([-3,3,2,1,2],2,4))