"""
匿名函数：
    其实际上就是一个lambda表达式
    语法：
        变量 = lambda 参数,参数2,...: 返回值
    能帮我一句话后创造一个函数
"""
# lambda:作用可以简化表达
# def func():
#     print("hello")
#     return 999
#
# ret = func()
# print(ret)

def func(a,b):
    return a+b

ret = func(12,13)
print(ret)

# 所有通过lambda生成的函数都叫这个
fn = lambda a, b : a+b
# 其就像正常的函数一样需要进行调用
ret1 = fn(12,13)
print(fn)
print(ret1)