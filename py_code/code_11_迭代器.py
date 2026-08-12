"""
迭代器
for 变量 in 可迭代:
    pass
共性，每一种数据类型都自己提供了一个可以迭代的东西，即迭代器
迭代器可以帮我们把数据类型中的所有数据逐一的拿到

# iterable：可迭代的东西，
# iterator:迭代器
# 如：str,list,tuple,dict,set,open
获取迭代器的两种方案：
    1.iter()内置函数可以直接拿到迭代器
    2.__iter__  特殊方法
从迭代器中拿到数据也有两种方法：
    1.next()内置函数
    2.（变量名）.__next()的方法进行取数据

for循环里，一定是要拿迭代器的，所以所有不可迭代的东西都无法使用for进行循环
需要__next()的出现或者next()，进行拿取数据

总结：迭代器统一了所有不同类型的遍历工作
也就是说它让不同的数据类型有了相同的遍历方式
反之，只要能拿到迭代器的都可以进行for循环

在此前str，list，tuple等还有索引可以进行取
但是dict，set集合，文件操作这些不可数的呢，便是此处迭代器的作用

注意：迭代器本身也是可以迭代的

迭代器的特性：
    1.只能向前，不能反复（即不能从后向前拿）其有自己内部设定的顺序
    2.特别的节省内存，说是迭代器，其实其内部是存储了指针一样的东西，其并没有真实的数据，只是记录了其位置
    3.惰性机制，你一旦用iter()获取了一个迭代器，只要你不访问它，他就不会向下挪移位置，
    什么时候执行next，才会进入下一个
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))

"""
s = "你好我是垂杨"
it = s.__iter__()
for i in it:
    # 并无报错，可以验证迭代器本身也是可以迭代的
    print(i)
# it = iter("你好啊，天才")
# # 此打印的为内存地址
# print(it)
# # 拿到了第一个数据
# print(next(it))
# # 逐个拿出
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# 当我已经全拿出打印后，我能否继续再拿？
# StopIteration：报错，其表示你前面的功能已经将迭代器中的数据全部拿出，
# 其实际就是，迭代已经停止了，不可以再从迭代器中拿数据了
# 相当于一次性的，但我如果还想从原来的迭代器中再拿数据呢？
# print(next(it))

# 则，我需要重新再获取获取一个迭代器
# 法2：__iter__
# it = "你好啊".__iter__()
# print(it)
# # 表示类型为迭代器 <class 'str_iterator'>
# print(type(it))
# print(next(it))
# print(it.__next__())
# print(it.__next__())


# for c in "你好我是垂杨":
#     print(c)

# 例如此，把字符串内的每一项东西，挨个提出赋值给c并且输出

# for c in "你好我是垂杨":
#      print(c)
# 但我如果使用int类型的数据，却无法打印
# 'int' object is not iterable
# for c in 123:
#     print(c)

# 模拟for循环的工作原理：
# s = "我是data"
#
# # 但在循环之前我是否应该先拿迭代器
# it = iter(s)
# while 1:
#     # 尝试运行内部的代码，若不出错就正常执行
#     # 若报错了，我需要查看你所出的错误，若错误类型为StopIteration
#     # 则执行break退出，程序仍在运行只是跳出循坏了
#     try:
#         # for循环的循环体
#         data = it.__next__()
#         print(data)
#         # StopIteration,当我全部拿取后由于无限制，再全部拿取后仍进行拿取操作，于是报错
#         # 我该如何避免此报错
#     # 此为py中的异常处理
#     except StopIteration:
#         break
# print(123456)