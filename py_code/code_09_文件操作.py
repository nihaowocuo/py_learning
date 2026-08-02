import os
import time
# os是操作系统模块的导入
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
# f = open("名单.txt",mode="w",encoding="utf-8")
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
# f = open("test.txt",mode="a",encoding="utf-8")
# f.write("我来也")

# with模式
# 打开文件后会自动关闭
# 此为常用
# with open("文本测试.txt",mode="r",encoding="utf-8") as f: # 此前常用f = open，现在相当反转了。as的含义和这个差不多
#     # :下要进行缩进
#     for line in f:
#         print(line.strip())

# 在此前，我们使用f打开时
# 可以直接用f.read()方法等
# 但是用with打开后，其运行完就会关闭，因此是无法进行后续操作的，因为文件已经被关闭了

# 那我想读取图片该如何读取：
# 注意在读写非文本文件时，要使用rb模式：其代表读取的是非文本文件，读取的是bytes
# with open("../tou.png",mode="rb") as f:
#     for line in f:
#         print(line)

# 我想完成文件的复制该如何操作，
# 从源文件中读取内容，写入到新文件中去
# with open("../tou.png",mode="rb") as f1,
# with open("../tou.png", mode="rb") as f1, \
    # 为何我进行换行便出错了？，因为常规来说f1的后面为:但是此时为,号
    # 那我们该如何做呢，文件太长了又不好看
    # 可是为何此时仍然会继续报错
    # 这是因为\后需要跟内容的不能跟空行
    # 而我们现在写的注释就相当于了空行，因此会报错

    # 接下来我将复制修改位置
    # 这样就不会报错了
    # 但现在出了新问题
    # [Errno 2] No such file or directory: '../tou.png'
    # with open("../tou.png", mode="rb") as f1, \
    # 经检测并非缩进问题
    # 原因在于，目录问题
    # 相对路径的查询是从你当下工作目录的根目录开始查询
    # 仅对的代码进行了低级的复制粘贴，并不清楚其具体作用，比如写入文件时wb，而我一股脑地复制了rb的模式
    # 这是我所犯的低级错误，
    # open("py_code/头像.png",mode="rb") as f2:
    # 可是现在依旧报错，是什么原因
# with open("tou.png", mode="rb") as f1, \
#     open("头像.png",mode="wb") as f2:
#     for line in f1:
#         f2.write(line)

# 此为测试异目录复制
# ./表示当前的工作目录
# 此为错误的../为上一层工作目录.每加一个.代表更上一级目录
# 正确的为../../为上两层，也就是说还需要加/表示进入该目录
# py中以三个点开头的文件名/目录名
# 哪进入下级目录呢？
# ./当前目录下要进入的下级目录名字/再下级的/再下级的
# with open("../tou.png", mode="rb") as f1, \
#     open("./头像3.png",mode="wb") as f2:
#     for line in f1:
#         f2.write(line)

# 4.5文件修改
#     1.从源文件中读取
#     2.从内存中修改
#     3.把修改后的内容写入到新文件
#     4.把源文件删除，新文件重命名
# 从源文件中读取内容，然后程序进行相应的操作修改
# 然后再把修改后的文件再写入到新的文件中
# 新的文件再对源文件进行覆盖
# 例如源文件叫source，新文件叫new
# 我进行操作后，读取source的内容，然后进行修改操作，再把需要的文件内容写入到new文件中
# 删除source文件
# 最后再把new改名为source
# 这就是文件操作的实质
# 例如我想把文件中的姓张的改为姓周的

# 此报错为没进行文件后缀
# with open("名单",mode="r",encoding="utf-8") as f1, \
#      open("名单_副本",mode="w",encoding="utf-8") as f2:
# 但是当前有一个bug，此程序只是将所有的姓张的中，其内所有的名字都进行了修改
# 比如有人叫张需张，则会将后续的名字也改为周
# with open("名单.txt",mode="r",encoding="utf-8") as f1, \
#      open("名单_副本.txt",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         line = line.strip() # 去换行
#         # 出现问题，并未进行修改成功
#         # 原因在于字符串不可变，以下方法操作后实际上是生成了新的字符串
#         # 原字符串并未进行修改
#         # 因此如果需要修改则需要下一步重新赋值
#         if  line.startswith("张"):
#             # line.replace("张","周") # 修改
#             line = line.replace("张","周") # 修改后的正确
#         f2.write(line)
#         f2.write("\n")

# 我加入了张旭张进行测试
# 可见程序运行后变成了周旭周
# with open("名单.txt",mode="r",encoding="utf-8") as f1, \
#      open("名单_副本.txt",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         line = line.strip() # 去换行
#         # 出现问题，并未进行修改成功
#         # 原因在于字符串不可变，以下方法操作后实际上是生成了新的字符串
#         # 原字符串并未进行修改
#         # 因此如果需要修改则需要下一步重新赋值
#         # if  line.startswith("张"):
#         #     # line.replace("张","周") # 修改
#         #     line = line.replace("张","周") # 修改后的正确
#         f2.write(line)
#         f2.write("\n")

# 接下来我们已经把需要修改后的成果写入到了新文件中
# 接下来我们需要删除源文件，然后将新文件改名成源文件的名字

# 首先若要删除文件，再py中需要先进行导包
# import os

# 删除源文件
# time.sleep(3) # 让程序休眠3秒
# os.remove("名单.txt")
# # 把副本文件重命名为源文件名字
# # 可以查看到此文件已被进行修改
# # 名单_2与名单_副本2为源文件与修改文件的备份
# time.sleep(3)
# # 但是的上文件管理系统去看/pycharm中有延迟，因此无法进行
# os.rename("名单_副本.txt","名单.txt")
# # 可是我们该如何看到呢
# 则需要导入时间模块
# import time
# 能看到被删除了，但是跳出报错，原因在于我的名单_副本.txt文件已经不存在了
# 我把此前的给注释掉了
# 让我们再次测试
# 能明显看到名单被删除后，
# 名单_副本.txt被重命名为名单.txt