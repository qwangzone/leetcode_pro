def plusOnemy(digits):
    num = ''
    lis = []
    for i in digits:
        num = num + str (i)
    result = int(num) + 1
    for i in str(result):
        lis.append(int(i))
    return lis

def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

print(plusOne([999989]))