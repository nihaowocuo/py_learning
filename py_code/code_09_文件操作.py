# 1.找到你想要打开的文件，双击打开它
# mode是模式，读写操作
# encoding为编码方式，此文件采用的是什么编码的方式
# open(文件路径,mode="",encoding="")
#     文件路径：
#         1.绝对路径
#               用的较少
#         2.相对路径
#           ../上一层文件夹
#               相对于你当前文件的路径
# 读写文本时，需要给encoding
# 图片无法
# f = open("文本测试.txt",mode="r",encoding="utf-8")
# content = f.read()
# 读取成功
# print(content)

# 但此文件较小所以可以直接全读出来
# 那以后文件大了呢，或者我想要只读一部分呢？

f = open("文本测试.txt",mode="r",encoding="utf-8")
# line = f.readline()
# 叠加使用，读取后然后去除字符串两侧的空白符
# 此次打印可以看出未占据两行
# 原因在于strip()去除了空白符（包含了换行符）
#

# 最重要的文本读取方式
# f我可以直接循环
# 直接全部循环出来了
# 但我想要只进行循环指定的行呢，该如何做
for line in f(1,3):
    print(line.strip())
    # 这样为何不行？
    # 原因在于调用的主体变为了print函数，其返回值时none
    # print(line).strip()
