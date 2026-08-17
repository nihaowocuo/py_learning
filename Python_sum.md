# Python_sum（问题与答复精简汇总）

## 问题（精简）
如何检测电脑是否已安装 Python 及解释器，并查找其安装位置？

## 答复（精简）
1. **是否安装**：在 CMD/PowerShell 执行 `python --version`、`py --version`、`python3 --version`；有版本号即已装。
2. **查找位置**：
   - `where python` 列出 PATH 中所有 python.exe 路径
   - `where py` 找启动器 py.exe
   - `py -0p` 列出本机全部 Python 及完整路径（最全）
   - 代码中 `import sys; print(sys.executable)` 得当前解释器路径
3. **其它途径**：系统"已安装应用"搜 Python；常见目录 `C:\Python3X\`、`AppData\Local\Programs\Python\`；注册表 `HKLM\SOFTWARE\Python\PythonCore`。
4. **原理**：这些命令分别通过 PATH 查找、启动器扫描注册表、运行时自检来定位解释器。

## 本机结果
已装 Python 3.13.14（WorkBuddy 隔离环境，路径 `...\binaries\python\versions\3.13.12\python.exe`）与 3.13.7（`D:\py\python.exe`），另有 Microsoft Store 占位程序（`WindowsApps\python.exe`）。

---

## 问题（精简）
为何 D 盘与 C 盘均有 Python，且 Python 解释器该如何查看是否已经安装？

## 答复（精简）
1. **D 盘**：`D:\py\python.exe` 是 python.org 官方安装包安装的真正解释器（3.13.7）。
2. **C 盘**：`C:\Users\...\WindowsApps\python.exe` 是 Microsoft Store 的"应用执行别名"，是重定向器/安装引导器，不是完整解释器。
3. **为何同时存在**：Windows 给 `python` 命令保留了 Store 别名；你同时安装了 python.org 版到 D 盘。`where python` 把 PATH 中匹配项都列出，实际运行按 PATH 顺序优先用 D 盘那个，所以 `python --version` 显示 3.13.7。
4. **判断解释器是否已安装**：
   - `py -0p` 最可靠，只列出注册表中正式注册的解释器（本机仅 D 盘 3.13.7）
   - `python --version` 有版本号即已找到可运行解释器
   - `where python` 会列出所有路径，但可能包含 Store 占位
   - `import sys; print(sys.executable)` 显示当前真正运行的解释器路径

---

## 问题（精简）
Python 解释器与 Python 环境是什么关系？没有解释器是否仍能写 Python 代码但无法运行/测试？

## 答复（精简）
1. **解释器**：`python.exe` 本身，负责读取、编译、执行代码，是真正的引擎。
2. **环境**：能运行 Python 的一整套配套 = 解释器 + 标准库 + 第三方包（可选）+ 配置（PATH 等）。
3. **关系**：解释器是环境的核心引擎；环境是包着引擎的工作台。虚拟环境（venv）也必须基于已安装的解释器，不能凭空生成引擎。
4. **没有解释器能否写代码**：能——写代码只是用编辑器创建 `.py` 文本，不需要解释器；但不能运行、看不到输出、也发现不了运行时错误。IDE 的语法静态检查（红波浪线）只是"读代码找错"，不算真正执行。结论：写代码不需要解释器，但运行与测试必须依赖它。

---

## 问题（精简）
是否需要把 `D:\py\Scripts` 加入环境变量 PATH？

## 答复（精简）
1. **建议加入**：`Scripts` 里有 `pip.exe` 及 pip 安装的工具，加入 PATH 后才能直接运行 `pip install xxx`。
2. **不加也能用**：可用 `python -m pip install xxx` 代替，但较繁琐。
3. **本机状态**：`where pip` 已指向 `D:\py\Scripts\pip.exe`，说明 Scripts 已在 PATH 中，无需重复添加。
4. **建议清理**：若 `C:\Python38` 与 `C:\Python38\Scripts` 已废弃，可从 PATH 删除，避免版本冲突。

---

## 问题（精简）
为何环境变量里看不到 `py`？

## 答复（精简）
1. `py.exe` 安装位置是 `C:\Windows\py.exe`（本机 `where py` 已验证）。
2. `C:\Windows` 是 Windows 默认 PATH 目录，放这里的程序全局可用，无需手动加 PATH 条目——所以环境变量编辑器里看不到 `py`。
3. 这是官方设计：`py` 作全局启动器，用 `py -0p` 统一管理本机所有 Python 版本，与具体安装解耦。
4. 对比：`python` 是具体安装的解释器（如 `D:\py`），需自己的 PATH 条目；本机 `D:\py` 与 `D:\py\Scripts` 已在 PATH 中。


6. **Q：退出 Python 只能用 `exit()` 吗？`quit` 也能退出？**
   **A：** `exit()` 与 `quit()` 在 Python 交互式解释器中都是退出别名，等价；还有 `Ctrl+Z`（Win）、`Ctrl+D`（Linux/Mac）、`sys.exit()`、`os._exit()` 等。`quit` 不是 SQL 专用命令，Python 自己也有同名退出对象。

7. **Q：Python 计算中无需转换数据类型，会自动转换吗？**
   **A：** 部分错误。数值类型（int/float/complex）运算会自动提升（int+float→float，`/` 永远 float）；但 Python 是强类型，int 与 str 等不同类型不能直接运算会报错，需手动 `int()`/`str()` 转换。结论：仅数值类型间自动提升，跨类型不会自动转换。

8. **Q：为什么 `"当前剩余的钱：" + money` 报错 TypeError？**
   **A：** 因为 `money` 是 float，字符串 `+` 只能拼接 str，不能自动转 float 为 str。修复用 `str(money)`、推荐 `f"..."` 或 `%.2f` 格式化。本质：Python 强类型，跨类型不自动转换。

9. **Q：`==` 能判字符串相等，其他类型的相等怎么判断？**
   **A：** `==` 比较值相等，对所有类型通用（字符串、数字、列表、字典等）。`is` 比较对象身份（同一对象），仅用于 `is None` 等。浮点别用 `==`，用 `math.isclose()`。记住：值相等用 `==`，同对象/None 用 `is`。

10. **Q：print 打印默认换行，如何让它不换行？**
    **A：** `print()` 默认 `end='\n'` 自动换行；使用 `end=''` 即可取消换行：`print('A', end='')`。也可用 `end=' '` 等自定义结尾。

11. **Q：Python 中没有 double 类型吗？**
    **A：** Python 没有 `double` 关键字，只有 `float`；但 `float` 本身就是 64 位双精度（IEEE 754 double）。需要更高精度用 `decimal.Decimal`。

12. **Q：切片负 step 为何取不到内容？`[2:14:-2]`、`[0:12:-1]` 空，但 `[0::-1]` 出 'a'？**
    **A：** 负 step 表示向左(减小)取，必须满足 start>=stop。默认 stop：负 step 时为 -1(首前)。`[2:14:-2]` 因 2<14 方向相反→空；`[0:12:-1]` 因 0<12→空；`[0::-1]` 从0向左只到-1前→仅索引0='a'。正确写法 `[14:2:-2]`。想左往右必须用正 step。

13. **Q：切片必须同号才能用吗？如何倒序每组取最左？**
    **A：** 不必同号，关键看实际索引方向是否匹配 step。负索引只是倒数简写，`[-1:-12:2]` 空因 step>0 但15>4。倒序每2取最右=`[-1:-12:-2]`='pnljhf'；取最左把起止各左移1→`[-2:-13:-2]`='omkige'(等价 `[14:2:-2]`)。

14. **Q：负索引被转成正数，所以 `[-1:-12:2]` 没法用？为何转正数？**
    **A：** 负索引统一换算为 值+len(-1→15,-12→4)，这是让负索引能用的机制(非失效)。该切片空因换算后=`[15:4:2]`，step>0 需 start<=stop，但15>4方向反。换算普遍存在且必要。

15. **Q：负索引最终转成正索引才能用，那是否也可用正索引实现？**\n    **A：** 是，任何负索引切片都有等价正索引写法（负=值+len）。负索引价值在：不用算长度、长度变化时仍正确（如 `s[-1]` 永远末位）。按意图选：倒着数用负，绝对位置用正，底层等价。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 15 个 Python 问答（切片系列收尾：负索引=正索引等价）：已追加到三文档。要点：负索引运行时统一换算值+len，存在等价正索引写法；其价值是不用算长度、长度变化时仍正确；按意图选负/正。

16. **Q：`[15:4:-2]` 从右向左需负step，改正数step冲突会无法执行？**\n    **A：** 方向冲突时返回空串 `''`（仍是 str，不报错）。`[15:4:2]` 正步长要向右但15已在4右→空。纠正：冲突得空结果，非"无法执行"。step 符号须与 start/stop 自洽。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 16 个 Python 问答（方向冲突返回空串非报错）：已追加到三文档。要点：`[15:4:-2]` 方向一致得'pnljhf'；改正数 `[15:4:2]` 返回空串''（str，不报错）；纠正"无法执行"误解——冲突是空结果非异常。

17. **Q：`[2:-12:2]` 为何不空而出 'c'？负stop不是右边吗？**\n    **A：** stop=-12 换算为 4(索引4,e)，等价 `[2:4:2]`。方向只看 step：+2 左→右，start=2<=stop=4 一致→非空；取索引2(c)后下一步4是stop停止→'c'。负stop只是固定正索引，可能恰在start右侧，不必然冲突。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 17 个 Python 问答（负 stop 不必然导致空）：已追加到三文档。要点：`[2:-12:2]` 中 stop=-12 换算为索引4，等价 `[2:4:2]`，step=+2 左→右且2<=4 一致→取索引2='c'。易错：负stop是固定正索引非"方向"，可能恰在start右侧不冲突。

18. **Q：`capitalize()` 对中文有效吗？首字符是中文会怎样？**\n    **A：** 对中文本身无效（无大小写）。规则：首字符若为字母则大写，其余字母全部小写。首字符是中文/数字/标点时保持不变，但后续英文大写会被强制小写（如 `你好Python世界` → `你好python世界`）。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 18 个 Python 问答（capitalize 对中文行为）：已追加到三文档。要点：capitalize 对中文无大小写处理；首字符非字母时保持不变，但后续字母会被强制小写；例 `你好Python世界`→`你好python世界`。

19. **Q：验证码 `.upper()` 比较有安全风险吗？为何生成混合大小写？**\n    **A：** 对展示型验证码，大小写不敏感比较不是风险(常见UX)。但生成"Xado"又忽略大小写是设计矛盾——混合大小写提供0安全性且让用户困惑。应：①生成单大小写直接`==`；或②要大小写作安全因子就精确比较并提示区分。注意密码绝不可先`.upper()`再比(真实漏洞)。高安全用`secrets.compare_digest()`。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 19 个 Python 问答（验证码大小写不敏感比较的安全设计）：已追加到三文档。要点：展示型验证码不敏感比较非风险；生成混合大小写又忽略大小写是设计矛盾(0安全性+困惑)，应单大小写直接==或精确比较；密码绝不可先.upper()再比(真实漏洞)；高安全用 secrets.compare_digest。

20. **Q：混合大小写本为增安全，忽略大小写比较不就抵消了？**\n    **A：** 正是。组合数=字符集^长度；混合(52)比单(26)在长度N时多 2^N 倍安全(N=4约16倍)。但 `.upper()` 比较归一为26，混合收益归零，用户小写也能过=白放宽。修复：①要安全就精确比较`==`并提示区分大小写；②纯UX就生成单大小写直接`==`。两头不讨好最差。\nEOF

cat >> "E:/py_learning/.workbuddy/memory/2026-07-26.md" <<'EOF'
- 第 20 个 Python 问答（混合大小写安全被忽略比较抵消）：已追加到三文档。要点：组合数=字符集^长度，混合52比单26多2^N倍安全(N=4≈16倍)；但.upper()比较归一26使混合收益归零；修复=精确比较+提示区分，或单大小写直接==。

21. **Q：`money.isdight()` 报错 AttributeError 是什么原因？**
    **A：** 方法名拼写错误。Python 只有 `isdigit()`，没有 `isdight()`（g/t 顺序写反）。报错里的 `Did you mean: 'isdigit'?` 已直接提示。修复：改成 `money.isdigit()`。注意 `isdigit()` 只认纯数字，小数点、负号都会返回 False。

22. **Q：输入 123.2 后 `isdecimal()` 判断失败，它不是判断小数的吗？**
    **A：** `isdecimal()` 只认纯十进制数字字符，`123.2` 含小数点 → False。`isdigit/isdecimal/isnumeric` 都不认识小数点、负号、e。判断小数应使用 `float()` + try/except。结论：`isdecimal()` 判断纯数字串，非小数。

23. **Q：PyCharm 提示 `isdecimal()`，为什么叫"小数"？它和小数有关吗？**
    **A：** `decimal` 英文是"十进制的"，不是"小数"，中文误译导致混淆。`isdecimal()` 判断字符串是否全由十进制数字字符(0-9)组成，与小数判断无关。判断小数用 `float()` + try/except。

24. **Q：`isdigit` 是什么？与 `isdecimal` 的不同？**
    **A：** `isdigit()` 判断字符串是否全由数字字符组成，比 `isdecimal()` 宽松，额外接受上标(²)、圈号(①)等；两者都不认小数点、负号、中文数字、分数。日常判断纯整数输入用 `isdigit()`；小数用 `float()` + try/except。宽松度：isnumeric >= isdigit >= isdecimal。

25. **Q：能否将多个字符串连接起来，像列表一样？**
    **A：** 能。方法：`+` 拼接、推荐 `join()`、f-string、循环。多个或大量字符串拼接用 `join()` 性能最佳（一次性分配内存，比循环 `s = s + x` 快几十倍）。`sep.join(列表)`，元素必须全是字符串。列表合并和字符串拼接是两回事。

26. **Q：多个独立变量字符串（s / s1 / s2 / s3）能否用 join 一起拼接？**
    **A：** `join` 只接 1 个可迭代对象，直接传多参数会 `TypeError`。解法：装进 list / tuple 再 join，或直接 `+` 拼接，或 f-string。变量多/动态时优先装容器再 join；少而固定可用 `+` 或 f-string。

27. **Q：`"_".join(s, s1, s2, s3)` 为何报 TypeError？**
    **A：** `join` 只接受 1 个可迭代对象参数，你传了 4 个字符串。修复：装 list → `"_".join([s, s1, s2, s3])`；或用 `+`/f-string。

## Q28 列表切片是否产生新列表？
**问**：`lst=[1,2,3]`，切片 `lst[1:3]` 是否不改变原列表、只产生新列表？
**答**：是。切片是读取表达式，返回新列表、原列表不变（`new is lst` 为 False）。切片赋值 `lst[1:3]=[...]` 才会改原列表。切片属浅拷贝，嵌套可变元素需注意。

## Q29 print(lst[1:3]) 输出的是新列表吗？
**问**：`print(lst[1:3])` 输出的是新的列表吗？
**答**：新列表由切片 `lst[1:3]` 产生，print 仅显示其文本 `[2,3]`，不创造也不保留列表（print 返回 None）。未赋值时该新列表为临时对象、打印完即回收，原列表不变。

## Q30 列表能装任何类型，为何 append 字符串会出黄色提示？
**问**：Python 列表不是能装任何类型吗，为何在一串 int 后 append 字符串会出现黄色提示？
**答**：Python 运行时允许混装。黄色提示是 PyCharm 静态类型推断的结果：它认为该列表是 list[int]，append str 即报警告；并非运行错误，程序可正常执行。元组内的列表对象可变，append 合法。

## Q31 print(切片) 中"新列表"如何展示、临时存储？
**问**：print(切片) 的新列表如何展示？是否有默认东西临时存储、运行关闭后才消失？
**答**：print 调用列表的 __str__ 把内容拼成文本 [2,3] 显示（展示的是文本而非对象本身）。"临时存储"是调用栈的求值栈槽位，仅在 print 期间持有引用；print 返回后引用计数归零，列表立即回收，早于程序结束。每次切片都是独立新对象。

## Q32 栈是什么，堆又是什么？
**问**：print 输出的列表存储到调用栈中，栈是什么，堆又是什么？
**答**：栈是函数调用栈，存局部变量名、函数帧和临时求值槽位，LIFO、自动管理、函数返回即释放。堆是存放所有 Python 对象的内存区，靠引用计数/GC 回收。栈只保存引用，真正对象在堆；print(切片) 的临时列表被栈槽短暂引用，print 返回后即被回收。

## Q33 字典如何取单个 key / value？
**问**：`dic.keys()` 取所有 key，那取单个 key 或 value 怎么做？
**答**：`dic.keys()` 返回 dict_keys 视图，不支持索引。取单个 key：`list(dic.keys())[0]` 或 `next(iter(dic))`。按 key 取值：`dic['a']` 或更安全的 `dic.get('a')`。取单个键值对：`next(iter(dic.items()))`。视图轻量不复制数据，需转列表或用迭代器才能按位置取。

## Q34 dict.items() 为何返回长度为 2 的元组？
**问**：`for item in dic.items()` 每次拿到的 `item` 长度为 2，是默认规定还是临时修改？
**答**：是 `dict.items()` 的默认规定。该方法每次返回 `(key, value)` 元组，长度固定为 2。`keys()` 返回单个 key，`values()` 返回单个 value，`items()` 返回键值对元组。推荐用 `for key, value in dic.items():` 直接拆包。

## Q35 嵌套字典为何报错？
**问**：截图中的嵌套字典写法为何报错？
**答**：`"sex": "男"` 后缺少逗号，导致 Python 无法继续解析 `"hobby": {...}`，报 `SyntaxError`。字典键值对之间必须用逗号分隔。修复：补逗号。建议最后一项也保留尾随逗号，减少后续新增时漏逗号。

## Q36 嵌套字典访问为何报 KeyError: 'game'？
**问**：截图中的嵌套字典访问报错，原因是什么？
**答**：`KeyError: 'game'` 表示 `dic` 第一层没有 `'game'` 键，它实际嵌套在 `'hobby'` 下。应逐层访问 `dic["hobby"]["game"]["game_name1"]`。另外建议变量名不要用 `str`，避免覆盖内置类型。

## Q37 为何一边循环一边删除字典会报错？
**问**：`for key in dic:` 中根据条件删除 key，为何报 `dictionary changed size during iteration`？
**答**：字典迭代器依赖内部游标，删除键会改变字典大小/结构导致游标失效，`del` 和 `pop` 都会触发。解决：遍历 `list(dic.keys())` 快照、先收集再删除、或用字典推导式重建新字典。

## Q38 open 带 encoding 为何报黄线？
**问**：`open("文本测试.txt","r",encoding="utf-8")` 出现什么问题？
**答**：PyCharm 静态类型检查误报（open 重载多，IDE 未精确推断文本模式），代码可正常运行。更应注意 open 后未关闭文件，推荐 `with open(...) as f:` 自动关闭。若黄线仍在可忽略。

## Q39 open() 报 unexpected keyword argument 'endoding'
**问**：`open(..., endoding="utf-8")` 运行报错是什么意思？
**答**：参数名拼写错误，正确应为 `encoding="utf-8"`。Python 关键字参数必须严格匹配，拼错会报 TypeError；错误信息已提示 Did you mean 'encoding'。修正后建议用 `with open(...) as f:` 自动关闭文件。

## Q40 Python 变量为何可以重复使用？
**问**：代码中两次使用 `line = f.readline()`，为什么不会报错？
**答**：Python 变量是对象的名字/引用，不是固定存储盒。`line` 第一次指向第一行字符串，第二次改指向第二行字符串；旧对象失去引用后被回收，所以不会报错。Python 无需声明变量。顺带 `readline()` 保留行尾 `\n`，`print()` 再加一个换行，会输出空行，可用 `strip()` 或 `end=""` 消除。

## Q41 为何不能在 print 函数外添加 strip 方法？
**问**：为什么不能写 `print(line).strip()`，只能写 `print(line.strip())`？
**答**：执行顺序不同。`print(line.strip())` 先对字符串调用 `.strip()`，再把结果给 `print`；`print(line).strip()` 先执行 `print`（返回 `None`），再对 `None` 调用 `.strip()`，因此报 `AttributeError: 'NoneType' object has no attribute 'strip'`。方法必须挂在有该方法的对象上。

## Q42 如何只循环文件中的指定行？
**问**：`for line in f` 会遍历所有行，如何只循环指定行？
**答**：可通过 `itertools.islice(f, N)` 取前 N 行、`islice(f, start, stop)` 取行号范围、`enumerate(f, start=1)` 配合 if 按行号过滤，或按内容条件过滤。文件对象只能顺序读一次，islice 停止后需重新 open 才能再读；小文件也可用 `readlines()` 转列表后切片。

## Q43 如何在 `for line in f` 基础上只循环指定行？
**问**：想只循环指定行，写 `for line in f(1, 3):` 为何不行？有哪些方案、各需不需要导包？
**答**：`f` 是文件对象，不是函数，不可调用，会报 `TypeError`。可行方案：① `itertools.islice(f, start, stop)`（需导包，推荐，内存友好）；② `enumerate(f, start=1)` 配合 `if`（无需导包，最常用）；③ `f.readlines()` 后列表切片（无需导包，小文件可用）；④ 手动计数器（无需导包，不推荐）。

## Q44 `f = open()` 能读图片吗？
**问**：`with open()` 能读图片，那 `f = open()` 打开的呢？
**答**：两者调用的是同一个 `open()` 函数，读图片能力完全一致。区别仅是 `with` 自动关文件、`f = open()` 需手动 `f.close()` 且异常时可能漏关。读图片必须用二进制模式 `'rb'`（读出 bytes），文本模式 `'r'` 会报 `UnicodeDecodeError`。推荐 `with` 写法因其异常安全、自动关闭。

## Q45 如何跨文件/跨目录读取文件？
**问**：如何跨文件读取？
**答**：跨文件读取即在 `open()` 中给出目标文件路径。三种写法：① 相对当前工作目录；② 相对当前脚本位置（`os.path.dirname(os.path.abspath(__file__))` + `os.path.join("..", ...)`，推荐）；③ 绝对路径。路径符号：`./` 当前目录、`../` 上级目录。读跨目录图片与文本相同，模式用 `'rb'`。若需使用另一个 `.py` 的变量/函数，用 `import` 而非 `open()`。

## Q46 `with` 同时打开两个文件复制图片为何报错？
**问**：写 `with open(...) as f1, \` 后换行再写 `open(...)` 报 `invalid syntax`，原因是什么？
**答**：`\` 续行符后不能有空行，必须紧跟后续代码。三种正确写法：① 一行写完；② 反斜杠续行且中间无空行；③ 用括号包裹（推荐）。另外目标文件应 `"wb"` 写入，二进制文件复制建议 `f2.write(f1.read())` 或按块读写，不要用 `for line in f1`。

## Q47 复制图片报 `FileNotFoundError: '../tou.png'`？
**问**：修正 with 多文件语法后，运行报 `FileNotFoundError: '../tou.png'`，为什么？
**答**：相对路径基于"当前工作目录"解析，PyCharm 默认工作目录是项目根目录 `E:\py_learning`，`../tou.png` 被解析为 `E:\tou.png`，与文件实际位置不符。修正：按工作目录写 `open("tou.png", ...)`，或用 `os.path.dirname(os.path.abspath(__file__))` 按脚本位置拼接路径（推荐）。目标文件应用 `"wb"`。

## Q48 直接运行脚本 `open("tou.png")` 仍报 `FileNotFoundError`？
**问**：用 `D:\py\python.exe 脚本.py` 运行后，`open("tou.png")` 仍报找不到，为什么？
**答**：直接运行脚本时，当前工作目录是命令行所在目录（非脚本/项目根目录），`open("tou.png")` 去该目录找而找不到。唯一可靠方案是用 `__file__`（os.path.dirname(os.path.abspath(__file__))）计算脚本位置再拼接路径，不受运行环境影响。PyCharm 运行或命令行在 E:\py_learning 下运行时 open("tou.png") 才有效。

## Q49 文件存在但 open 仍报 FileNotFoundError？
**问**：E:\py_learning 下明明有 tou.png，命令行运行脚本后仍报 FileNotFoundError: 'tou.png'，为什么？
**答**：相对路径基于"当前工作目录"解析，命令行运行脚本时 cwd 是命令敲击时的目录而非项目根，故相对路径找不到。文件存在不等于 open 找得到。三种解决：① 运行前 `cd` 到项目根；② 用绝对路径（硬编码）；③ **推荐**用 `__file__` 计算脚本位置再拼接路径。换电脑换环境都不变。

## Q50 相对路径基准点到底是什么？如何以脚本目录为基准访问外层文件？
**问**：之前说相对路径起点是 py_learning，现在又说是 cwd，如何解释？如何在 py_code 目录下访问外层目录的文件？
**答**：相对路径基准就是"当前工作目录"（cwd），由运行方式决定（PyCharm 运行=项目根，命令行运行=命令敲击目录），并不固定。以脚本目录为基准访问外层文件：① cwd 恰好是 py_code 时用 `open("../tou.png")`；② **推荐**用 `__file__`（os.path.dirname(os.path.abspath(__file__))）+ os.path.join("..", "tou.png")，任何 cwd 下都有效。排障口诀：先 `print(os.getcwd())`。

## Q51 是否必须把图片复制到 py_code 才能操作？
**问**：是不是只能把图片复制到 py_code 目录，再用命令打开并复制到 py_code 下的另一个文件？
**答**：完全不需要。`open()` 按文件路径找文件，与文件在哪个目录无关。源文件放 py_learning 不动，py_code 里的脚本用 `__file__` 方案（os.path.dirname(os.path.abspath(__file__)) + join("..", "tou.png")）即可直接读外层文件，并把副本写到 py_code 内。之前报错只是路径写错，不是必须移动文件。

## Q52 能否在现有代码基础上修改？tou.png 为何被删？
**问**：能否不用 __file__ 方案，在我现有代码基础上修改？运行程序后 py_learning 下的 tou.png 为何被删除了？
**答**：可以。你的代码（rb 读 tou.png、wb 写 py_code/头像.png）本身不会删除源文件；tou.png 被删是此前 AI 演示用 `open(..., "wb")` 创建测试图片时覆盖了同名真实文件并在清理时删除（git/回收站均无记录，无法恢复，深表歉意）。在你代码基础上修改：① 不改代码，命令行先 `cd /d E:\py_learning` 再运行；② 代码开头加一行 `os.chdir("E:/py_learning")`。教训：`"wb"`/`"w"` 模式会清空覆盖同名文件，测试勿覆盖真实文件。

## Q53
问：用 rb 读 tou.png 又用 wb 写 头像.png，中途出错未写入、文件被打开后被清理删除？
答：不会。rb 不删源文件；wb 只清空它自己指定的文件（头像.png）；with 出错仅关闭句柄、不删文件。文件删除只能靠 os.remove()。真实 tou.png 丢失是 AI 演示代码用 wb 覆盖并清理所致，与你的代码无关。

## Q54
问：同目录下复制图片成功，为何跨目录执行失败？
答：相对路径从 cwd 解析，不是从脚本目录。同目录成功是因为 cwd 正好等于文件目录。跨目录失败是因为 cwd 与路径写法不匹配（如在 py_code 里写 `../tou.png` 会指到项目根；在项目根里写 `py_code/头像.png` 会指到 py_code，但若同时写 `tou.png` 则又指到项目根）。用 `os.getcwd()` 看 cwd，最稳用 `__file__` 以脚本目录为基准。

## Q55
问：教程里用 ../ 跨目录写文件为何能成功，我之前却失败？
答：跨目录相对路径本身没问题，关键是路径、文件实际位置、运行时 cwd 三者要匹配。教程中脚本、源文件同目录，且 ../01_初识python 真实存在，所以成功。之前失败是因为 cwd 或文件位置与 ../tou.png、py_code/头像.png 等写法对不上，不是跨目录写法本身有错。用 os.getcwd() 和 os.path.abspath() 可自查。

## Q56
问：如何判断当前目录以正确使用 ./ 与 ../？
答：应判断"当前工作目录 cwd"而非根目录。`./`=cwd，`../`=cwd 上级。用 `os.getcwd()` 查看 cwd，用 `os.path.abspath("相对路径")` 验证解析结果。相对路径只与 cwd 有关，与脚本位置无关。

## Q57
问：如何进入下级目录？../ 加更多点是不是更上一级？
答：进入下级目录直接写 `子目录/文件名` 或 `./子目录/文件名`。`..` 是上一级；上两级是 `../..`，不是 `...`，每多一个 `../` 段才多上一级。截图代码从 cwd 上级读 tou.png、在 cwd 写 头像3.png，前提是 ../tou.png 真实存在。

## Q58
问：读源→改→写新文件→删源改名，这是文件操作实质吗？
答：整体正确，是"安全原地编辑"标准范式，但只是原地修改一种场景，并非所有文件操作实质。纠正：第4步用 `os.replace(new, source)` 一步替换（Windows 上 os.rename 遇已存在目标报 FileExistsError，已实测）；小文件也可读入内存后 `open("w")` 重写，无需临时文件。

## Q59
问：代码为何报 FileNotFoundError: '名单'？
答：代码里 open("名单") 与实际文件名 `名单.txt` 不匹配，缺扩展名。应改为 `名单.txt`。另有隐藏 bug：`line.replace("张","周")` 未赋值给 line，修改不会生效，需写 `line = line.replace(...)`。若最终覆盖原文件，末尾用 os.replace。

## Q60
问：Word 改一个字后保存就是 read→modify→write temp→replace？另存为是源和新都在？
答：对。保存=内存改→写临时文件→原子替换原文件（同你学的模式），保存后磁盘仍是 1 个文件（被替换）。.docx 是压缩包，改一字要重写整篇，不是改单字节。另存为=新路径写当前内容、源文件保留，故源与新同时存在（2 个）。

## Q61
问：git revert 后文件消失，git reset --mixed 找回无效，如何恢复并真正删除错误提交？
答：文件消失因 `git revert` 反转了新增文件（code_10_函数.py）的改动将其从工作区删除；`--mixed` 不恢复工作区文件，用 `git checkout HEAD -- <file>` 找回。想删除错误提交用 `git reset --soft HEAD~1`（revert 只会新增反向提交、原提交仍在）。当前 HEAD 与远端都停在错误提交 1a5c03c，目标未达成；重提需 reset --soft HEAD~1 + 改内容 + commit + `git push --force-with-lease`（因已推送）。reflog/fsck 可兜底找回。

## Q62
问：print(a,b,c,*args,**kwargs) 为何报 TypeError: unexpected keyword argument 'hello'？
答：`**kwargs` 解包把 {'hello':465,'haha':654} 变成关键字参数传给 print，而 print 只接受 sep/end/file/flush 四个关键字，不认 hello/haha。修复：打印字典用 `print(..., kwargs)`，或遍历 items；透传只能用 print 支持的键。


## Q63
问：教程 `def func(a,b,*args,c="哈哈",**kwargs): print(a,b,c,args,kwargs)` 正常打印，为何用户写法报错？
答：两个差异：① 教程 c 在 *args 之后、是有默认值的 keyword-only 参数；用户 c 在前、必填。② 教程 print 不带 */**（args、kwargs 当对象打印），用户 print 加 **（kwargs 解包成关键字参数传给 print，print 只认 sep/end/file/flush，不认 hello/haha）。推荐 `print(a, b, *args, kwargs)`。


## Q64
问：func(1,2,haha=654) + print(a,b,c,*args,**kwargs) 为何报 TypeError: unexpected keyword argument 'haha'？
答：根因同 Q62/Q63——**kwargs 解包把 haha 作为关键字参数传入 print，print 不认。另缺必填位置参数 c（调用只给 a,b）。修复：print 去掉 ** 改为打印 kwargs 对象，并补上 c=3。


## Q65
问：func(hello=456,haha=654,1,2,3,4) 报 SyntaxError: positional argument follows keyword argument，请总结实参与形参输入规律。
答：Python 实参铁律——位置参数必须集中在前、关键字参数必须集中在后，不能穿插。形参定义顺序为：必填位置 → 默认值位置 → *args → keyword-only → **kwargs。实参绑定流程：位置按顺序绑必填、多余进 *args；关键字按名字匹配、剩余进 **kwargs；keyword-only 必须用关键字传。


## Q66
问：ord 是否取字符编码，chr 是否把编码转字符？
答：方向对。ord 取 Unicode 码点（整数），chr 把码点转字符，二者互逆。但严格说 ord 不是"编码"，编码指字符↔字节序列（用 encode/decode）。ord 只返回整数码点。


## Q67
问：VS Code 运行输出处为何没有搜索功能？
答：当前是"运行/输出"面板，搜索支持受限；应切换到"终端"面板（Ctrl+` 新建终端），在终端里运行脚本后按 Ctrl+F 搜索。另建议 range(65536) 输出过多控制字符会卡终端，可缩小范围测试。


## Q68
问：终端中 `py code_10_函数` 报 No such file，该如何运行？
答：文件名缺 `.py` 扩展名。Python 不会自动补扩展名，应写 `py code_10_函数.py` 或 `python code_10_函数.py`。当前 cwd 已在 py_code，无需路径。


## Q69
问：`for i in range(65536): print(chr(i)+" ", end="")` 为何看起来没全部打印？
答：代码确实执行了 65536 次，但 0-65535 包含大量控制/不可见字符（\n/\r/\b/\t 等），会换行、回车、退格或显示为空白，导致终端看起来没打印完或显示混乱。应只打印可见范围（32-127 或 19968-40870）或用 `isprintable()` 过滤。


## Q70
问：PowerShell 终端中直接输入 `help(str)` 为何报错？
答：终端是 PowerShell 环境，不是 Python 解释器；`help()` 是 Python 内置函数，PowerShell 不认识。应先输入 `py` 进入 Python 交互式解释器再执行 `help(str)`，或在脚本中运行。


## Q71
问：`print(fun1(fun2))` 与 `print(fun1(fun2()))` 为何会输出 None？
答：fun1 内部无 return，默认返回 None；外层 print 打印的是 fun1 的返回值，故出现 None。fun2() 调用时先打印 hi；fun2 本身作为参数时只是函数对象、未执行。


## Q72
问：截图代码 `print(fun1(fun2()))` 的运行顺序是什么？
答：先求参数 fun2() → fun2 内部调用 fun1()（返回 hello 但未被使用/返回，丢弃）→ fun2 返回 None → 调用 fun1(None) 返回 "hello" → print 输出 hello。最终只输出 hello。


## Q73
问：print(fun1(fun2)) 与 print(fun1(fun2())) 的区别？
答：fun2（无括号）是函数对象，不执行函数体，把函数当数据传入；fun2()（有括号）立即调用函数，传其返回值。当前两者都输出 hello，但第二行会先执行 fun2 整个函数体。


## Q74
问：fun2() 是调用取返回值传入，fun2 是传入函数对象本身？
答：对。fun2() 执行函数体、传返回值（数据）；fun2 传函数对象本身（可调用能力）。区别在于接收方能否再次调用它——传函数对象可再调用，传返回值则不能。


## Q75
问：函数可作返回值、可作参数、函数名即变量指向内存地址，是否正确？
答：三点皆正确，对应"函数是 first-class object"。①②即高阶函数/闭包/装饰器基础；③ 中 def 实为"把函数对象绑定到名字"，更精确表述是"名字是对函数对象的引用"，`print(func)` 末尾显示的 0x... 即该对象地址。函数与 int/list 一样可被绑定、传递、返回、存入容器。


## Q76
问：变量存的是数据的起始位置，还是只是一个索引位置？
答：变量存的是“指向对象的引用”，底层即对象在内存中的地址（起始位置），不是数据内容，也不是容器下标索引。CPython 中名字在 dict 命名空间里映射到 PyObject* 指针，id(obj) 即该地址（故 Q75“函数名指向内存地址”成立）。容器对象内部还持有指向各元素的二级指针（多级间接）。与 C 指针不同，Python 把地址隐藏，不能做地址运算。


## Q77
问：变量存的就是真实内存地址的首位？
答：CPython 下是——变量持有指向对象的指针，即对象在内存中的真实起始地址（首位）。该地址指向整个对象（含对象头），id(obj) 即它，但 Python 隐藏地址不可直接运算；其他实现（PyPy 等）id 未必是真实地址。名字在命名空间 dict 中的值格装的就是这个指针。


## Q78
问：变量指向的是封装后的东西，不是直接指向具体数据？
答：对。变量指向对象，对象=对象头(类型/引用计数等元数据)+数据负载，数据在对象内部需经对象访问。与 C 的裸 int 不同，Python 的 42 是堆上的 int 对象。铁证：sys.getsizeof(42)=28 字节（含对象头开销，非 4 字节原始值）。列表内部再持指向元素的二级指针，层层封装。


## Q79
问：装饰器本质是否就是函数，作用为简化操作/集成调用？打游戏开外挂，装饰器替我开/关外挂？
答：对。装饰器是“接收函数、返回函数”的函数（即 Q75 的函数作参数+返回值），`@deco` 等价于 `原函数=deco(原函数)`。它在不改原函数代码下包入前置/后置逻辑，恰如“开外挂/关外挂”环绕原函数。时序：装饰器在定义时执行一次产出 wrapper，之后每次调用都跑 前置→原函数→后置。常见用途：计时、日志、权限、缓存、资源管理。


## Q80
问：函数名与全局/局部变量名一致是否会冲突？
答：Python 函数名与变量名共用同一命名空间，无专门分区。同作用域后者覆盖前者（greet=123 后 greet() 报 TypeError，已实测）；跨作用域局部名遮蔽全局名；最危险的是 UnboundLocalError——函数内有赋值则该名为局部，赋值前读取报 UnboundLocalError（已实测）。同名不报语法错，但会覆盖/遮蔽/未绑定。建议名字不要重复。


## Q81
问：C 的 int 才 4 字节，为何 Python 的 42 占 28 字节？
答：C 的 int 是栈上裸数据，类型编译期固定、无元数据；Python 的 int 是堆上完整对象（呼应 Q78），含对象头(引用计数8+类型指针8)+数值字段8≈28字节（含对齐），其中仅约8字节是真实数值、其余为簿记。原因：动态类型需对象自带类型指针、引用计数做GC、任意精度（2**1000实测160字节，数值用更宽的long）。加上名字引用8字节，Python“一个整数”约36字节，约为C的9倍。小整数缓存但对象仍28字节。


## Q82
问：int 像不像封装了一个类、内部有多个属性与操作？
答：对。int 是 class 'int' 类，42 是其实例；实例既带数据属性（real/imag/numerator/denominator）也带方法（bit_length/to_bytes/from_bytes）及 63 个 dunder 运算符方法（如 3+4 即 3.__add__(4)）。需区分两层：Python 层接口（代码直接可用）与 CPython 实现层 C 结构体（ob_refcnt/ob_type/ob_digit，即 Q81 的 28 字节对象头，Python 不可直接见）。对象=数据+操作即 OOP 本质。


## Q83
问：装饰器这步是否用闭包保存 `game`？定义 `inner` 时 `game()` 会执行吗？
答：是闭包，`inner` 持有外层局部变量 `game`。定义 `inner` 时不执行函数体，`game()` 不会运行。时序：`play_dnf = guanjia(play_dnf)` 只定义并返回 `inner`、重新绑定名字，不执行 `inner` 体；之后 `play_dnf()` 才执行"打开外挂 → game() → 关闭外挂"。名字 `play_dnf` 指向 `inner`，但闭包保存的是原始函数对象，不受影响。


## Q84
问：x = 42，42 是 int 实例，x 是什么？
答：x 是"名字"，绑定到 42 对象（存的是 42 的地址/引用），本身不是对象。42 是堆上对象；x 是访问它的标签。多个名字可指向同一对象（y=x 后 y is x）；type(x) 因查看所指向对象故返回 int；x=43 是重新绑定、原 42 仍在。小整数 -5~256 被缓存故 id 相同。


## Q85
问：x 只存地址？而非像 C 那样对象就是类的实例？
答：前半对（CPython 下 x 存的是 42 的地址/引用）。后半需纠正："对象=类的实例"在 Python/C++ 都通用，42 本就是 int 实例（对象）。真正区别是持有方式——Python 变量永远持引用（间接），C/C++ 变量可直接持对象本体（值语义，如栈上 struct/类对象）。实证：a=b=[1,2,3] 后 a is b 且改 a 影响 b，证明 Python 引用语义。


## Q86
问：装饰器是否等于"给原函数加操作再重新封装为原名"，和文件修改（删源、改名）一样？
答：骨架一致——都是"同名替换、接口不变、内部增强"，即你 Q58 文件原地修改的精神。但机制不同：装饰器是名字重绑（引用替换），原函数在内存不被删（闭包 game 仍持有，有引用则不销毁）；文件修改是磁盘字节覆盖，旧内容丢失。装饰器 = 内存重定向到包裹函数（保留原函）；文件修改 = 磁盘覆盖旧字节。已实测 old=play_dnf 保留原引用后 old() 仍可调用。


## Q87

问：装饰器与直接改原函数有何不同？多层嵌套（外挂叠加）在哪改？是否冗余易错？

答：装饰器不改原函数、只在外层包 wrapper 并重绑名字，可叠加、可逆、可复用；本质是函数嵌套+语法糖。"外挂"为比喻，真实外挂非此机制。叠加时在自己的外层再包一层即可（不碰别人源码），执行由外到内。不冗余；风险在忘 return wrapper / 忘调用原函 / 参数不匹配（*args,**kwargs 透传）/ 元数据丢失（functools.wraps），均易规避。


## Q88

问：wrapper 是什么？答：装饰器内部"包住"原函数的函数，负责前后插入行为并通过闭包记住原函数；非关键字，命名约定；functools.wraps 是另一回事（复制元数据）。


## Q89

问：@装饰器传过去的是不是函数+它的参数？答：只传函数对象（无括号=不调用），此步无实参；函数自带的是形参签名（定义的一部分），非装饰时额外携带；实参是之后调用 wrapper 时才传入，故 wrapper 需 *args,**kwargs 透传。


## Q90

问：带参函数装饰器，参数是否也传入管家？答：否。('admin','123456') 在调用时才进场，传给被重绑的 inner（wrapper），而非 guanjia；guanjia 装饰时只收到裸函数对象。报错因 inner 未透传参数给 game()。修复：inner 内 game(username,password) 或 *args,**kwargs 透传。


## Q91

问：对带参装饰器代码逐行注释。答：guanjia 装饰时只收函数对象；inner 为 wrapper 接调用者实参并透传 game(...)；return inner 完成名字重绑。隐患：play_lol 3 参 vs inner 写死 2 参会冲突；通用写法用 *args,**kwargs。


## Q92

问：检验执行顺序分析 + game 处为何/如何加参数。答：四步分析正确（右侧先算->guanjia 收函数对象 game=原函数->def inner 未调用->return inner 重绑->调用即调 inner）。game 需加参因原函数要 username/password，裸 game() 报缺参；通过 inner(*args) 收、game(*args) 解包实现透传。

## Q93
- 问题：game(*args,**kwargs) 解包处，是 inner 传入的参数，然后 game 获取参数进入 play_dnf() 执行？
- 答复：对。play_dnf 已被重绑为 inner，调用即调 inner；inner 收集实参后，game(*args) 解包调用原函数（game 即原 play_dnf 对象）。

## Q94
- 问题：登录装饰器为何用 `if login_flag == False:`？为何不直接"失败才操作"？如何免重复验证？
- 答复：`login_flag` 是登录态标记，==False 即"未登录才弹框"，是正确闸口写法；"失败才重试"是内层 while 的职责。全局变量+global 让登录态被四个函数共享，一次登录后免重复验证；重登只因重启进程。

## Q95
- 问题：用全局变量的目的就是不收局部变量影响、保存登录状态？
- 答复：对。全局变量生命周期=整个程序、且被所有 inner 共享；不加 global 的赋值只会建局部变量、状态丢失。global 让它跨调用持久+跨函数共享。

## Q96
- 问题：完善操作需加入退出登录，把 login_flag 重新赋值为 False？
- 答复：对。logout 函数内 `global login_flag; login_flag=False` 即可重置共享状态，之后业务函数会重新要求登录；同样必须 global，否则只改局部。

## Q97
- 问题：迭代器省内存，是否只是存了类似指针、记录位置、无真实数据？
- 答复：对。迭代器惰性、按需产出，内部只存"来源+当前位置/状态"（容器迭代器=引用+索引；生成器=函数帧+进度），不物化全部元素；代价是单向单次、不可回退/索引。

## Q98
- 问题：迭代器内部存指针一样的东西、无真实数据、只记录内存位置？
- 答复：方向对但措辞要改：不是指向数据字节的裸指针。容器迭代器=容器引用+整数索引(逻辑位置)；生成器=函数帧(指令偏移+局部变量)。数据或在原容器共享、或由生成器按需算，都不物化整段。

## Q101
- 问题：py 库是什么？与技术栈、Java 的关系？
- 答复：库=可 import 复用的代码集合(标准库内置/第三方 pip 装)；技术栈=按需挑库+框架+工具的组合，库是其零件；Java 库概念相同，区别在打包(jar)、依赖管理(Maven/Gradle)、运行(编译+JVM) vs Python(包+pip+解释)，且两者可混搭同一技术栈。

## Q102
- 问题：当前主流 Python 版本？哪些版本第三方库适配好？
- 答复：最新稳定版 3.14（2025-10 起）；生态最完整区间 3.12-3.13；3.10/3.11 安全维护期、3.9 及以下 EOL；3.15 计划 2026-10 发布、尚未成熟。第三方库：纯 Python 无缝、C 扩展（numpy 等）需对应 cp3xx wheel 故滞后；主流大库已支持 3.12-3.14。用户本机 3.13 正合适。

## Q103
- 问题：为何有两个 Python 环境？
- 答复：两个独立解释器安装，非 venv。managed 3.13.12 是 WorkBuddy 自带隔离运行时(C:\Users\...\workbuddy\binaries)，system 3.13.7 是你自己装的(D:\py)。前者供 AI 安全隔离跑代码、不污染系统；二者同属 3.13、标准库一致、site-packages 各自独立；AI 优先用 managed。

## Q104
- 问题：运行时标注的 (managed) 是什么？
- 答复：managed=受管理/托管，是 WorkBuddy 对运行时分类的标签（与 system 相对）。指由 WorkBuddy 自动安装、统一管理(路径/版本/依赖隔离)的 Python，装在隔离目录、预配置安全执行、优先使用；system 是用户自装、作备用。用户无需管理它，正常用 D:\py 学习。

## Q105
- 问题：f.write(response.read().decode(utf-8)) 报 gbk codec cant encode ue687？
- 答复：解码(utf-8)成功，但 open 写文件未指定编码，Windows 中文系统默认 GBK，网页私用区字符  GBK 不支持而崩。修复：open(路径,w,encoding=utf-8)（可加 errors=replace）。网页本身若是 gbk 需换解码。

## Q106
- 问题：爬虫拿到的信息是实时的吗？
- 答复：不是真实时。爬虫=请求那一刻的网页快照(拉取 pull)，页面之后变了文件不会自动更新；看起来实时是因为服务器动态生成、每次请求都返回当下最新。持续更新需轮询(限速防封)或直连 WebSocket/JSON 接口。另注意：urllib 拿的是未执行 JS 的 HTML，JS 动态内容需找接口或用浏览器自动化。

## Q107
- 问题：Web 请求分析是什么？与当前 urllib 爬虫学习何关系？
- 答复：请求分析=用 F12 Network/抓包工具观察每个网络请求(URL/方法/头/体/状态码/响应)。与 urllib 是同一件事两个视角：urllib 亲手发请求、Network 查看请求。它是爬虫进阶必备：找 JS 动态数据的 JSON 接口、补反爬缺的 User-Agent/Cookie、查响应编码。当前阶段先记住概念，遇动态页再实战。

## Q108
- 问题：网页源代码中的搜索功能怎么实现？
- 答复：是浏览器自带页面内查找(Ctrl+F / Cmd+F)，非网页实现；它搜索当前标签页所有文本，view-source 下搜的就是 HTML 源码；6/112 表示第 6 个共 112 处匹配。爬虫里可用 str/re/BeautifulSoup 做代码级搜索。

## Q109
- 问题：教程 Network 有很多请求，我的 name 等列为空白？
- 答复：多为 DevTools 未开启录制或打开后未刷新。标准步骤：F12 -> Network -> 确认左上角红点录制中 -> Ctrl+R 刷新。也可能 Filter/类型筛选或列被隐藏导致。

## Q110
- 问题：如何把 python-mini-projects-master 排除在提交外？
- 答复：在项目根目录 .gitignore 里加 `python-mini-projects-master/`。若已提交过，先 `git rm -r --cached python-mini-projects-master` 移除索引再提交；.gitignore 本身也要提交。

## Q111
- 问题：截图中服务器渲染和客户端渲染是什么意思？
- 答复：SSR=服务器把数据拼进 HTML 一起返回，源码里有数据，直接爬 HTML 即可；CSR=服务器先返回空骨架，浏览器再执行 JS 去接口拉数据填页面，源码里没数据，需找 JSON 接口或用浏览器自动化。判断：view-source 里搜关键词，搜到是 SSR，搜不到是 CSR。

## Q112
- 问题：from urllib.request import urlopen 是什么意思？
- 答复：导入标准库 urllib 下 request 子模块的 urlopen 函数到当前作用域。urllib=网络URL操作标准库；request=请求子模块；urlopen=发请求并打开URL的函数。等价写法 import urllib.request 后需写 urllib.request.urlopen(url)。from 写法调用更简洁。

## Q113
- 问题：cookie 是什么？
- 答复：服务器发给浏览器的文本数据，浏览器存本地、之后每次请求自动带回，用来在无状态的 HTTP 上维持状态(登录/购物车/追踪)。流程：服务器 Set-Cookie -> 浏览器存 -> 后续请求自动带 Cookie。与 login_flag 思路同(保存状态位)，但存在浏览器(客户端)而非程序内存。爬虫里用于模拟登录态、过反爬(urllib 用 Request.add_header(Cookie) 或 cookiejar)。

## Q114
- 问题：为什么 Network 里 Request Headers 显示 Provisional headers are shown？
- 答复：因为该资源被浏览器本地缓存命中，未真正发网络请求，只能展示临时头。解决：勾选 Network 顶部的 Disable cache，再刷新页面即可看完整 Request Headers。爬虫模拟请求时应以禁用缓存后的完整头为准。

## Q115
- 问题：解释截图 Request Headers 每一行含义。
- 答复：以 `:` 开头的是 HTTP/2 伪头（authority=目标主机、method=GET、path=资源路径、scheme=https）。常规头 Accept 表示接受类型、Accept-Encoding 支持压缩、Accept-Language 语言偏好、Cache-Control/Pragma 控制缓存、Referer 来源页、Sec-Ch-* 客户端信息、Sec-Fetch-* 请求上下文、User-Agent 浏览器身份。爬虫里最常模拟 User-Agent 和 Referer。

## Q116
- 问题：解释 General 和 Response headers 每一行含义。
- 答复：General 显示请求 URL、GET 方法、状态码 200 OK、服务器 IP:443、Referrer Policy。Response headers 是服务器返回的元信息：Accept-Ranges 支持断点、Age 缓存时长、Cache-Control 缓存策略、Content-Encoding 压缩方式(br)、Content-Type 文件类型、Date/Expires/Last-Modified 时间、Ohc-* 豆瓣 CDN 自定义头、Via 代理链路、X-Cache-Status:HIT 缓存命中、X-Request-Id 链路追踪 ID。爬虫重点关注 Status Code 和 Content-Type。

## Q117
- 问题：API、缓存命中、CDN 分别是什么？
- 答复：API=程序间沟通的接口(URL+参数+返回JSON)，爬虫常直接调它拿数据；缓存命中=要的数据已在缓存直接取、不必回源(X-Cache-Status:HIT，反义 Miss)；CDN=把内容复制到各地边缘节点让用户就近访问(如 img1.doubanio.com、Via 杭州节点)。三者串：调 API->放 CDN->就近取->命中则直接返回。

## Q118
- 问题：pip install requests 装到哪？
- 答复：装到当前 pip 关联的 Python 解释器的 site-packages 目录。具体位置取决于执行 pip 时用的是哪个 Python（PyCharm 终端默认用项目配置的解释器）。不同终端/环境 site-packages 独立，建议用 `python -m pip install xxx` 确保装对位置，避免 ModuleNotFoundError。


- Q119：URL 编码 = UTF-8 字节的 %XX 表示，中文必须转义才能放进 URL；`unquote()` 反解。


- Q120：浏览器地址栏粘贴带 `%` 编码的 URL 可能被当成搜索词（默认搜索引擎=百度），加 `https://` 协议头可避免；Python 爬虫不受影响。


- Q121：用户在 PyCharm 跑 sogou 代码，但浏览器看到的不是 sogou 而是 `localhost:63342/.../my_baidu.html`（PyCharm 内置服务器打开的百度首页离线副本）。判断页面真伪看地址栏：本地文件 ≠ 真实网络请求。


- Q122：PyCharm 对 HTML 文件点"Open in Browser"会启动内置 HTTP 服务器（63342 端口）预览本地文件，与运行 Python 代码无关；想看代码结果要 Run .py 文件看控制台。
