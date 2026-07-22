# a = float(input("请输入第一个数字"))
# print(type(a))
# print("\n")
# b = float(input("请输入第二个数字"))
# c = a + b
# print(c)

# name = '无言'
# print(name)
# word = '是最大的沉默'
# print(word)

# money = float(input("请输入当前所剩的钱\n"))
# if money >= 7:
#     print("我能吃泡面")
# else:
#     print("没钱吃饭了")
# print("我要回家")

# 多次判断,判断嵌套
# money = float(input("请输入当前资金：\n"))
# if money >= 50:
#     print("吃大餐")
# elif money >= 20:
#     print("吃水饺")
# elif money >= 10:
#     print("吃泡面")
#
# print(f"当前剩余的钱：{money}")

# 循环
# i = 1
# while i <= 13:
#     print(i)
#     i = i + 1
# i = 1
# sum = 0
# while i <= 15:
#     sum = sum + i
#     i = i + 1
# print(sum)
#     注意：while常用于死循环
# while True:
#     content = input("请输入你要说的话：")
#     if content == "quit":
#         break
#     print("发送给他人：",content)
# for循环的语法：
# py中for循环不同于我此前学习到的语言，其可以
# for 变量 in 可迭代的对象:
#     代码
#     将可迭代的每一项东西都拿出来，赋值一遍给变量
#     我此前接触最多的是数字，下方的例子为字符串
# name = "垂杨，你好啊"
# for str in name:
#     print("本次输出的为：",str)
# for 循环计数采用 range
#     注意：以下均不包含n
#     # 从零数到n
#     range(n):
#     # 从m数到n
#     range(m,n):
#     # 从m数到n，中间间隔t
#     range(m,n,t):
# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)

# for i in range(2,10,2):
#     print(i)