import sys

# 1) 列表对象 与 生成器对象 本身占多大内存
big_list = list(range(1_000_000))
gen = (x for x in range(1_000_000))

print("list 对象大小      :", sys.getsizeof(big_list), "字节  (~%.2f MB)" % (sys.getsizeof(big_list)/1024/1024))
print("generator 对象大小 :", sys.getsizeof(gen), "字节")
print("range 对象大小     :", sys.getsizeof(range(1_000_000)), "字节  (range 本身也是惰性的)\n")

# 2) 迭代器"只记位置"：单向、不可回退、不备份数据
it = iter([10, 20, 30])
print("next(it) ->", next(it))   # 10
print("next(it) ->", next(it))   # 20
# 此刻迭代器只"知道"自己走到了第 2 个位置；它持有的是原列表引用 + 索引，
# 并没有把 [10,20,30] 复制一份存起来

# 3) 生成器：不保存所有值，按需计算后产出
def gen_sq(n):
    for i in range(n):
        yield i * i

g = gen_sq(5)
print("\n生成器逐个产出:", [next(g) for _ in range(5)])   # 0,1,4,9,16

# 4) 迭代器是单向单次的：耗尽后不能再取（证明它没有备份全部数据）
it2 = iter([1, 2, 3])
for _ in it2:
    pass
try:
    next(it2)
except StopIteration:
    print("迭代器耗尽后 next() 抛 StopIteration —— 它只维护当前位置，没有备份整段数据，无法回退/重启")
