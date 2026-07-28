# 4.1
# 列表：能装东西的东西
# python中用[]来表示列表，列表中的元素采用，隔开
# 同时我还可以放列表,甚至放基本上任何内容
# a = ["张三丰","张无忌","天下第一",[1,2,3]]
# 特性:
#   1.和字符串一样也有索引和切片
#   2.列表的索引如果超出范围会报错,同理字符串也是
#   3.可以使用for循环遍历
#   4.还可以用len拿到列表的长度
# list = ["张三丰","张无忌","天下第一"]
# print(list[0])
# print(list[1])
# print(list[2])
# 取多个
# 此取了都二个和第三个
# print(list[1:3])
# print(list[0:2])
# 倒着输出
# print(list[::-1])
# 列表list超出了其索引为的范围:list index out of range
# print(list[20])
# for i in list:
#     print(i)
# 还可以用len拿到列表的长度
# print(len(list))

# 4.2
# 列表的增删改查是最重要的操作
lst = []
# 向列表中添加内容
# 注意这是追加,是从末尾追加
lst.append("你好")
lst.append("垂杨")
lst.append("磨损")
lst.append("落幕")

# .insert()插入.但这种效率低,你每次插入,其后续的位置均需要调整
lst.insert(0,"天涯")
# .extend():可以合并两个列表,批量添加数据,自动追加到末尾
lst.extend(["卡神","陌生","妙可"])
print(lst)

# 删除操作,你想删除谁,得需要知道它的位置,
# 这意味着,你首先需要通过某种函数,去测试到要删除的元素是否存在,存在的话,那在哪?
# 第三个被删除,pop是有返回值的
# 也可以存储到一个字符串中
# print(lst.pop(3))
# ret = lst.pop(3)
# print(ret)
# print(lst)

# remove也是删除,不过是直接删除其中的元素,如果列表中没有,则会报错
# 如下
# lst.remove(3)
# lst.remove("你好")
# print(lst)

# 修改元素,或者也可以说是替换
# 落幕被改变
# lst[4] = "阿七"
# print(lst)

# 查询:直接使用索引进行查询
# print(lst[0])
# print(lst[1])