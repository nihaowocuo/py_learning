"""
Q87 演示：装饰器 vs 直接改原函数；多层装饰器嵌套（外挂叠加）的执行顺序
"""
import functools

# ---------- 1) 原始游戏函数（不碰它的源码）----------
def play_game():
    print("    [游戏本体] 打怪中 ...")

# ---------- 2) 方案A：直接改原函数（把外挂逻辑写进源码）----------
def play_game_direct_modified():
    print("    [外挂] 透视开")        # 直接改了原函数
    print("    [游戏本体] 打怪中 ...")
    print("    [外挂] 透视关")

# ---------- 3) 方案B：装饰器 = 在外面包一层，原函数源码不动 ----------
def cheat_see(func):                 # 别人的"透视"外挂
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("    [外挂A 透视] 开")
        result = func(*args, **kwargs)
        print("    [外挂A 透视] 关")
        return result
    return wrapper

def cheat_speed(func):               # 我的"加速"外挂
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("    [外挂B 加速] 开")
        result = func(*args, **kwargs)
        print("    [外挂B 加速] 关")
        return result
    return wrapper

# 别人已经把原函数包了一层
game_with_A = cheat_see(play_game)

# 我在"别人的外挂"外面再包一层我的外挂（嵌套在最外层，不碰别人的源码）
game_with_A_and_B = cheat_speed(game_with_A)

print("=== 直接改源码版 ===")
play_game_direct_modified()

print("\n=== 装饰器叠加版（B 在外、A 在中、原函数在内）===")
game_with_A_and_B()

# 等价语法糖：从下往上依次包裹
@cheat_speed
@cheat_see
def play_game2():
    print("    [游戏本体] 打怪中 ...")

print("\n=== 语法糖 @ 写法（效果同上）===")
play_game2()
