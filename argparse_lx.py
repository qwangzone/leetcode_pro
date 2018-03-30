import argparse

def math_add(a,b,c):
    d = a + b + c
    #e = a * b * c
    return d

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='描述参数')
    parse.add_argument('a', metavar='a', type=str, nargs=1, help='diyige')
    parse.add_argument('b', metavar='b', type=str, nargs=1, help='diyige')
    parse.add_argument('c', metavar='c', type=str, nargs=1, help='diyige')
    args = vars(parse.parse_args())
    print(args)
    print(type(args))
    print(args['a'])
    #print(math_add(int(args['a'][0]), int(args['b'][0]), int(args['c'][0])))
    print(math_add(args['a'][0], args['b'][0], args['c'][0],))