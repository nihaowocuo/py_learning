# 函数的嵌套，内部在定义函数
# 变量的作用域
# 闭包
# 装饰器
"""
装饰器通用写法：
wrapper:装饰器，fn:目标函数
def wrapper(fn):
    def inner(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return inner

@wrapper
def taget():
    pass

target() 其所指向的为inner
注意：一个函数可以被多个装饰器装饰
@wrapper1 # target = wrapper(target) target / wrapper2.inner => wrapper1.inner
@wrapper2 # target = wrapper(target) target => wrapper2.inner
def target():
    print("我是目标函数")
规则：wrapper1 wrapper2 target wrapper2 wrapper1
"""
from sqlalchemy import false

# 迭代器
# 生成器
# 推导式
# 匿名函数
# py内置函数_下 sorted,filter,map

# 作用域：变量访问的权限
    # 全局变量
    # a = 10
    # # 我们顶格所写的函数也可以被认为时全局的函数，如果在其内部在生成一个函数，则此函数为局部函数
    # # 但如果我想要在函数外面访问此函数内部定义的数据呢
    # # 只能通过用
    # def fun(*args):
    # # b为局部变量
    #     b = 10
    #     # a作为全局变量，是否可以被函数内所调用的
    #     print(a)
    #     print(b)
    #     for x in args:
    #         print(x)
    #
    # print(a)
    # # 由于b为函数内创建的，为局部变量，因此是无法被外部所引用的
    # print(b)

    # 与作用域相关的关键字
    # global
    # a = 10
    # # print(a)
    # def fun1():
    #     # 这是在函数内部创建一个新的a
    #     # a = 20
    #     # 但如果我就想在函数内部更改外部的全局变量
    #     # 那就需要global
    #     # 这是将外部的全局变量引入到函数内部
    #     global a
    #     a = 20
    #     # return a
    #
    # # 注意：只有调用函数时函数内的设置才生效
    # # 比如此处如果我不进行函数调用，则此处打印的就是a = 10
    # # 而当我进行函数调用时，其内部操作才进行了修改
    # # fun1()
    # print(a)
    # # 此处可以看到a被改为了20
    # # print(fun1())

    # nonlocal
    # # 那如果我想要在嵌套的内部函数中去更改外层的函数的所赋值的变量呢
    # # 则采用nonlocal关键字，其表示向外找一层是否有该变量
    # # 若外层有则引入，若没有则继续向外层函数寻找
    # # 但如果外层是全局，则无法引入，需要使用global关键字
    #
    # a = 10
    # def fun1():
    #     a = 10
    #     def fun2():
    #         a = 20
    #
    # fun1()


# 函数可以嵌套函数，注意嵌套不是调用
    # 1.函数可以作为返回值返回
    # 2.函数可以作为参数相互传递
    # 函数名实际也是一个变量名，本质上都表示了一个内存地址
    # 是可以直接打印变量名或者函数名进行查看
    # def fun(*args):
    #     def fun2(*args):
    #         pass
    #     a = fun2()
    #     print(a)
    # 此处报错，是因为这是被嵌套的局部的函数，
    # 和局部变量一样无法被正常的访问
    # 但同样的一般被定义在函数内的变量
    # 都是在函数内使用的
    # print(fun2())

    # 但如果我想在外部使用
    # def fun():
    #     a = 10
    #     return a
    # # 既然能够返回值，那我能否返回函数
    # a = fun()
    # print(a)

    # def fun():
    #     def fun2():
    #         print(123)
    #     #     function表示函数的意思，local表示的是局部作用域内的所有东西，把.当作成的意思
    #     #     后面的0x是16进制其存储的位置<function fun.<locals>.fun2 at 0x0000023C5BB939C0>
    #     print(fun2)
    #     return fun2
    # # 此处相当于b1被赋值成了函数
    # # 也就是说b1也成了函数
    # b1 = fun()
    # # 函数可以被赋值，可以被返回
    # # 打印的结果和fun2一致，意味着把函数暴露在了外界
    # print(b1)
    # print(b1())

    # 你可以传变量给函数，也可以传函数
    # 但是函数呢？
    # 注意当你函数内没写return时，其会默认返回none
    # def fun1(an):
    #     print(an)
    # def fun2():
    #     # print("hello")
    #     def fun3():
    #         pass
    #     return fun3
    # # 此传的是函数
    # # 而fun1打印出的正是fun2函数所存储的地址位置
    # fun1(fun2)
    # # 此传的是fun2()函数调用后的返回值
    # # 此结果是输出fun2的返回值hello
    # # fun1(fun2())
    # # 此处我将返回值改为了函数
    # fun1(fun2())

# 闭包：内层函数对外层函数的局部变量使用，此时内层函数被称为闭包函数
# 1.可以让一个变量常驻于内存（效果：
# 2.我可以达成在修改局部变量时，避免全局变量未被修改
# 相当于时增加了安全性，其实质就是封装

    # def func():
    #     a = 10
    #     # 此种就构成了闭包函数
    #     # 此处的变量a就是被常驻于内存的变量
    #     def inner():
    #         nonlocal a
    #         a += 1
    #         # print(a)
    #         return a
    #     return inner
    #
    # # 此返回的是函数
    # # 但此处你的inner你是不确定其什么时候执行的
    # # 注意此处result1为函数
    # result1 = func()
    # # 此为打印result的类型
    # # print(type(result1))
    # # 打印此函数的内存地址
    # print(result1)
    # # 而此处的r1便是接收result函数的返回值
    # r1 = result1()
    # # 打印r1的值
    # print(r1)
    # # 再次调用函数，看其内部的a变量是否是被重置，还是说被临时保存下来
    # r2 = result1()
    # # 可以看到此处打印的是12，说明上一次的函数执行后的a的结果未被重置
    # # 此后的结果均出现累加
    # print(r2)
    # r3 = result1()
    # print(r3)
    # r4 = result1()
    # print(r4)
    # # 以此达成了操作
    # # 在全局中使用了局部变量
    # # 优势：局部变量不容易被修改
    # # 我才用闭包的形式间接的对局部变量进行修改了
    # # 但如果我不通过闭包？、

# 注意：函数的变量名字是可以和局部变量全局变量一致的，
# 但是函数的名和变量的名，谁在后面，变会覆盖前者所指向的类型
# py中是共享命名空间的命名
# 例如：
# 此时两者正常
    # def greet():
    #     print('hello world')
    # print(type(greet))
    # greet = 20
    # print(type(greet))
# 但当我去调用此greet函数时呢？
    # def greet():
    #         print('hello world')
    # print(type(greet))
    # greet = 20
    # print(type(greet))
    # # 此时便会报错为，greet为int类型，而非函数类型无法被调用
    # # TypeError: 'int' object is not callable
    # # 这便可以证明后者的greet把前者的函数greet给覆盖掉了
    # greet()

# 内容回顾：
#     1.函数可以作为参数被传递
        # def fun():
        #     #     print("我是函数")
        #     #
        #     # def fun1(fn):
        #     #     # 此时其形参接收的就是一个函数名
        #     #     # 同时被命名fn的函数
        #     #     # 此处加了()便意味着被调用了
        #     #     # 可以看到输出结果
        #     #     fn()
        #     # # 此处便是我把函数传入过去，
        #     # fun1(fun)
#     2.函数可以作为返回值被返回
#     3.函数名称可以和变量一样进行赋值操作
        # def fun2():
        #     print("我是函数2")
        # def fun3():
        #     print("我是函数3")
        #
        # fun2 = fun3
        # # 此处调用函数打印的却是函数3
        # fun2()

                    # 此为突发奇想
                        # import sys
                        # x = "你好啊"
                        # y = 18
                        # print(sys.getsizeof(42))    # 28 字节
                        # print(sys.getsizeof(x))    # 64 字节
                        # print(sys.getsizeof(y))    # 28 字节
                        # # 现在我想知道为何在c中,整数之占4个字节，为何在py中会占28个字节？
                        # # 两者为何差别这么大
                        # # int c = 12

# 装饰器：本质上是一个闭包（内层函数对外层函数的变量做一个引用）
    # 作用：在不改变原有函数（不改变源代码）调用下，给函数添加新的功能，
    # 可以在函数的前后添加额外的功能
    # 范围使用，例如写个员工管理系统，增删改查，
    # 你要修改的前提，就要先登陆账号
    # 还有日志，
    # 实际的应用雏形
        # def wrapper(fn): # wrapper是装饰器，fn为目标函数
        #     def inner():
        #         # 在目标函数执行之前执行什么操作，如登陆验证
        #         fn() #执行目标函数
        #         # 在目标函数中执行后干什么，如记录日志，或者关闭数据库链接
        #     return inner

# def guanjia(game):
#     # 在此处可以看到内层函数inner使用了外层函数局部变量game，只不过此变量比较特殊为函数
#     def inner():
#         print("打开外挂")
#         game()
#         print("关闭外挂")
#     return inner
# # 此处为验证函数功能性
# @guanjia
# def play_dnf():
#     print("来吧勇士们")
# @guanjia
# def play_lol():
#     print("我要打联盟")
#
# # 此为验证功能性函数
# # play_dnf()
# # play_lol()
#
# # 但这样是否太过麻烦
# # play_dnf = guanjia(play_dnf) # 管家重新封装了游戏，并且在其外层函数内加入了部分打开外挂，关闭外挂等操作
# play_dnf() # 此时运行的便已经是管家给的内层函数inner，是已经被修改过的
# # play_lol = guanjia(play_lol) # 让管家重新封装lol
# play_lol()
# # 于是我们有新方法，在你原有的函数上，加入@函数名（guanjia)
# # 在函数上加入@guanjia，或其他的函数名，这就是告诉管家这个函数你要对此功能函数进行重新封装
# # 尝试运行后无错


# def guanjia(game):
#     # 在此处可以看到内层函数inner使用了外层函数局部变量game，只不过此变量比较特殊为函数
#     # 动态参数
#     # 此处的*，**表示接收所有的参数，打包成元组和字典
#     def inner(*args,**kwargs):
#         print("打开外挂")
#         # 此处的*把args的元组打散成位置参数和kwargs字典打散成关键字参数再传入，后者同理
#         # 此处调用参数是已经被定义了，在inner接收到是就已经定义
#         game(*args,**kwargs) #游戏中
#         print("关闭外挂")
#     return inner
# 你如果要理解这个闭包，
# play_dnf = guanjia(play_dnf)
# 首先先弄清楚你传入了什么
# 然后你返回了什么
# 例如此处中，我传入了username与password
# 然后其返回值为inner，这是一个函数名，是在guanjia内部定义的一个局部函数
# 然后再把inner这个赋值给play_dnf
# 然后play_dnf()进行调用，此处就相当于inner()
# 而inner函数正是管家内部的那个局部函数
# 进一步拆解inner，又发现，其内部又调用了一个函数，是game()
# 那这个game是什么，其是guanjia(传入函数)，该函数名赋值给了game
# 而调用game()就是传入函数()的调用
# 其具体的执行流程就是
# def guanjia(game):
#     def inner(*args,**kwargs):
#         print("打开外挂")
#         game(*args,**kwargs) #游戏中
#         print("关闭外挂")
#     return inner
# play_dnf = guanjia(play_dnf)
# 由于此为赋值运算
# 因此先从右侧进行执行
# 1.先调用guanjia()把play_dnf的函数名传入进去
# 此时game = play_dnf
# 2.然后是定义的inner局部函数，此时未被调用
# 继续下一步
# 3.返回值，把inner这个函数名作为返回值返回
# 此时play_dnf = guanjia(play_dnf)
# 也就是 play_dnf = inner
# 也就是说在inner未被调用时，inner内部的game是未被执行过的
# 4.play_dnf("admin,"123456") # 此时进行了函数调用即为inner的调用
# 首先，两个实参被传入到此方法中：def inner(*args,**kwargs):
# 然后下一步执行game()，注意game实际上是play_dnf原函数
# 由于原函数是需要两个参数值的
# 所以此处的game也需要取用参数
# 而这一步的调用传参play_dnf("admin,"123456")
# 是传给了inner
# 而game引用的参数便是inner中的
# 即play_dnf(username,password)传入的参数，game(*args,**kwargs)
# 然后调用原函数play_dnf()
# 进行操作后结束


# 我要玩游戏是否需要账号和密码
# 这时就是需要传数据
# 注意此时play_dnf传过去的不只是函数名，而且还有其所携带的参数（形参）
# @guanjia # play_dnf = guanjia(play_dnf)
# def play_dnf(username,password):
#     print("来吧勇士们",username,password)
#
# @guanjia
# def play_lol(username,password,hero):
#     print("我要打联盟")
#     print("开始游戏",username,password)
# 此时程序仍能够正常运行，但是当我使用嵌套的呢
# play_dnf("admin","123456")

# 出现报错
# guanjia.<locals>.inner() takes 0 positional arguments but 2 were given
# 当没有管家是，我是直接调用的play_dnf函数
# 而当管家上来后，由于管家重新封装了
# 你实际上调用的是inner这个函数
# 而inner这个函数本身是没有参数的
# 那我如果给inner加上传参的参数呢
# 但仍然报错，play_dnf缺失了所需的两个参数
# play_dnf() missing 2 required positional arguments: 'username' and 'password'
# 此时，我都放入参数后，才可正常运行
# play_dnf("admin","123456") # 此时运行的便已经是管家给的内层函数inner，是已经被修改过的

# 此时再度报错，表示inner只接受两个参数，但你传入了3个
# guanjia.<locals>.inner() takes 2 positional arguments but 3 were given
# 此时我们得考虑，谁能接收各种各样的参数，而不进行挑呢
# 那就是*args：所有的位置参数，元组,与**kwargs所有的关键字参数


# 装饰器返回值问题
# def guanjia(game):
#     def inner(*args,**kwargs):
#         print("打开外挂")
#         # 此处是game函数，其实际上也有返回值的，咱们可以打印
#         # play_lol的返回值被接收后，再次返回到最初调用的函数那
#         ret = game(*args,**kwargs) #游戏中 #
#         print("关闭外挂")
#         return ret
#     return inner
#
# @guanjia # play_dnf = guanjia(play_dnf)
# def play_dnf(username,password):
#     print("来吧勇士们",username,password)
#
# @guanjia
# def play_lol(username,password,hero):
#     print("我要打联盟")
#     print("开始游戏",username,password,hero)
#     return "诺克萨斯即将崛起"
#
# # 而由于我们未给play_lol设置返回值，所以其返回的是none
# ret = play_lol("admin","123456","诺克")
#
# # 可以看出此时可以打印出诺克萨斯即将崛起
# print(ret)

# 注意：一个函数可以被多个装饰器装饰
# def wrapper1(fn):
#     def inner(*args, **kwargs):
#         print("此为wrapper1进入")
#         ret = fn(*args, **kwargs)
#         print("此为wrapper1出去")
#         return ret
#     return inner
#
# def wrapper2(fn):
#     def inner(*args, **kwargs):
#         print("此为wrapper2进入")
#         ret = fn(*args, **kwargs)
#         print("此为wrapper2出去")
#         return ret
#     return inner
#
# # 若我采用此种呢
# # 分析，首先@wrapper2先套入的
# # 此时
# @wrapper1 # target = wrapper1(target) target / wrapper2.inner => wrapper1.inner
# @wrapper2 # target = wrapper2(target) target => wrapper2.inner
# def target():
#     print("我是目标函数")
#
# # 调用验证
# # 分析，谁距离目标函数近，谁先包裹的，
# # 首先target => wrapper2.inner
# # 然后wrapper2.inner => wrapper1.inner
# # 通俗来讲
# # 就是wrapper2传入target函数，然后返回inner函数名
# # target被重新赋值为wrapper2.inner
# # 然后再次执行嵌套
# # target再次被wrapper1调用传入，然后返回inner
# # target被重新赋值为wrapper1.inner
# # 然后开始函数的执行
# # target()执行，也就是wrapper1.inner()这个执行
# # 先输出这个 print("此为wrapper1进入")
# # 然后进入这一步 ret = fn(*args, **kwargs)
# # 此为调用的当前target上一层嵌套的函数
# # 也就是说wrapper.2inner()
# # 开始执行 print("此为wrapper2进入")
# # 然后又出现这一项，ret = fn(*args, **kwargs)
# # 此时又进一步向前调用嵌套的函数，此为target最初的函数
# # 输出这个然后    print("我是目标函数")
# # 再输出这个 print("此为wrapper2出去")
# # 执行return ret 返回到wrapper1
# # ret = fn(*args, **kwargs)
# # 执行这个 print("此为wrapper1出去")
# # 然后返回这个，但由于没设置接收的变量，所以无法查看return ret
# # 此时我进行设置
# ret = target()
# # 你会发现其打印的时none,原因在于你未设置返回值
# # 因此返回默认的none
# print(ret)
# target()


# 装饰器实战
# 写一个员工管理系统
# 对登录的账号进行验证
login_flag = False


def login_verify(fn):
    def inner(*args, **kwargs):
        # 在此处进行登录验证
        global login_flag
        # 此为当正确时才执行，但实际的登录原理，不该是，登录失败才再次进行操作吗
        # 所以我们进行修改为False
        if login_flag == False:
            print("还为完成登录操作")
            while True:
                username = input(">>>")
                password = input(">>>")
                if username == "admin" and password == "123456":
                    print("登陆成功")
                    # 而由于其为全局变量，所以我得需要进行引入
                    # 此为登陆成功时记录状态
                    # 无需进行下此验证
                    login_flag = True
                    break
                else:
                    print("登陆失败，用户名或者密码错误")
        ret = fn(*args, **kwargs) # 后续的具体功能函数
        return ret
    return inner



# 此为具体的功能函数
# 而在执行之前我们是否先需要一个管理员的账户登录
@login_verify
def add():
    print("添加员工信息")

@login_verify
def delete():
    print("删除员工信息")

@login_verify
def update():
    print("修改员工信息")

@login_verify
def search():
    print("查询员工信息")

# 先执行新增进行验证

add()
# 当我每次执行时都需要再重新登录
# 那我该如何在登陆成功之后，能否留下一个登录成功的状态
# 让我不再需要重复的验证
delete()
update()
search()