# 演示：装饰器里全局变量 login_flag 的作用
# 目的 = 让登录状态(a)跨函数调用持久存在 (b)被多个 inner 共享

print("=== 1. 不加 global：赋值只建局部变量，状态没保存 ===")
login_flag = False  # 模块级

def bad_inner():
    login_flag = True   # 没有 global -> 这里是新建一个【局部】变量，模块级的不动
    print("  bad_inner 内看到的 login_flag =", login_flag, "(这是局部副本)")

bad_inner()
print("  bad_inner 返回后，模块级 login_flag =", login_flag, "(仍是 False -> 状态没保存)\n")


print("=== 2. 加 global：改的是模块级变量，状态被保存 ===")
def good_inner():
    global login_flag
    login_flag = True

good_inner()
print("  good_inner 返回后，模块级 login_flag =", login_flag, "(变成 True -> 状态保存)\n")


print("=== 3. 用 global 后，两个装饰函数共享同一状态 ===")
login_flag = False

def login_verify(fn):
    def inner(*a, **k):
        global login_flag
        if login_flag == False:
            print("  [门卫] 需要登录 -> 验证通过，置 True")
            login_flag = True
        else:
            print("  [门卫] 已登录，直接放行")
        return fn(*a, **k)
    return inner

@login_verify
def a(): print("  执行 A")
@login_verify
def b(): print("  执行 B")

a()   # 第一次：走登录
b()   # 第二次：共享同一全局，已登录直接放行
