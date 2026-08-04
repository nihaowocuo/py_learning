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
def func(a,b,*args,**kwargs):
    print(a, b,  *args, **kwargs)
# 此处第三位，我传入的实参为数字，系统提示我，应为str，但是实际为int
func(1,2,hello=465,haha=654)

