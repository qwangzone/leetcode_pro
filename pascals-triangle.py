'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        num = [[1], [1, 1]]
        if numRows == 1:
            return num[0:1]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []

        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []

        return num

a=Solution()
for i in a.generate(3):
    print(i, end='\t')
    print("\n")
#print(a.generate(5),end='\t')