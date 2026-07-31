# 1.算术运算
#     + - * / %（取余） //（整除）
# 2.比较运算
#     > < >= <= ==(条件判断）!=（不等于）
# 3.赋值运算
#     += -= *= /= 等  即1中的运算
#     =（赋值运算）
# 4.逻辑运算
#     运算顺序：先括号 其次not 再次and 最后or
# 5.成员运算
#     in :判断某元素是否在某xxx出现了
#     not in :判断某元素是否在某xxx没出现

# 1.
# a = 10
# b = 3
# # 此为取余运算
# result = a % b
# print(result)

# 示例：用户输入任意数字，来判断是否为35的倍数
# num = int(input("请输入您要检验的数字："))
# if  num % 35 == 0:
#     print("是35的倍数！")
# else:
#     print("不是35的倍数")

# n = 20
# a = 3
# # 此为整除，直接舍去不够除数的数
# # 直接输出6
# c = n // a
# print(c)

# 我想让a，b互换
# a = 20
# b = 30
# 此时正常
# print(a)
# print(b)
# # 此为按顺序进行运算
# # 一旦运算后，就会进行改动
# a = b
# b = a
# print(a)
# print(b)
# 通用语言互换
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# py中特有的
# 此为解构，本质是右侧为一个元组
# a,b = b,a
# # 将元组中的b扔给a，把元组中的a扔给b
# a,b = (b,a)
#
# print(a)
# print(b)

# 4.逻辑运算
# and   并且，两侧式子都符合条件才真
# or    或者，式子两侧有一个成立，即真，全假才假
# not   非，相反，例如真为假，假变真
# 例如用户登录
# user_name = input("请输入你的用户名：")
# user_password = input("请输入你的密码：")
# # 密码和用户名都正确
# # if user_name == "admin" and user_password == "123456":
#
# # 仅需要用户名和密码任意一个对即可
# # if user_name == "admin" or user_password == "123456":
#
# # 此为取反
# if not user_password == "123456":
#     print("登陆成功！")
# else:
#     print("登陆失败！")

# 5.成员运算
# lst = [1,2,3,4,5]
# print(4 in lst)
# print(6 in lst)
# print(7 in lst)
# print(8 in lst)