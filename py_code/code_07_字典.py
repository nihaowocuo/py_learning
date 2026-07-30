# # 首先:字典是通过键值对来存储数据的,
# # 也就是说是一对,一对存的
# # 存储一个是键,一个是值
# # 字典的表示方式{key:value,key2:value,key3:value}采用的此方式
#
# # dic = {"卡":"卡卡","莫":"莫莫"}
# # 输出整个字典包含键值对
# # print(dic)
# # 在字典中[]相当于列表中的索引,访问此键,返回此值
# # print(dic["卡"])
# # val = dic["莫"]
# # print(val)
#
# # 但字典对键值的存储分别有不同的要求
# # 字典的key(键)必须是可哈希的,这意味着是不可变的类型数据
# # value(值)可以放入任何数据类型
#
# # 示例
# # unhashable type: 'list' 出现报错,不可哈希列表
# # dic = {[]:"灭"}
#
# # 4.2字典的增删改查:
# # 空字典
# # dic = {}
# # dic = dict()
# # # dic['a'] = 1
# # # dic['b'] = 2
# # # dic['c'] = 3
# # # print(dic)
# # # dic['d'] = 4
# # # print(dic)
# #
# # # 增加:1.直接增加.你的key1之前不能存在,否则会直接给你修改
#         采用默认setdefault,若key已经
# # dic[1] = "名字"
# # dic[2] = "年龄"
# # dic["你好"] = "卡罗"
# # # print(dic)
# # print(dic[1])
#
# # 修改：此时字典中1已经有了相应的值
# # 但你在进行此操作时，出现了覆盖，也就是修改了此位置的数据
# # dic[1] = "无言"
# # print(dic)
#
# # 此为设置默认值，比如这个键并未被设置过
# # dic.setdefault("tom","咔嚓") # 以前没有才会生效
# # print(dic)
# # dic.setdefault("tom","咪咪") # 如果有了就不会生效
#
# # 删除操作：根据键来删除
# # 就和列表类似，
# # dic.pop(1)
# # print(dic)
# # 第二种删除
# # 不常用
# # del dic[1]
#
# # 查询：
# # print(dic)
# # print(dic[1])
# # print(dic[2])
# # 也可以进行
# # print(dic.get(1))
#
# # 如果key不存在，则程序报错
# # print(dic['你好11111111']) # 当你确定你的key是没问题的，可以用
# # 如果key不存在，则程序不报错 # 当你不确定你key存在的时候
# # 此不报错，返回None
# # print(dic.get('你好222222'))
#
# # None,py中的关键字,单纯就是空表示没有的含义
# # print(type(None))
# # 例如,此为空字符串，你可以使用其他相关的字符串操作，如字符串添加等
# # s = ""
#
# # 例子：
# dic = {
#     "莫言" : "我来了",
#     "咔嚓" : "他来了",
#     "魔力" : "你来了"
# }
#
# str = input("请输入你要查找的内容：")
# # 注意：采取了此种赋值的方式，若用户输入的内容不存在，
# # 其会强制根据不存在查询，但由于我的为dic[]查询所以会拨错
# # val = dic[str]
# # 而这种方式不会报错
# val = dic.get(str)
#
# if str in dic:
#     print(val)
# else:
#     print("并无您要查询的信息！")

# 4.3字典的循环和嵌套
# dic = {
#     "莫言": "我来了",
#     "咔嚓" : "他来了",
#     "魔力" : "你来了"
# }
# 1.for循环拿key，进而拿值
# 我想要将字典的所有内容全部循环出来
# for key in dic:
    # 此处输出的就为键
    # print(key)
    # 通过键拿值
    # print(key,dic[key])

# 2.希望把所有key全部保存到一个列表
# for key in dic:
#     print(list(dic.keys()))
# 这是回取出所有的key，那取单个呢？
# 直接拿到所有的key
# print(dic.keys())
# 取单个，可以使用上方的循环

# 3.同理，你可以用同样的方式存储value
# 直接拿到所有的value
# print(list(dic.values()))

# 4.我想同时把键值对都拿到
# 这种太繁琐
# print(dic.items())
# 我们可以采用此种方式
# for item in dic.items():
#     print(item)
# 但我们还可以更简洁
# 即我想单独的拿到键值
# for item in dic.items():
#     # 每次生成一个元组进行存储从字典中拿出数据
#     # 其打印的长度只有2，
#     # 这是为什么？这是默认规定的还是，根据后面要遍历的类型进行临时修改的
#     # 得出结论items()这个方法的返回值就是一个事先规定的长度为2的元组
#         item中只有两项元素，一个键，一个值
#     # print(type(item))
#     # print(len(item))
#     # key = item[0]
#     # value = item[1]
#     # print(key, value)
#
    # 还能进一步简化
# a,b = (1,2) #元组或者列表均可以执行此操作，此操作被称为解构（解包）
#     # 元组中的值需要和前面的变量一一对应，若是超出则报错
# print(a)
# print(b)

# dic = {
#     "莫言": "我来了",
#     "咔嚓" : "他来了",
#     "魔力" : "你来了"
# }
#
# # for item in dic.items():
# # 前文中讲过，items()方法返回的是一个元组，只含有两个元素，
# # 因此a,b = (1,2)可以进行类似的操作
# # 将其加入循环中就是如此显示
# for key,value in dic.items():
#
#     # item也可以省略
#     # key, value = item
#     print(key, value)

# 字典的嵌套
# dic = {
#     "name": "垂杨",
#     "age": 18,
#     "sex": "男",
#     "hobby": {
#         "game" : {
#             "game_name1": "单机游戏",
#             "game_name2": "联机游戏"
#         },
#         "sport": ["跑步","拉单杠","拉伸"]
#     }
# }
#
# str = dic["hobby"]["game"]["game_name1"]
# print(str)

# 若要修改期内的内容，一般时需要拿出后进行修改
# 然后再重新赋值回去

# 7.4总结:
# 字典的循环删除
# 例如此处我想删除以魔为开头的
# dic = {
#     "莫言": "我来了",
#     "咔嚓" : "他来了",
#     "魔力" : "你来了",
#     "魔王" : "讨伐我"
# }
#
# # 以下的报错是你在循环此字典的过程中,并且进行删除此字典的操作
# # 但你循环其他的东西，是不会报错的
#
# # for key in dic:
# #     if key.startswith("魔"):
# #         print(key)
#         # 此删除会报错dictionary changed size during iteration
#         # 即字典在迭代和循环的时候改变了大小
#         # 那我该如何删除呢?
#         # dic.pop(key)
#
# # 可以和列表一样
# # 创建一个临时的列表
#
# temp = [] #存放及将要删除的key
# for key in dic:
#
#     if key.startswith("魔"):
#         # 如何确定,这是我要删除的?
#         # 所以需要加判断
#         temp.append(dic[key])
# for t in temp:
#     # 此时是循环列表,删除字典中的内容
#     dic.pop(t)
# print(dic)

