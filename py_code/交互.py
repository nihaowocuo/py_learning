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
while True:
    content = input("请输入你要说的话：")
    if content == "quit":
        break
    print("发送给他人：",content)

