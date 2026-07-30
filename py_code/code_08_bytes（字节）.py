# # 1.字符集和编码：
# #     电脑是通过二进制存储信息
# #     通过ASCII码来表示信息
# #     标准ASCII码为7位，首位为0
# #     中国编码gbk，今天仍在用，其有存储空间占用小的特点，这也是其依旧未被utf-8完全取代的因素之一
# #     1B（byte） = 8b（比特）
# #       Unicode:万国码，国际通用编码，但存储是一个问题，后续即使经过了扩充，
# #       ASCII码已经常用，很难进一步修改
#
# #       Utf：可变长度的unicode
# #         utf-8：表示最短的字节长度为8
#         # 英文1个字节，欧洲文字2个字节，中文3个字节
#         # utf-16：表示最短的字节长度为16
#
# # 2.bytes
#
# s = "垂杨"
# # 我将此字符串真正存储为gbk或者utf-8是什么状态
# # 此为对文字进行编码
# # bs1 = s.encode("gbk")
# # print(bs1)
# # 转为utf-8呢?
# # 共6个字节,一个字符3个字节
# # bs2 = s.encode("utf-8")
# # print(bs2)
# # b'\xb4\xb9\xd1\xee':此为bytes类型的，每一个\都是代表一个字节
# # 共4个字节
# # print(type(bs1))
# # print(type(bs2))
#
# # 能明显察觉到gbk与utf-8的不同
# # 那我该如何转化呢
# bs3 = b'\xb4\xb9\xd1\xee'
# # 先变成字符串
# # 此为解码
# s1 = bs3.decode("gbk")
# # 将字符串s1再转为utf-8类
# bs4 = s1.encode("utf-8")
# print(bs4)
# # 解码后输出没问题
# print(s1)
#
# # 1.str.encode("编码类型") 进行编码
# # 2.bytes.decode("编码类型") 进行解码
#
# s2 = "你好啊,垂杨,abc"
# # 英文符合ASCII码的标准符合因此可以正常显示
# print(s2.encode("gbk"))
# print(s2.encode("utf-8"))