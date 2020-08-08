

## 关于参数(上)

#### python关键字

| -       | Python  | Keyword    | List    | -          |
| ------- | ------- | ---------- | ------- | ---------- |
| `and`   | `as`    | `assert`   | `async` | `await`    |
| `break` | `class` | `continue` | `def`   | `del`      |
| `elif`  | `else`  | `except`   | `False` | `finally`  |
| `for`   | `from`  | `global`   | `if`    | `import`   |
| `in`    | `is`    | `lambda`   | `None`  | `nonlocal` |
| `not`   | `or`    | `pass`     | `raise` | `return`   |
| `True`  | `try`   | `while`    | `with`  | `yield`    |

#### 在代码中查询关键字

```
import keyword
keyword.kwlist               # 列出所有关键字
keyword.iskeyword('if')      # 查询某个词是不是关键字
```

#### 函数定义格式

```
def name(参数1, 参数2···):
	pass(内容)
	return 返回值(可以没有)
```

## 关于参数(下)

#### 可以接受一系列值的位置参数

如果你在定义参数的时候，在一个*位置参数*（Positional Arguments）前面标注了星号，`*`，那么，这个位置参数可以接收一系列值，在函数内部可以对这一系列值用 `for ... in ...` 循环进行逐一的处理。

带一个星号的参数，英文名称是 “Arbitrary Positional Arguments”，姑且翻译为 “随意的位置参数”。

例：

```
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')
say_hi()
say_hi('ann')
say_hi('mike', 'john', 'zeo')
```

如果要将一个容器传递给可以接受一系列值的位置参数，就要在参数前加上`*`

```
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

names = ('mike', 'john', 'zeo')
say_hi(*names)
```

#### 有默认值的参数(关键字参数)

> 可以在定义函数的时候，为某些参数设定默认值，这些有默认值的参数，又被称作关键字参数（Keyword Arguments）。从这个函数的 “用户” 角度来看，这些设定了默认值的参数，就成了 “可选参数”。

```
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'john', 'zeo')
say_hi('Hello', 'mike', 'john', 'zeo', capitalized=True)
```

```
Hello, mike!
Hello, john!
Hello, zeo!
Hello, Mike!
Hello, John!
Hello, Zeo!
```

#### 可以接受一系列值的关键字参数

> 之前我们看到，可以设定一个位置参数（Positional Argument），接收一系列的值，被称作 “Arbitrary Positional Argument”；
>
> 同样地，我们也可以设定一个可以接收很多值的关键字参数（Arbitrary Keyword Argument）。

```
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
say_hi(mike='Hello', ann='Oh, my darling', john='Hi')
```

```
Hello, mike!
Oh, my darling, ann!
Hi, john!
```

既然在函数内部，我们在处理接收到的 Arbitrary Keyword Argument 时，用的是对字典的迭代方式，那么，在调用函数的时候，也可以直接使用字典的形式：

```
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi(**a_dictionary)
#注意这里如果传入的是字典，就要在前面加上`**`
say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})
```

```
Hello, mike!
Oh, my darling, ann!
Hi, john!
Hello, mike!
Oh, my darling, ann!
Hi, john!
```

#### 函数定义时各种参数的排列顺序

> **Order of Arguments**
> 1. Positional
> 1. Arbitrary Positional
> 1. Keyword
> 1. Arbitrary Keyword



## 化名和匿名

#### 化名

在 Python 中，我们可以给一个函数取个**化名**（alias）。

以下的代码，我们先是定义了一个名为 `_is_leap` 的函数，而后为它另取了一个化名：

```
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_leap_bool = _is_leap
year_leap_bool              #<function __main__._is_leap(year)>
year_leap_bool(800)         # _is_leap(800) -> True

id(year_leap_bool)          # id() 这个函数可以查询某对象的内存地址
id(_is_leap)                # year_leap_bool 和 _is_leap 其实保存在同一个地址中，也就是说，它们是同一个对象。

type(year_leap_bool)
type(_is_leap)              # 它们都是 function
```

```
<function __main__._is_leap(year)>
True
2202871385256
2202871385256
function
function
```



#### lambda

lambda 的语法结构如下：

> ```
> lambda_expr ::= "lambda" [parameter_list] ":" expression
> ```

以上使用的是 BNF 标注。当然，BNF 是你目前并不熟悉的，所以，有疑惑别当回事。

反正你已经见到示例了：

```python
lambda x, y: x + y
```

先写上 `lambda` 这个关键字，其后分为两个部分，`:` 之前是参数，之后是表达式；这个表达式的值，就是这个函数的返回值。

> **注意**：`lambda` 语句中，`:` 之后有且只能有一个表达式。

而这个函数呢，没有名字，所以被称为 “匿名函数”。

```
add = lambda x, y: x + y
```

就相当于是给一个没有名字的函数取了个名字。



## 递归函数

#### 递归三原则

> 1. 根据定义，递归函数必须在内部调用自己；
> 2. 必须设定一个退出条件；
> 3. 递归过程中必须能够逐步达到退出条件……



## 函数的文档

> 你在调用函数的时候，你像是函数这个产品的用户。
>
> 而你写一个函数，像是做一个产品，这个产品将来可能会被很多用户使用 —— 包括你自己。
>
> 产品，就应该有产品说明书，别人用得着，你自己也用得着 —— 很久之后的你，很可能把当初的各种来龙去脉忘得一干二净，所以也同样需要产品说明书，别看那产品曾经是你自己设计的。

#### Docstring

在函数定义内部，我们可以加上 **Docstring**；将来函数的 “用户” 就可以通过 `help()` 这个内建函数，或者 `.__doc__` 这个 Method 去查看这个 Docstring，即，该函数的 “产品说明书”。

```
def is_prime(n):
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True


help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```

```
Help on function is_prime in module __main__:

is_prime(n)
    Return a boolean value based upon
    whether the argument n is a prime number.


    Return a boolean value based upon
    whether the argument n is a prime number.
    
'\n    Return a boolean value based upon\n    whether the argument n is a prime number.\n    '
```



## 保存在文件的函数

> 写好的函数，当然最好保存起来，以便将来随时调用。

#### 模块

> 写好的函数可以单独放在一个.py文件当中，—— 这样可以被外部调用的 `.py` 文件，有个专门的称呼，**模块**（Module）。而后，我们就可以在其它地方用import导入使用。



#### 模块文件系统目录检索顺序

当你向 Python 说 `import ...` 的时候，它要去寻找你所指定的文件，那个文件应该是 `import` 语句后面引用的名称，再加上 `.py` 构成的名字的文件。Python 会按照以下顺序去寻找：

> - 先去看看内建模块里有没有你所指定的名称；
> - 如果没有，那么就按照 `sys.path` 所返回的目录列表顺序去找。

你可以通过以下代码查看你自己当前机器的 `sys.path`：

```
import sys
sys.path
```



#### 引入指定模块中的特定函数

可以用以下方式只导入自己需要的函数

```
from mycode import is_prime
is_prime()
```

注意这里在函数调用时不用写mycode.is_prime()，而是直接写函数名就可以调用。

用`import mycode`时，虽然相当于向前工作空间引入了 `mycode` 文件中定义的所有函数，但是要**写模块名才能调用函数**。

```
from mycode import *
```

用这种方式可以直接写函数名进行调用。

注意，如果当前目录中并没有 `mycode.py` 这个文件，那么，`mycode` 会被当作目录名再被尝试一次 —— 如果当前目录内，有个叫做 `mycode` 的目录（或称文件夹）且该目录下同时要存在一个 [`__init__.py`](https://docs.python.org/3/reference/import.html#regular-packages) 文件（通常为空文件，用于标识本目录形成一个包含多个模块的 **包**（[packages](https://docs.python.org/3/reference/import.html#regular-packages)），它们处在一个独立的 **命名空间**（[namespace](https://docs.python.org/3/glossary.html#term-namespace-package)）），那么，`from mycode import *` 的作用就是把 `mycode` 这个文件夹中的所有 `.py` 文件全部导入……

如果我们想要导入 `foo` 这个目录中的 `bar.py` 这个模块文件，那么，可以这么写：

```python
import foo.bar
```

或者

```python
from foo import bar
```



## 测试驱动的开发

> 在写程序的过程中，为别人（和将来的自己）写注释、写 Docstring；在写程序的过程中，为了保障程序的结果全面正确而写测试；或者干脆在最初写的时候就考虑到各种意外所以使用试错语句块 —— 这些明明是天经地义的事情，却是绝大多数人不做的…… 因为感觉有点麻烦。



## 可执行的 Python 文件

当一个模块（其实就是存有 Python 代码的 `.py` 文件，例如：`mycode.py`）**被 `import` 语句导入的时候，这个模块的 `__name__` 就是模块名**（例如：`'mycode'`）。

而当一个模块**被命令行运行的时候，这个模块的 `__name__` 就被 Python 解释器设定为 `'__main__'`**。

把一个程序整个封装到 `main()` 之中，而后在模块代码里加上：

```python
#这个模块被直接运行时才会执行main()函数，而被调用时不会
if __name__ == '__main__':
    main()
```

这么做的结果是：

> 1. 当 Python 文件被当作模块，被 `import` 语句导入时，`if` 判断失败，`main()` 函数不被执行；
> 2. 当 Python 文件被 `python -m` 运行的时候，`if` 判断成功，`main()` 函数才被执行。

```
import this
bool(love)
love = this
this is love                            # True
love == True                            # False
love is False                           # False
love is not True or False               # True
love is not True or False; love is love # True True
if love:
    print(True)
else:
    print(False)                        #True  
    
if bool(love) == True:
    print(True)
else:
    print(False)						#True
    
if love == True:
    print(True)
else:
    print(False)						#False
```

> 在if的判断条件中，love被转换为bool值来进行判断，相当于bool(love) == True
>
> 而love == True是将love的id与True的id进行比较，自然是不相同
>
> 问题`==`或`is`的判断标准是怎样的？什么时候比较id？