'''杨辉三角'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ls = [1]
        ls1 = []
        a=1
        while a <=numRows:
            ls1.append(ls)
            ls = [1] + [ls[i]+ls[i+1] for i in range(len(ls)) if i+1 < len(ls)] + [1]
            a+=1
        return ls1

a=Solution()
print(a.generate(0))