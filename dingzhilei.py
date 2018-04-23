'''
演示定制类__getattribute__和__getattr__用法
'''
class Studen:
    def __init__(self):
        print('调用__init__')
        self.name = 'wq'
        self.age = 20

    def __getattr__(self, item):
        print('调用__getattr__')
        if item == 'sex':
            return 'boy'

    def __getattribute__(self, item):
        print('调用__getattribute__')
        if item == 'score':
            return 90

a = Studen()
print(a.name)
print(a.sex)
print(a.score)
print(a.sa)