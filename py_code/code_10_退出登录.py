# 退出登录：把全局登录态重置为 False
login_flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag == False:
            print("[门卫] 尚未登录，需要验证")
            # 模拟一次正确登录（真实场景用 input 读取）
            username, password = "admin", "123456"
            if username == "admin" and password == "123456":
                print("登陆成功")
                login_flag = True
            else:
                print("登陆失败")
                return
        ret = fn(*args, **kwargs)
        return ret
    return inner

def logout():
    global login_flag          # 同样需要 global，才能改到模块级变量
    if login_flag:
        login_flag = False     # 关键：重置为 False
        print("已退出登录，登录态已清除")
    else:
        print("当前本就处于未登录状态")

@login_verify
def add(): print("添加员工信息")
@login_verify
def delete(): print("删除员工信息")

print("--- 第1次 add：会要求登录 ---")
add()
print("--- 此时 delete：已登录，直接放行 ---")
delete()
print("--- 执行 logout：重置为 False ---")
logout()
print("--- 再调 add：login_flag 又变 False，重新要求登录 ---")
add()
