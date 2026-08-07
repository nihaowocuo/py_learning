# 函数的概念
# 参数
# 返回值
# py中内置的函数
# 函数：对某项功能或者代码块进行封装，需要使用时直接调用即可
# 参数：可以在函数调用时传递一些信息
#   形参：在函数定义时，需要准备一些东西来接收，要传递的信息
#   实参：实际调用时传递的信息
    #   具体分辨，你在调用函数传递的信息为实参
    #   函数接收处的为形参（其实际上就是个装载真正信息的容器
    #   py的特点，其是无需主动定义变量类型

# 定义
# def 函数名字():
# 此时仅为定义，只有有人调用时才会用
# def go_home():
#     print("打车")
#     print("回家")
#     print("吃饭")
#     print("睡觉")
# range的范围此处是直接使用的，未展现范围，以下的括号中是几，那就是循环多少次
# for i in range(2):
#     go_home()

# 我想定义一个和人对骂的功能
# 但如果我要骂谁，骂道什么程度
# 则需要我们去传递信息
# def maren(name,level):
#     print("1.怒目而视",name)
#     print("2.验证交涉",name)
#     if level>66:
#         print("3.死不要脸",name)
#     else:
#         print("3.蠢货",name)
#     if level>99:
#         print("4.骂完收工",name)
#
# maren("垂杨",188)
# maren("废物",21)

# 请用函数编写一个计算器，可以计算加减乘除，并且返回结果：
# def jisuan(num1,opt,num2):
#     if opt == "+":
#         return num1+num2
#     elif opt == "-":
#         return num1-num2
#     elif opt == "*":
#         return num1*num2
#     elif opt == "/":
#         return num1/num2
# print("此为计算器：")
# num1 = int(input("数字_1："))
# opt = input("请输入您要运算的法则")
# num2 = int(input("数字_2："))
# result = jisuan(num1,opt,num2)
# print(result)

# 实参与形参之别：
# 实参：
#     1.位置参数:按位置传参数
#     2.关键字传参:按照参数名字传参
#     3.混合参数:位置参数放前面,关键字参数放后面
#     4.实参要执行的时候,必须要保证形参存在
#         也就是说,一旦我设置了形参,那再调用此函数时,必须放入相关的实参
#     此为强制规则
# 例如:此即为位置参数
# open("xxx",mode="r",encoding="utf-8")
# # 这样会报错
# open(mode="r",encoding="utf-8","xxx")
# # 但我们可以直接指定关键字此为关键字传承
# open(mode="r",encoding="utf-8",file="xxx")
#
# # 此为形参
# def eat(zhu,fu,tang,tian):
#     print(zhu,fu,tang,tian)
# # 此为实参
# # 此为位置传参
# eat("大米饭","西红柿炒鸡蛋","疙瘩汤","老冰棍")
# # 此为关键字参数
# eat(zhu="大米饭",fu="西红柿炒鸡蛋",tang="疙瘩汤",tian="老冰棍")
# # 混合参数
# eat("大米饭","西红柿炒鸡蛋",tang="疙瘩汤",tian="老冰棍")

# 形参：
# 位置 > *args > 默认值 > **kwargs
# 1.位置参数
# 2.默认参数
# 3.动态传参


# 2.默认参数
# 你可以直接为你的形参进行赋值默认值
# 这样我在输入男性名字时就不需要其性别，而女性录入时会有传来的实参进行覆盖
# 也就是说，实参不传递，则采用默认值
# 注意：当使用默认值参数时，需要将默认值参数放置在位置参数后面
# def luru(name,age = 18,sex): # 这样就会报错
#     print(name,age,sex)

# def luru(name, age, sex="男"):
#     print(name, age, sex)
#
# luru("垂杨",18,)
# luru("落幕",20,"女")
# luru("诺克",19,)
# luru("阿鸾",18,"女")

# 3.动态传参
    # 1.*args(表示参数名),接收所有的位置参数的动态传参
    # *args要在默认值之前才不报错
    # 2.**kwargs关键字函数
    # 3.混合传参
# 当我想要执行此参数时，必须每个参数都进行传递，除非你有默认值，
# 否则报错
# def eat(zhu,fu,tang,tian):
#      print(zhu,fu,tang,tian)

# 即此报错：eat() missing 2 required positional arguments: 'tang' and 'tian'
# eat("米饭","西红柿炒鸡蛋")
# 也就是说当我们要调用参数时无法确定传入参数个数
# 所以我们得办法不把参数固定，或者说
# 让一个东西能接受任意的参数与个数

# 1.
    # *表示位置参数的动态传参
    # *号接收的值统一被放到了一个元组内
    # def eat(*food):
    #     print(type(food))
    #     print(food)
    # eat("米饭","炒菜")
    # # 也就是说任意类型的都可以被接受
    # eat("米饭","炒菜",18)

# 2.
# def eat(zhu,fu,tang,tian):
#      print(zhu,fu,tang,tian)
# # 出现报错
# # eat() missing 3 required positional arguments: 'fu', 'tang', and 'tian'
# eat(zhu="米饭")

# **表示关键字传参
# 此为字典的形式
# def eat(**food):
#     print(type(food))
#     print(food)
# eat(zhu="米饭")
# c="哈哈",
# c,
# 3.
# def func(a,b,*args,c="哈哈",**kwargs):
#     # 此处报错是因为，你在形参时需要表示动态传参加*
#     # print(a, b, c, *args, **kwargs)
#     print(a, b, c, args, kwargs)

# 此处第三位，我传入的实参为数字，系统提示我，应为str，但是实际为int
# 注意，此处c的默认值要生效，意味着在位置参数b之后不能有任何数据，关键字可以，是已经被锁定了，关键字，强制会传入**kwargs
# 这样是会报错的,在实参中,位置参数在前,关键字参数在后
# func(hello=456,haha=654,1,2,3,4)
# func(1,2,3,4,hello=456,haha=654,)

# 可以没有限制的接收任何参数
# def fun2(*args,**kwargs):
#     print(args)
#     print(kwargs)

# 补充:
# stu_lst = ['诺亚','白来',"二清","扒鸡"]
# def func(*args):
#     print(args)

# 接下来我想让列表中的每一项作为参数传给函数
# func(stu_lst[0],stu_lst[1],stu_lst[2],stu_lst[3])
# 但如果列表非常长呢
# py中的特有语法
# *在实参位置,把列表打散成位置参数进行传递
# 我们把stu_lst中打散成位置参数一个个传递
# 这样就会把列表打散成位置参数进行传递
# 注意:这是*在实参的位置
# func(*stu_lst)
# 同理字典也可以此操作
# **也可以把字典转成关键字参数进行传递

# 5.函数的返回值:给调用方返回的结果
#         关于return:
#             1.如果函数内没有return,此时外界接收到的是啥,是none
#             2.return加一个值，此为常用，外界可以接收到一个数据
#             3.只写了return,后面不跟值,这意味着return是直接结束,return后函数立即停止,并返回内容,
#               此时外界收到的为none
#               return是可以返回多个值的,这时候返回的是元组，存放了所有的返回值
#               例如return 1,2,3,4，就会出现元组
# def jisuan(a,opt,b):
#     if opt == '+':
#         print(a+b)
#         return a+b
# # 需要一个变量存储返回的结果
# resule = jisuan(2,"+",5)
# 然后可以在对其进一步操作

# def jisuan(a,b):
#     print(a,b)
#     return
#     print(a+b)
# 此可以发现在return之后的print并未打印
# 实际上就是会直接结束中断
# jisuan(3,4)

# 可以看到返回的内容是元组
# def fanhui():
#     return 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
#
# result = fanhui()
# print(result)

# 内置函数：可直接拿来用，无需你定义的（也就是说事前准备好的）
# py中自带的
# 例如:
# print("你好世界！")

# 基本数据类型
    # s = "123"
    # i = int(s)
    # b = bool(s)
    # f = float(s)
    # complex 复数，实部加虚部。i**2 = -1 i的平方等于-1

# 进制转换类：
    # bin2进制，oct8进制，hex16进制
    # a = 18
    # print(bin(a))
    # print(oct(a))
    # print(hex(a))
    # a = 0b10010
    # print(int(a)) # 转十进制

# 数学运算类：
    # sum,min,max,pow
    # a = 10
    # b = 3
    # # 此为10的3次方
    # print(pow(a,b))
    # # 这个表示的是次方
    # # 10的3次方
    # print(a ** b)
    #
    # sum
    # lst = [12,45,65,58,132]
    # print(max(lst))
    # print(min(lst))
    # print(sum(lst))

# 与数据结构相关：
    # list,把你传入的东西转为列表
    # s = {1,2,3,4,5}
    # # list他是如何转换放入的，
    # # lst = list(s)
    # # 此时你会发现是单个字符存入
    # lst = list("你好啊")
    # # 所以其实际逻辑是循环放入
    # # 类似这种操作，循环一个装入一个
    # # for item in s:
    # #     lst.append(item)
    # print(lst)
    #
    # tuple,是变为元组

# 相关内置函数：
# reversed(),翻转，把整个列表翻过来，最大放到最小
# slice(),作用是切片
# 例如这个[1:4:2]
# 从一到四每三个出来一个
# result = slice(1,4,2)
# print("啊啊啊啊啊啊啊啊啊啊"[result])

# str,repr

# format,ord,chr
# format,格式化
# a = 18
# a = 18000
#
# # b表示的是二进制,o为8进制，x为16进制
# # 我为什么要用这种，此前不是有特定转换的数呢
# # 我如果要一个定长的二进制呢
# # 此为5位，0代表你要补充的数，而8表示补到几位
# # 但如果数超了呢，则按原样显示，当你位数不足时才进行补足
# print(format(a,'08b'))
# # print(format(a, 'o'))
# # print(format(a, 'x'))

# ord:
# a = "中" # 在py内存中所使用的时unicode编码
# # 汉字在其中是有编码的，而我可以通过ord能够实际的取到此字的编码
# ord只能接收单个字符，chr也只能在范围内运行
# print(ord(a))
# # 给出编码位置，我将其变为汉字
# print(chr(ord(a)))

# for i in range(65536):
#     # 同时我想打印结果中有一个空格的效果
#     # 如果不加end，其默认时\n换行
#     print(chr(i)+" ",end="")

# forzenset,表示被冻结的集合，即不可变的集合，无法增删改查，和普通的集合操作差不多

# enumerate:
# all,any