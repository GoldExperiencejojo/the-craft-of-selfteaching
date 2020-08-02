## 操作符
### 数值操作符

| 数值操作符 | 意义     | 示例   | 结果   |
| ---------- | -------- | ------ | ------ |
| `//`       | 整除运算 | 5 // 2 | 2(int) |
| `**`       | 幂运算   | 5 ** 2 | 25     |

补充：

> 除法：
>
> 除法运算 (`/`) 永远返回浮点数类型。如果要做 [floor division](https://docs.python.org/zh-cn/3/glossary.html#term-floor-division) 得到一个整数结果（忽略小数部分）你可以使用 `//` 运算符；如果要计算余数，可以使用 `%`。
>
> > floor division -- 向下取整除法
> >
> > 向下舍入到最接近的整数的数学除法。向下取整除法的运算符是 `//` 。例如，表达式 `11 // 4` 的计算结果是 `2` ，而与之相反的是浮点数的真正除法返回 `2.75` 。注意 `(-11) // 4` 会返回 `-3` 因为这是 `-2.75` *向下* 舍入得到的结果。

> 幂运算符：
>
> **幂运算符的绑定比在其左侧的一元运算符更紧密；但绑定紧密程度不及在其右侧的一元运算符。**
>
> 因此，在一个未加圆括号的幂运算符和单目运算符序列中，**运算符将从右向左求值**（这不会限制操作数的求值顺序）: `-1**2` 结果将为 `-1`。
>
> 幂运算符与附带两个参数调用内置 [`pow()`](https://docs.python.org/zh-cn/3/library/functions.html#pow) 函数具有相同的语义：**结果为对其左参数进行其右参数所指定幂次的乘方运算。 数值参数会先转换为相同类型，结果也为转换后的类型**
>
> 对于 int 类型的操作数，结果将具有与操作数相同的类型，**除非第二个参数为负数；在那种情况下，所有参数会被转换为 float 类型并输出 float 类型的结果**。 例如，`10**2` 返回 `100`，而 `10**-2` 返回 `0.01`。
>
> 对 `0.0` 进行负数幂次运算将导致 [`ZeroDivisionError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ZeroDivisionError)。 **对负数进行分数幂次运算将返回 [`complex`](https://docs.python.org/zh-cn/3/library/functions.html#complex) 数值。** （在早期版本中这将引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError)。）




### 逻辑操作符

| 比较操作符 | 意义     | 示例             | 布尔值  |
| ---------- | -------- | ---------------- | ------- |
| `==`       | 等于     | `1 == 2`         | `False` |
| `!=`       | 不等于   | `1 != 2`         | `True`  |
| `>`        | 大于     | `1 > 2`          | `False` |
| `>=`       | 大于等于 | `1 >= 1`         | `True`  |
| `<`        | 小于     | `1 < 2`          | `True`  |
| `<=`       | 小于等于 | `1 <= 2`         | `True`  |
| `in`       | 属于     | `'a' in 'basic'` | `True`  |

除了等于、大于、小于之外，Python 还有一个逻辑操作符，`in`：

这个表达式 `'a' in 'basic'` 用自然语言描述就是：

> “`'a'` 存在于 `'basic'` 这个字符串之中吗？”（属于关系）
>
> 可以理解为python中内置了**字符串匹配**功能




### 布尔运算操作符

|            | 与   | 或   | 非   |
| :--------- | ---- | ---- | ---- |
| 操作符表示 | &    | \|   | ^    |
| 关键字表示 | and  | or   | not  |



### 字符串操作符

针对字符串，有三种操作：

> - 拼接：`+` 和 `' '`（后者是空格）
> - 拷贝：`*`
> - 逻辑运算：`in`、`not in`；以及，`<`、`<=`、`>`、`>=`、`!=`、`==` 

```python
'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'ome' in 'Awesome'
```
'AwesomePython'
'AwesomePython'
'Python, Awesome! Awesome! Awesome! '
True

当字符串被比较的时候，将从两个字符串各自的第一个字符开始逐个比较(**Unicodo码**)，“**一旦决出胜负马上停止**”：

```
>>> 'PYTHON' > 'Python 3'
False
```



### 列表的操作符

跟字符串的操作符相同，因为字符和列表都属于容器。

> - 拼接：`+` 和 `' '`（后者是空格）
> - 拷贝：`*`
> - 逻辑运算：`in`、`not in`；以及，`<`、`<=`、`>`、`>=`、`!=`、`==`

> 列表就是数组，python将数组的拼接，拷贝及逻辑运算都做成了内置的功能，可以通过运算符来使用。



## 流程控制

### if

> - 在python中，不能写`else if`，只能写简写形式`elif`。
> - 没有switch语句，用`if  elif`代替。



### for / while

#### range()函数：

> 返回一个range对象
>
> [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 类型表示不可变的数字序列，通常用于在 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中循环指定的次数。
>
> *class* `range`(*start*, *stop*[, *step*])
>
> range 构造器的参数必须为整数（可以是内置的 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 或任何实现了 `__index__` 特殊方法的对象）。 如果省略 *step* 参数，其默认值为 `1`。 如果省略 *start* 参数，其默认值为 `0`。
>
> 如果 *step* 为正值，确定 range `r` 内容的公式为 `r[i] = start + step*i` 其中 `i >= 0` 且 `r[i] < stop`。
>
> 如果 *step* 为负值，确定 range 内容的公式仍然为 `r[i] = start + step*i`，但限制条件改为 `i >= 0` 且 `r[i] > stop`.

#### 循环中的else语句

> 循环语句可能带有 `else` 子句；它会在循环耗尽了可迭代对象 (使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for)) 或循环条件变为假值 (使用 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while)) 时被执行，但不会在循环被 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break) 语句终止时被执行。

#### pass语句

> [`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它。
>
> [`pass`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#pass) 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考。 `pass` 会被静默地忽略.。
>
> 比如在设计类或者函数时，可以不写具体的而用`pass`代替。



## 函数

本章需要（大致）了解的重点如下，其实很简单：

> * 你可以把函数当作一个产品，而你自己是这个产品的用户；
> * 既然你是产品的用户，你要养成好习惯，一定要亲自阅读产品说明书；
> * 调用函数的时候，注意*可选位置参数的使用方法*和*关键字参数的默认值*；
> * 函数定义部分，注意两个符号就行了，`[]` 和 `=`；
> * 所有的函数都有返回值，即便它内部不指定返回值，也有一个默认返回值：`None`；
> * 另外，一定要耐心阅读该函数在使用的时候需要注意什么 —— 产品说明书的主要作用就在这里……

知道这些就很好了！

这就好像你拿着一张地图，不可能一下子掌握其中所有的细节，但花几分钟搞清楚 “图例”（Legend）部分总是可以的，知道什么样的线标示的是公交车，什么样的线标示的是地铁，什么样的线标示的是桥梁，然后知道上北下南左西右东 —— 这之后，就可以开始慢慢研究地图了……

> 用一个函数之前一定要去阅读**官方**的”说明书“



## 字符串

![](..\images\string-concept-table.png)

| 搜索 | s.count()    | s..find()      | s.rfind() | s.index() | s.rindex() | s.startswith() |
| ---- | ------------ | -------------- | --------- | --------- | ---------- | -------------- |
|      | s.endswith() | `in`           |           |           |            |                |
| 替换 | s.replace()  | s.expandtabs() |           |           |            |                |

补充：

> - `''' / """`既可以标识字符串，又可以作为注释。
> - 切片
>
> >“提取” 的动作有个专门的术语，叫做 “Slicing”（切片）。索引操作符 `[]` 中可以有一个、两个或者三个整数参数，如果有两个参数，需要用 `:` 隔开。它最终可以写成以下 4 种形式：
>
> >  `s[index]` —— 返回索引值为 `index` 的那个字符
> >  `s[start:]` —— 返回从索引值为 `start` 开始一直到字符串末尾的所有字符
> >  `s[start:stop]` —— 返回从索引值为 `start` 开始一直到索引值为 `stop` 的那个字符*之前*的所有字符
> >  `s[:stop]` —— 返回从字符串开头一直到索引值为 `stop` 的那个字符*之前*的所有字符
> >  `s[start:stop:step]` —— 返回从索引值为 `start` 开始一直到索引值为 `stop` 的那个字符*之前*的，以 `step` 为步长提取的所有字符
>
> - 字符串是 str 类（`Class str`）的对象。
> - 关于`' '`(空格)表示拼接字符串
>
> > 作为单一表达式组成部分，之间只由空格分隔的多个字符串字面值会被隐式地转换为单个字符串字面值。 也就是说，`("spam " "eggs") == "spam eggs"`。
>
> - 为了找到位置而进行搜索之前，你可能经常需要事先确认需要寻找的字符串在寻找对象中是否存在，这个时候，可以先用 `in` 操作符确认
>
> - str.format()
>
> >  在一个字符串中，插入一个或者多个占位符 —— 用大括号 `{}` 括起来；
> >  而后将 `str.format()` 相应的参数，依次插入占位符中；
> >  两个连续使用的大括号，不被认为是占位符；且只打印出一对大括号。



## 数值的计算

| 名称         | 操作           | 结果 | 官方文档链接                                                 |
| ------------ | -------------- | ---- | ------------------------------------------------------------ |
| 加           | `1 + 2`        | 3    |                                                              |
| 减           | `2 - 1`        | 1    |                                                              |
| 乘           | `3 * 5`        | 15   |                                                              |
| 除           | `6 / 2`        | 3.0  |                                                              |
| 商           | `7 // 3`       | 2    |                                                              |
| 余           | `7 % 3`        | 1    |                                                              |
| 负           | `-6`           | -6   |                                                              |
| 正           | `+6`           | 6    |                                                              |
| 绝对值       | `abs(-1)`      | 1    | [`abs()`](https://docs.python.org/3/library/functions.html#abs) |
| 转换为整数   | `int(3.14)`    | 3    | [`int()`](https://docs.python.org/3/library/functions.html#int) |
| 转换为浮点数 | `float(3)`     | 3.0  | [`float()`](https://docs.python.org/3/library/functions.html#float) |
| 商余         | `divmod(7, 3)` | 2, 1 | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) |
| 幂           | `pow(2, 10)`   | 1024 | [`pow()`](https://docs.python.org/3/library/functions.html#pow) |
| 幂           | `3 ** 2`       | 9    |                                                              |



## 数据容器

<img src="../images/python-containers-final.png" style="zoom:150%;" />

### 列表

#### 列表的生成

*class* `list`([*iterable*])

可以用多种方式构建列表：

- 使用一对方括号来表示空列表: `[]`
- 使用方括号，其中的项以逗号分隔: `[a]`, `[a, b, c]`
- 使用列表推导式: `[x for x in iterable]`
- 使用类型的构造器: `list()` 或 `list(iterable)`

> #### 列表推导式
>
> 例：创建一个平方列表
>
> ```
> squares = [x**2 for x in  range(10)]
> ```
>
> > 列表推导式提供了一个更简单的创建列表的方法。常见的用法是把**某种操作**(x* *2)应用于**序列或可迭代对象**(range(10))的每个元素上，然后使用其结果来创建**列表**(squares)，或者通过满足某些**特定条件**(if语句)元素来创建子序列。
>
> **结构**
>
> > 列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个 `for` 子句，然后是零个或多个 `for` 或 `if` 子句。 其结果将是一个新列表，由对表达式依据后面的 `for` 和 `if` 子句的内容进行求值计算而得出。
>
> 例：
>
> ```
> >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
> ```
>
> 等价于
>
> ```
> >>> combs = []
> >>> for x in [1,2,3]:
> ...     for y in [3,1,4]:
> ...         if x != y:
> ...             combs.append((x, y))
> ...
> >>> combs
> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
> ```
>
> ---
> ```
> >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
> >>> [num for elem in vec for num in elem]
> [1, 2, 3, 4, 5, 6, 7, 8, 9]
> ```
>
> 等价于
>
> ```
> vec = [[1,2,3], [4,5,6], [7,8,9]]
> num = []
> for elem in vec:
> 	for num_ in elem:
> 		num.append(num_)
> ```
>
> > 不熟练时可以将列表推导式转化为上述代码来理解

![](../images/list-concepts.png)



### 元组




## 其他

### 语句块

在python中，如果有行首空白存在，那么，Python 将认为**这一行与其他邻近有着相同行首空白的语句同属于一个语句块** —— 而一个语句块必然由一个行末带有冒号 `:` 的语句起始。**同属于一个语句块中的语句，行首空白数量应该相等**。在其他语言中通常使用` {} `作为语句块标识，这是python比较特殊的地方。

![](..\images\python-leading-space.png)



### 注释

2种注释方法

1. 单行注释`#`
2. 多行注释`'''`

示例：

```python
# 单行注释
'''
	多行注释
'''
```



### 值

#### 类型转换

运算的默认法则：通常情况下应该是*相同类型的值才能相互运算*。

类型转换：

> - 将字符串转换为数字用 `int()`、`float()`；
> - 将数字转换成字符串用 `str()`；

另外，即便是在数字之间进行计算的时候，有时也需要将整数转换成浮点数字，或者反之：

> - 将整数转换成浮点数字用 `float()`；
> - 将浮点数字转换成整数用 `int()`；



#### 逻辑值检测

> 逻辑值检测
>
> 任何对象都可以进行逻辑值的检测，以便在 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 作为条件或是作为下文所述布尔运算的操作数来使用。
>
> **一个对象在默认情况下均被视为真值**，除非当该对象被调用时其所属类定义了 [`__bool__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__bool__) 方法且返回 `False` 或是定义了 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__) 方法且返回零。下面基本完整地列出了会被视为假值的内置对象:
>
> - 被定义为假值的常量: `None` 和 `False`。
>- 任何数值类型的零: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
> - 空的序列和多项集: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`
> 
> 产生布尔值结果的运算和内置函数总是返回 `0` 或 `False` 作为假值，`1` 或 `True` 作为真值，除非另行说明。 （重要例外：布尔运算 `or` 和 `and` 总是返回其中一个操作数。）
>
> > **每个变量或者常量，除了它们的值之外，同时还相当于有一个对应的布尔值。**



### 负索引

> s[i]：s的第i项。
>
> > 如果 *i* 或 *j* 为负值，则索引顺序是相对于序列 *s* 的末尾: 索引号会被替换为 `len(s) + i` 或 `len(s) + j`。 但要注意 `-0` 仍然为 `0`。