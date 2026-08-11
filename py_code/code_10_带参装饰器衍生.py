import functools

# ---------- 通用装饰器：用 *args,**kwargs 接住并转发任意参数 ----------
def guanjia(game):
    @functools.wraps(game)
    def inner(*args, **kwargs):
        print("打开外挂")
        game(*args, **kwargs)
        print("关闭外挂")
    return inner

@guanjia
def play_dnf(username, password):
    print("来吧勇士们", username, password)

@guanjia
def play_lol(username, password, hero):
    print("我要打联盟")
    print("开始游戏", username, password, "英雄:", hero)

print("=== 通用版：两个函数都能跑 ===")
play_dnf("admin", "123456")
play_lol("admin", "123456", "亚索")

# ---------- 演示"inner 写死 2 参"的隐患 ----------
def guanjia_bad(game):
    def inner(username, password):     # 写死 2 个形参
        print("打开外挂")
        game(username, password)
        print("关闭外挂")
    return inner

@guanjia_bad
def play_lol_bad(username, password, hero):
    print("我要打联盟", hero)

print("\n=== 隐患版：play_lol 有 3 参，inner 只有 2 参 ===")
try:
    play_lol_bad("a", "b", "c")
except TypeError as e:
    print("报错：", e)
