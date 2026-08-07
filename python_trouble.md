# python_trouble

**提问时间**：2026-07-12

**问题**：
如何检测自身电脑是否已经安装了 Python 与 Python 解释器，同时查找已安装的位置？

---

**提问时间**：2026-07-12

**问题**：
为何 D 盘与 C 盘均有 Python，且 Python 解释器该如何查看是否已经安装？

---

**提问时间**：2026-07-12

**问题**：
python 解释器与 python 环境是什么关系，没有 python 解释器，是否也能写 python 代码，但是无法与运行测试

---

**提问时间**：2026-07-12

**问题**：
我是否需要将 py 下的 Scripts 加入到环境变量中吗？

---

**提问时间**：2026-07-12

**问题**：
为何我未曾在环境变量中看到 py 的存在？


6. 退出 Python 的指令不只有 `exit()` 吗？截图里输入 `quit` 也退出了，这是否是数据库用的 `quit` 指令也可以用在 Python 中？

7. Python 计算中无需进行数据类型转换，便可以自动转换吗？

8. 为什么 `print("当前剩余的钱：" + money)` 会报错 `TypeError: can only concatenate str (not "float") to str`？

9. `==` 可直接判断字符串是否相等，那其他类型的相等判断条件是什么（如数字、列表，以及 `==` 与 `is` 的区别）？

10. print 打印默认换行，该如何让其不换行？

11. Python 中没有 double 类型吗？

12. 切片 step 负数时为何取不到内容？我对 `str[2:14:-2]`、`str[0:12:-1]` 期望从左到右取却输出空，而 `str[0::-1]` 却能输出 'a'，原理是什么？

13. 切片是否必须 [start:end:step] 同号才能用？`[-1:-12:2]` 为空、改负后 `[-1:-12:-2]` 成功(右往左每2取最右)，那如何实现倒序同时每组取最左侧？

14. 负索引实际会被转成正数，所以 `[-1:-12:2]` 没法用？为什么负数会被转为正数？

15. 总结：负索引最终会转换成正索引才能使用，那是否也可以用正索引来实现？（切片系列收尾）

16. `str_6[15:4:-2]` 从右向左，必须搭配负数 step；若改正数 step 从左取，与原顺序冲突导致无法执行？

17. `print(str_6[2:-12:2])` 为何没返回空串，而是打印出 'c'？负 stop 不是代表右边吗，为何和正 step 不冲突？

18. 字符串 `capitalize()` 方法对中文有效吗？首字符是中文会怎样？

19. 验证码比较用 `user_input.upper() == verify_code.upper()` 是否有安全风险？既然统一转大写比较，为何生成的验证码还要混合大小写（如 "Xado"）？

20. 我故意用混合大小写验证码就是为了增加安全性，但 `.upper()` 比较让用户无需完全一致输入也能通过，这不就抵消了安全提升吗？

21. `money.isdight()` 报错 `AttributeError: 'str' object has no attribute 'isdight'. Did you mean: 'isdigit'?` 是什么原因？

22. 输入 `123.2` 后，`if money.isdecimal():` 判断失败，输出"对不起你输入的有误"，这是为什么？`isdecimal()` 难道不是用来判断小数的吗？

23. 输入 `money.isde()` 时 PyCharm 提示 `isdecimal()`，为什么叫"小数"？它和小数有什么关系？

24. `isdigit` 是什么？它和 `isdecimal` 有什么不同？

25. 能否将多个字符串像列表那样拼接起来？比如多个字符串连接成一个长字符串？

26. 多个字符串以独立变量形式（s / s1 / s2 / s3）存在时，能否用 `join()` 一起拼接？

27. `"_".join(s, s1, s2, s3)` 为何报错 `TypeError: str.join() takes exactly one argument (4 given)`？

# Q28 列表切片是否产生新列表（lst = [1,2,3], lst[1:3]）
问题：和字符串一样也有索引和切片，lst = [1,2,3]，我进行的切片 lst[1:3]，其并没有改变原列表，而是产生了一个新的列表？

# Q29 print(lst[1:3]) 输出的是新的列表吗？
问题：如果我进行 print(lst[1:3])，这是输出的什么新的列表吗？

# Q30 列表 append 字符串为何出现黄色提示
问题：py中的列表不是什么内容都可以装吗，为何我在一串数字后，加入字符串会出现黄色提示？

# Q31 print(切片) 中"新列表"如何展示、是否有临时存储
问题（承接 Q29）：print(切片) 输出的是切片瞬间生成的新列表的显示内容，那新列表是如何展示的？其是否有一个默认的东西临时存储了它，在运行关闭后便消失？

# Q32 栈是什么，堆又是什么
问题：print 输出的列表存储到调用栈中，栈是什么，堆又是什么？

# Q33 字典取单个 key / value 的方法
问题：print(list(dic.keys())) 是取出所有 key，那取单个呢？

# Q34 dict.items() 为何每次返回长度为 2 的元组
问题：for item in dic.items(): 每次生成一个元组存储从字典中拿出的数据，其打印的长度只有 2，这是默认规定的还是根据后面要遍历的类型进行临时修改的？

# Q35 嵌套字典为何报错
问题：截图中的嵌套字典写法为何报错？

# Q36 嵌套字典访问报错 KeyError: 'game'
问题：截图中的嵌套字典访问报错，这又是什么报错？

# Q37 为何一边循环一边删除字典会报错
问题：for key in dic: if key.startswith("魔"): print(key) 此删除会报错 dictionary changed size during iteration，那我该如何删除呢？

# Q38 open 函数带 encoding 参数出现黄色警告
问题：open("文本测试.txt","r",encoding="utf-8") 出现什么问题？

# Q39 open() 报 unexpected keyword argument 'endoding'
问题：open("文本测试.txt", mode="r", endoding="utf-8") 运行报错，这是什么意思？

# Q40 Python 变量为何可以重复使用
问题：py 中变量为何可以重复使用，有两个 line 且并未报错？

# Q41 为何不能在 print 函数外添加 strip 方法
问题：我为何不能再 print 函数外再添加 strip 方法？（print(line).strip() 报错）

# Q42 如何只循环文件中的指定行
问题：for line in f 会直接全部循环出来，但我想要只进行循环指定的行呢，该如何做？

# Q43 如何在 for line in f 基础上只循环指定行（f(1,3) 为何不行）
问题：在此基础上修改，同时告诉我，你给的方案都是什么，需要导入包？（用户尝试写 for line in f(1,3)）

# Q44 with 打开能读图片，f = open 打开的也能读吗
问题：with 的形式打开的文件能读取图片，那使用 f = open 打开的呢？

# Q45 如何跨文件/跨目录读取文件
问题：我想跨文件读取该如何操作？

# Q46 with 同时打开两个文件复制图片报错
问题：我想完成文件的复制，使用 with open("../tou.png", mode="rb") as f1, \ open("./py_code/头像.png", mode="rb") as f2: 报错 invalid syntax，是什么原因？

# Q47 复制图片时 FileNotFoundError: '../tou.png'
问题：语法修正后运行报 FileNotFoundError: [Errno 2] No such file or directory: '../tou.png'，是什么原因？

# Q48 直接运行脚本 open("tou.png") 仍报 FileNotFoundError
问题：改成 D:\py\python.exe E:\py_learning\py_code\code_09_文件操作.py 运行后，open("tou.png", mode="rb") 仍报 FileNotFoundError: 'tou.png'，为何？

# Q49 文件确实存在但 open 仍报 FileNotFoundError
问题：当前文件夹（E:\py_learning）下明明有 tou.png，命令行运行脚本后仍报 FileNotFoundError: 'tou.png'，为什么？

# Q50 相对路径基准点到底是什么？如何在 py_code 目录访问外层目录文件？
问题：你此前告诉我相对路径的起始点是 py_learning，现在又说是当前工作目录 py_code，请详细解释，并给出我能在当前目录下访问外层目录的文件内容的方法。

# Q51 是否必须把图片复制到 py_code 才能操作？
问题：还是说我只能把图片复制到当前目录下 py_code，然后在通过命令将其打开并复制到当前目录下的另一个文件内？

# Q52 能否在用户现有代码基础上修改？运行后 tou.png 为何被删除？
问题：我能否不用你所给的操作，而是在我的基础上进行指导我修改？同时，运行程序后我在 py_learning 下的 tou.png 文件自动删除了，是什么原因？

## Q53
原因是否是，我使用 `with open("tou.png", mode="rb") as f1` 读取了文件内容，又使用 `open("py_code/头像.png",mode="wb") as f2` 以 w 模式打开，要正确写入新文件，但因中途出现未知错误未正常写入，文件又被打开所以被清理删除了？

## Q54
（图）在当前目录下我成功地执行了操作，为何此前跨目录执行操作失败？

## Q55
（图）教程中的就可以正常操作

## Q56
（图）我该如何判断当前的根目录，进而能正确的使用./与../等操作

## Q57
（图）哪进入下级目录呢？

## Q58
从源文件读取内容→修改→写入新文件→覆盖源文件（删源、改名）。问：这是否为文件操作的实质，若不正确请修改。

## Q59
（图）为何报错：FileNotFoundError: [Errno 2] No such file or directory: '名单'

## Q60
4.5 文件修改四步法。问：Word 改一个字后保存，默认保存就是如此操作？另存为是源文件与新文件同时存在？

## Q61
（git 操作）本次问题：我不小心把提交的附录内容写错了，然后使用了回滚提交（git revert），发现不符合预期——我想要的是删除此次错误提交、重新提交一遍。于是我进行了所谓的“回滚的混合式”（git reset --mixed），结果出现文件消失的情况，回收站也无此文件。我先执行了 `git reset --mixed 1a5c03c` 发现无效果，又执行 `git checkout HEAD -- py_code/code_10_函数.py` 最终找回文件。问题起因：我想在提交附录中加入今天解决的“vscode 中文输入时中文无法正常显示（只显示英文字母，不显示中文）”这一问题的解决方案。

## Q62
运行 code_10_函数.py 报错：
TypeError: print() got an unexpected keyword argument 'hello'
代码：
func(1,2,3,4,hello=465,haha=654)
def func(a, b, c, *args, **kwargs):
    print(a, b, c, *args, **kwargs)


## Q63
（图）教程中 `def func(a, b, *args, c="哈哈", **kwargs): print(a, b, c, args, kwargs)` 加 `func(1,2,3,4, c="呵呵", hello=456, haha=654)` 能正常打印 1 2 呵呵 (3, 4) {'hello': 456, 'haha': 654}。问：为何教程能正常打印？


## Q64
运行 code_10_函数.py 报错：
TypeError: print() got an unexpected keyword argument 'haha'
代码：
func(1, 2, haha=654)
def func(a, b, c, *args, **kwargs):
    print(a, b, c, *args, **kwargs)


## Q65
（图）调用 `func(hello=456, haha=654, 1, 2, 3, 4)` 报 SyntaxError: positional argument follows keyword argument。请总结实参与形参的输入规律。
用户注释："此处第三位我传入实参为数字，系统提示应为str但实际为int"；"注意，此处的默认值要生效，意味着在位置参数 b 之后不能有任何数据，关键字可以，是已经被锁定了，关键字，强制会传入 **kwargs"。


## Q66
（图）`ord` 是否为提取字符的编码，而 `chr` 则是将编码转为字符？代码注释："在 py 内存中所使用的时 unicode 编码"；"汉字在其中是有编码的，可以通过 ord 取到此字的编码"；"给出编码位置，我将其变为汉字"；`print(chr(ord(a)))`。


## Q67
（图）VS Code 运行面板输出大量字符后，问：为何终端运行处没有搜寻（搜索）功能？


## Q68
（图）在 VS Code 终端中输入 `py code_10_函数` 运行，报 `can't open file '...\code_10_函数': [Errno 2] No such file or directory`。问：该如何运行？


## Q69
（图）运行 `for i in range(65536): print(chr(i)+" ", end="")` 后，终端只显示部分字符（ASCII 可见字符），后面大量空白/方块。问：为何未进行全部打印？
