'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。
'''


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        ss = (s + s)[1:-1]
        print(ss)
        return ss.find(s) != -1

a = Solution()
print(a.repeatedSubstringPattern("acac acac"))