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

#     mode：
#         r：read,readline(),line.strip()
#         w
# 读写文本时，需要给encoding
# 图片无法
# f = open("文本测试.txt",mode="r",encoding="utf-8")
# content = f.read()
# 读取成功
# print(content)

# 但此文件较小所以可以直接全读出来
# 那以后文件大了呢，或者我想要只读一部分呢？

# f = open("文本测试.txt",mode="r",encoding="utf-8")
# # 一行一行的阅读
# # line = f.readline()
# # 叠加使用，读取后然后去除字符串两侧的空白符
# # 此次打印可以看出未占据两行
# # 原因在于strip()去除了空白符（包含了换行符）
#
# # 最重要的文本读取方式
# # f我可以直接循环
# # 直接全部循环出来了
# # 但我想要只进行循环指定的行呢，该如何做
# # 从f中读取到每一行数据
# for line in f:
#     print(line.strip())
    # 这样为何不行？
    # 原因在于调用的主体变为了print函数，其返回值时none
    # print(line).strip()

# # 写入文件：
# # w模式下，若文件不存在，则会进行创建
# f = open("文本测试_写入.txt",mode="w",encoding="utf-8")
# # 若文件存在，每一次open都会清空文件的内容
# f.write("你好啊，世界")
# # 注意每次open后，要及时关闭链接
# f.close()

# 案例1：
# 准备一个列表，要求把列表中的每一项内容，写入到文件中
# lst = ["张无忌","周芷若","郭靖","赵敏"]
# f = open("test_09.txt",mode="w",encoding="utf-8")
# f.write(lst[0])
# f.write(lst[1])
# f.write(lst[2])
# f.write(lst[3])
# f.close()
# 但是我想让其能够分段显示
# 则我们可以写入换行符
# f.write(lst[0])
# f.write("\n")
# f.write(lst[1])
# f.write("\n")
# f.write(lst[2])
# f.write("\n")
# f.write(lst[3])
# f.close()
# f = open("test_09.txt",mode="r",encoding="utf-8")
# print(f.read())
# f.close()

# 我们也可以进行循环写入
# lst = ["张无忌","周芷若","郭靖","赵敏"]
# # 注意打开文件写入到外层中
# f = open("test_09.txt" ,mode="w",encoding="utf-8")
# for item in lst:
#     # 若这样的话则会出现每次写入都要打开一次此文件，
#     # 然而每次打开此文件都会删除
#     # 因此会导致只能写入最后一个
#     # f = open("test_09.txt", mode="w", encoding="utf-8")
#     f.write(item)
#     f.write("\n")

# a模式：
# 不会把原来的数据删除，而是追加的效果
# 运行两次后可以查看到具体效果
f = open("test.txt",mode="a",encoding="utf-8")
f.write("我来也")
