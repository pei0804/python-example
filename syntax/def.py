# 普通の関数定義
def add_one(n):
    return n + 1


print(add_one(1))
print(add_one(n=1))


# デフォルト値
def add(a=0, b=0):
    print('a={}, b={}'.format(a, b))
    return a + b


print(add(a=1))
print(add(1, 2))


# 可変長引数
def listAdd(*args):
    r = 0
    for i in args:
        r += i
    return r


listAdd(1, 2, 3)


# キーワード引数で可変長引数
def multiArgs(*args, **kwargs):
    print(args)
    print(kwargs)


multiArgs(1, 2, a=3, b=4)
