def guanjia(game):
    print("  [装饰阶段] guanjia 被调用，局部变量 game 绑定到原函数对象")
    def inner(*args, **kwargs):
        print("  [调用阶段] inner 被调用，收到 args =", args, "kwargs =", kwargs)
        print("打开外挂")
        print("  [调用阶段] 执行 game(*args, **kwargs) -> 解包为 game", args)
        result = game(*args, **kwargs)   # 把收到的参数原样透传给原函数
        print("关闭外挂")
        return result
    print("  [装饰阶段] guanjia 准备 return inner（函数对象）")
    return inner

def play_dnf(username, password):
    print("来吧勇士们", username, password)

print("=== 第1步：装饰（执行赋值号右侧 guanjia(play_dnf)）===")
play_dnf = guanjia(play_dnf)

print("\n=== 第2步：调用（执行 play_dnf('admin','123456')，实际是 inner(...) ）===")
play_dnf("admin", "123456")
