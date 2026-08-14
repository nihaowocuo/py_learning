"""
zip：将多个可迭代的内容进行合并
sorted：排序
filter:筛选
map:映射
"""
# lst1 = ["耳根","辰东","圣骑"]
# lst2 = [43,42,41]
# lst3 = ["一念永恒","完美世界","修真聊天群"]
# 我想对其进行整体的重构，来达成，每个列表的第一位放在一起，第二位放在一起，第三位放在一起
# 我们可以通过循环把数据取出，取出后放入新的列表
# result = []
# for i in range(len(lst1)):
#     first = lst1[i]
#     second = lst2[i]
#     third = lst3[i]
#     # 将每三个数据封装为一个元组传入
#     result.append((first,second,third))
#
# print(result)

# 而zip函数可以自动的实现这种功能
# result1 = zip(lst1,lst2,lst3)
# print(zip)
# # 此为zip的对象
# print(result1)
# # 我通过打印这个类型和这个对象的帮助dir，是一致的
# # 可以发现有__iter__和__next__
# # 发现其实际上是一个迭代器
# print(dir(zip))
# print(dir(result1))
# 而我想要从迭代器中拿东西
# 则可以通过循环拿出
# 可以看到打印结果一致，不过为分开的元组
# for item in result1:
#     print(item)
# 注意当你要进行此操作时，请把上方的循环取出给注释掉
# 否则你的for循环会将迭代器中的内容全部取出
# 而你拿不到任何数据，因为数据已经被提前取出了
# 所以执行下面的操作会是一个空列表[]
# lst = list(result1)
# print(lst)

# locals：当前作用域的内容
# global：全局作用域的内容


# locals:帮你查看当前位置的局部变量的内容
# a = 123
# # 此时locals被写入到了全局作用域的范围内，此时看到的就是全局作用域的内容
# # 其表示当前作用域中的内容
# print(locals())

# def func():
#     a = 154
#     # 此时打印的只有154，即打印的只有当前的作用域中的内容
#     # 也就是说此函数中有哪些东西
#     print(locals())
#     return a
# func()

# global:把全局的内容引用到局部
# c = 12
# # print(globals())
# def func():
#     # 其能看到c的内容
#     print(globals())
#
# func()

# lst = [21,3,4,8,42]
# # receerse代表翻转
# # True代表降序从大到小
# # False代表升序从小到大
# lst = sorted(lst,reverse=True)
# print(lst)

# 我想将这种进行排序呢
# 很多时候我们不只需要给数字排序
# 甚至我想要按自己的规则去定义排序
# lst = ["垂杨","法斯塔纳","洛坦乐","卡罗尔其","诺威帕斯"]
# sorted(可迭代的内容，key=排序规则)
# sorted工作原理就是把列表中的每一项传递个排序函数，然后排序函数返回一个东西
# 然后sorted根据你所返回的东西来进行排序
# def func(item): #此时item所对应的是列表中的每一项数据
#     return len(item)
#
# # 注意是不能加()加了的话就成函数调用了，你要传的是函数
# sorted_lst = sorted(lst,key=func)

# 此处的函数功能是不是很简单，是否可以使用lambda表达式进行简化
# x为接收函数的名字
# 这个fun是专门为此函数准备的，那我们是否可以把这个函数名也省略掉
# fun = lambda x: len(x)
# 默认升序排列
# s = sorted(lst, key=fun)
# 此时结果一致
# s = sorted(lst, key=lambda x: len(x))
# print(s)

# 练习：
# lst = [
#     {"id": 1, "name": "战争机器", "age": 17, "adress": "夜之城"},
#     {"id": 23, "name": "战争魔法", "age": 27, "adress": "夜城"},
#     {"id": 3, "name": "战争断绝", "age": 16, "adress": "之城"},
#     {"id": 54, "name": "战争短剑", "age": 89, "adress": "夜之"},
#     {"id": 65, "name": "战争杀戮", "age": 15, "adress": "夜断城"},
#     {"id": 68, "name": "战争坑野", "age": 41, "adress": "断城"},
#     {"id": 37, "name": "战争罚曳", "age": 28, "adress": "夜断"}
# ]
# # 1.根据每个人的年龄进行排序
# # d为接收参
# s = sorted(lst, key=lambda d: d["age"])
# print(s)
# # 2.根据编号进行排序
# s1 = sorted(lst, key=lambda d: d["id"])
# print(s1)

# lst = ["灰毛","卡夫卡","银狼","流萤","黄泉","啊哈"]
# #           此为筛选条件
# # 拿出每一项数据交给前面的函数，有这个函数的返回真假，来决定该数据是否保留
# #                 x内就是取的这个一个的数
# # 也可以用not
# # f = filter(lambda x: x.startswith("银"), lst)
# f = filter(lambda x: not x.startswith("银"), lst)
#
# # 其为生成器
# print(f)
# # 我就可以通过list把生成器中的内容拿空并且组成列表
# # 只有银狼被存入
# # 而此时修改后，便是除了银狼后其他均可
# print(list(f))
# filter:根据你函数计算的结果来决定你该元素是否进行保留
# 而map这是将lmabda计算的结果作为最终结果

lst = [1,2,3,4,5,6]
# 我要使用map将列表中的每一项计算他们的平方
# 此为列表推导式
# result = [item * item for item in lst]
# 但我们也可以使用lambda表达式进行实现
# 第一个参数为函数，第二个参数为可迭代的对象
# lambda为匿名函数
# 将列表中的每一项扔过去
# 返回值为你所需要的值
r = map(lambda x: x * x,lst)
# print(result)
print(list(r))
