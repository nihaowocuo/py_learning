# 登录验证装饰器演示（用队列模拟 input，避免交互阻塞）
login_flag = False  # 登录态标记：False=未登录，True=已登录

# 模拟用户在 input() 里的输入：前两次故意输错，第三次正确
_inputs = iter(["wrong", "000000", "admin", "123456"])
def fake_input(prompt):
    val = next(_inputs)
    print(prompt + val)        # 把"用户输入"打印出来，便于观察
    return val

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag       # 声明要改的是模块级全局，不是新建局部
        if login_flag == False:  # 外层 if：会话还没登录才弹框
            print("[门卫] 尚未登录，需要验证")
            while True:          # 内层 while：单次凭证对错，输错才重试
                username = fake_input(">>>")
                password = fake_input(">>>")
                if username == "admin" and password == "123456":
                    print("登陆成功")
                    login_flag = True   # 登录成功 -> 写入全局状态
                    break
                else:
                    print("登陆失败，用户名或者密码错误，请重试")
        else:
            print("[门卫] 已登录，直接放行")
        ret = fn(*args, **kwargs)  # 放行后执行真正的业务函数
        return ret
    return inner

@login_verify
def add():    print("添加员工信息")
@login_verify
def delete(): print("删除员工信息")
@login_verify
def update(): print("修改员工信息")
@login_verify
def search(): print("查询员工信息")

print("=== 第一次调用 add（应弹登录框，含一次输错重试）===")
add()
print("\n=== 第二次调用 delete（应直接放行）===")
delete()
print("\n=== 第三次调用 update（应直接放行）===")
update()
print("\n=== 第四次调用 search（应直接放行）===")
search()
