"""
生成器：
    其本质就是迭代器
    所以生成器拥有迭代器的所有性质

    创建生成器的方案：
        1.生成器函数
        2.生成器表达式

    1.生成器函数：
        其内部含有一个关键字yield
        只要函数中出现了yield函数，它就是一个生成器函数
        作用：
            1.可以返回数据
            2.可以分段的执行函数的内容，
            通过__next__()或者next()可以执行到下一个yield位
    2.生成器表达式
        其语法规则就和推导式类似
        (数据 for循环 if判断)

"""
# def func():
#     print(123456)
#     # return 999
#     # generator就是生成器，生成器函数执行时得到的是生成器
#     # 而并不会执行函数
#     # <generator object func at 0x00000211C2B25B40>
#     yield 999
#     # yield本身也有返回的意思，
#     # 和return不一样，return是立即执行然后返回结果
#     # 而yield只有当你执行到next的时候才能返回数据
#
#
#
# ret = func()
# # 此打印的生成器的地址
# print(ret)
#
# # 我们可以像使用迭代器一样使用它
# print(ret.__next__())
# # 那我再next一遍呢
# # 会发现再次报错，StopIteration
# # 和迭代器一样
# print(ret.__next__())


# def func():
#     print(123)
#     yield 666
#     print(456)
#     yield 999
#
# # 此处创建了个生成器
# ret = func()
# # print(ret)
# # 拿到生成器后再执行
# # 当执行时函数开始
# # 结果发现执行到yield返回666便结束了
# print(ret.__next__())
# # 那让我们再执行一次
# # 会发现其执行了后续的操作
# # 即进行了分段的操作执行
# print(ret.__next__())


# 实际应用举例，例如我想要去工厂定制20件衣服
# def order():
#     lst = []
#     for i in range(20):
#         lst.append(f"衣服{i}")
#     return lst
#
# lst = order()
# for i in lst:
#     print(i)

# 但我一次性用不了这么多的衣服
# 我能否使用一部分一部分的请求生成
# 此时就可以考虑使用生成器

# def order():
#     lst = []
#     for i in range(1000):
#         lst.append(f"衣服{i}")
#         # 此处我采用的是len计算的长度而非依靠
#         # 单纯i的循环值
#         if len(lst) == 50:
#             # 我使用了yield，返回这已经准备好的50件衣服，
#             # 但我需要下次再进行来取时呢
#             yield lst
#             # 此时我仍需要在此处继续执行
#             # 让列表清空，再次拿50件衣服
#             # 此时我的程序一次性就只进行50件衣服的返回
#             # 注意此处lst是在if判断之下的，只有当你已经生成50件的时候
#             # 才进行对列表重新赋值
#             lst = []
#
# # 由于我的函数中含yield，所以此处clothes接收的返回值也是生成器
# # 而我需要从中取数据，便要使用next()内置函数
#
# clothese = order()
# print(clothese)
# print(next(clothese))
# # 而当下一次执行时，是从重新为列表赋值处开始执行的
# # 注意在函数中我所使用的是len函数计算内部数据长度
# # 而非完全重新创建一个lst，这意味着，我循环的i是不会再次从0开始的
# print(next(clothese))



# 生成器表达式:
gen = (i**2 for i in range(10))
# 如果是列表推导式的话,我们拿到的式i的平方,可以通过print直接打印
# 但由于此为生成器其只是这个生成器的地址
# print(gen)
# 此为0的平方
# print(gen.__next__())
# # 逐步打印平方
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# 我能否一次性全部拿出

# 此时为何未出现越界报错
# for item in gen:
#     print(item)
# 我能否再次进行调用
# 发现再次爆出此错误:StopIteration
# print(gen.__next__())
# for循环实际上是已经简化的了
# for item in gen: 其实等价于下面这段
        # 此为实际上的for循环,其是有try,catch的存在是可以捕获报错并且丢出的
        # 其默认帮我们执行了此操作,所以不会跳出报错
        # _it = iter(gen)          # 拿到迭代器
        # while True:
        #     try:
        #         item = next(_it) # 反复调 next()
        #     except StopIteration:
        #         break            # ← 收到"结束信号"就 break，不往外抛
        #     print(item)


# 那我能否将其变为一个列表
# lst = list(gen)
# print(lst)
# 注意执行此操作时
# 注意list,set()这些本质上是有一个循环迭代在内的
# 验证：
# 可以发现其并非像"垂杨风落"这样这个字符串，
# 而是逐个的单个字符
# s = list("垂杨风落")
# print(s)

for item in gen:
    print(item)
# 此生成器（本质为迭代器）在for循环结束时已经被拿空了
# 因此无法再取出，打印的时空列表
# 生成器表达式是一次性的东西，一次性拿光后就没了
lst = list(gen)
print(lst)










