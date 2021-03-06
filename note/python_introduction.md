> [对应代码](https://github.com/zhangxiaoyuan/pythonStudy/blob/master/src/hello_test_in_study.py)

#### 1.python基础库：
  * Python就为我们提供了非常完善的基础代码库，覆盖了网络、文件、GUI、数据库、文本等大量内容
  
#### 2.python定位：
  * '优雅' '明确' '简单'
  * Python的哲学就是简单优雅，尽量写容易看明白的代码，尽量写少的代码
  
#### 3.python应用场景：
  * 首选是网络应用，包括网站、后台服务等等；
  * 其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；
  * 另外就是把其他语言开发的程序再包装起来，方便使用。 
  
#### 4.python缺点：
  * 第一个缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言，你的代码在执行时会一行一行地翻译成CPU能理解的机器码，这个翻译过程非常耗时，所以很慢。而C程序是运行前直接编译成CPU能执行的机器码，所以非常快。
  * 第二个缺点就是代码不能加密。如果要发布你的Python程序，实际上就是发布源代码，而解释型的语言，则必须把源码发布出去。
  
#### 5.pyhton数据类型：

 > 这种变量本身类型不固定的语言称之为动态语言:
 
 - **整数**：整数永远是精确的，除法都是精确的，整数除法有两种方式：1.'a/b'表示普通除法，结果是浮点数；2.'a//b'表示地板除，结果是四舍五入的整数   
 - **浮点数**：浮点数运算则可能会有四舍五入的误差   
 - **字符串**：字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等，如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容    
 - **布尔值**：布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值   
 - **空值**：空值是Python里一个特殊的值，用None表示   
 - **常量**：所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量   
 - **集合list**：list是一个可变的有序表。 len()可以获取list的个数，获取最后一个元素可以用'-1'下标，如list[-1],依次可以用-2.-3往前推获取元素   
 - **元祖tuple**：tuple和list非常类似，但是tuple一旦初始化就不能修改，另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义   
 - **字典dict**：dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度,dict内部存放的顺序和key放入的顺序是没有关系,dict的key必须是不可变对象   
 - **set**: set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key.要创建一个set，需要提供一个list或tuple作为输入集合,重复元素在set中自动被过滤,set可以看成数学意义上的无序和无重复元素的集合   

#### 6.python字符编码:
 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：  
 
 > #!/usr/bin/env python3   
   #-*- coding: utf-8 -*-   
   第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；   
   第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。   

#### 7.python字符格式化：
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好，如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

#### 8.数据类型转换：
int()函数将字符型数字转化为数字，如果是非数字则报错, int('123');也可以将浮点数转化为整数int(3.14154)     
float()函数将字符型数字转化为浮点型数字，float('3.1415')   
str()函数将非字符型转化为字符型, str(123), str(23.345)      
bool()函数其他类型转化为布尔型，bool(1) bool('')     
 
#### 9.函数：
- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”： a = abs  a(-1)      
- 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。      
如果想定义一个什么事也不做的空函数，可以用pass语句,实际上pass可以用来作为占位符   
- **函数可以返回多个返回值**：原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便 

 
 > 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值,也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。 调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数，当不按顺序提供部分默认参数时，需要把参数名写上。
#### 10.函数参数：
- **位置参数**：普通参数，按照传入实参给对应位置上的形参赋值   
- **默认参数**：默认参数可以简化函数的调用，必选参数在前，默认参数在后，否则Python的解释器会报错，当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。**默认参数必须指向不变对象。** **我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。**
- **可变参数**：定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个'\*'号,所以Python允许你在list或tuple前面加一个\*号，把list或tuple的元素变成可变参数传进去，可变参数允许你传入0个或任意个参数，**这些可变参数在函数调用时自动组装为一个tuple**
- **关键字参数**：而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。改变形参不会影响实参，因为形参获取是实参的一份拷贝
- **命名关键字参数**：如果要限制关键字参数的名字，就可以用命名关键字参数，和关键字参数\*\*kw不同，命名关键字参数需要一个特殊分隔符\*，\*后面的参数被视为命名关键字参数,例：def person(name, age, \*, city, job):，如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符\*了.**命名关键字参数必须传入参数名，这和位置参数不同**
- **组合参数**：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
**对于任意函数，都可以通过类似func(\*args, \*\*kw)的形式调用它，无论它的参数是如何定义的**

#### 11.python高级特性：
- **切片slice**：
```python:
 listq = [1,4,5,6,7,8,9,0]
 listp = range(0, 100, 5)
 tupleq1 = (9,8,7,6,5,4,3,2,1)
 print(listq[0:5])
 print(listq[:7])
 print(listq[1:5:2])
 print(listp[-1])
 print(list(listp[-5:-1]))
 print(tupleq1[-3:])
 print(tupleq1[-5:-1:2])
 print(tupleq1[:6:3])
 print(list(listp[::5]))
 print(tupleq1[:])
 print((1,2,3,4,5,6,7,8)[2:5:1])
 print([9,8,7,6,5,4,3,2,1][-8::2])
 print('abcdefghi'[::2])
```

#### 12.列表生成式：
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来  

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

#### 13.生成器：
在Python中，这种一边循环一边计算的机制，称为生成器：generator 
**难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。**
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

```python
 >>> L = [x * x for x in range(10)]
 >>> L
 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 >>> g = (x * x for x in range(10))
 >>> g
 <generator object <genexpr> at 0x1022ef630>
```
这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

```python
 def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

> 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

#### 14.迭代器：
凡是可作用于for循环的对象都是Iterable类型；   

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；   

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。   

Python的for循环本质上就是通过不断调用next()函数实现的，

#### 15.闭包：
```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```
内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力   

每次调用都会返回一个新的函数，即使传入相同的参数
```python
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
```

**返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```

 ***返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。***
 
 #### 15.匿名函数:
 关键字lambda表示匿名函数，冒号前面的x表示函数参数
 
 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
 
 #### 16.装饰器：
 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
 
 本质上，decorator就是一个返回函数的高阶函数
 
 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
 
#### 17.偏函数：
简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
```python
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```

#### 18.类和实例：
注意：特殊方法“init”前后有两个下划线！！！
注意到\__init\__方法的第一个参数永远是self，表示创建的实例本身，因此，在\__init\__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了\__init\__方法，在创建实例的时候，就不能传入空的参数了，必须传入与\__init\__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去

**和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self**,并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线\__，在Python中，实例的变量名如果以\__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

需要注意的是，在Python中，变量名类似\__xxx\__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用\__name\__、\__score\__这样的变量名。

#### 19.继承和多态：
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

```python
class Timer(object):
    def run(self):
        print('Start...')
```     
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

#### 20.对象信息：
首先，我们来判断对象类型，使用type()函数：
断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
```pythons
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```

对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
```python
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(d, Dog) and isinstance(d, Animal)
True
```

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
```python
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
```
紧接着，可以测试该对象的属性：
```python
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
```



#### .尾递归优化：
Python中可以写（尾递归）：尾递归是把变化的参数传递给递归函数的变量了。

```python
  def tailrecsum(x, running_total=0):
   if x == 0:
     return running_total
   else:
     return tailrecsum(x - 1, running_total + x)
     
  def fact(n):
   return tailrecsum(n)
```

#### .[常用函数](https://docs.python.org/3/library/functions.html)：
|  function name                |     description                                                         |
|:------------------------------|------------------------------------------------------------------------:|
|    isinstance()               |     数据类型检查    例：if not isinstance(x, (int, float)):              |
|    range(start, end, step)    |     根据step生成一个start到end-1的list,例： range(1,5,2) [1,3,5]          |
|      dict.values()            |     获取字典中所有value值组成的list 返回结果：dict_values([1, 2, 3])       |
|      dict.items()             |     获取字典中的所有key-value组成list 返回结果：dict_items([('a', 1), ('b', 2), ('c', 3)])　｜
|　 isinstance(value, Iterable) |     判断value是否可迭代，例：isinstance("stringvalue", Iterable) True    |
|   enumerate(list)             |     把一个list变成索引-元素对                                             |
|      os.listdir('.')          |     列出当前路径下所有文件名称                                             |
|      iter()                   |     把list、dict、str等Iterable变成Iterator                               |
| sum()                         |     求和                                                                  |
|    str(),int(),float()        |      类型转换函数   str(123), int('123'), float('123.189')                 |
|    filter()                   |   filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素|
|    sorted()                   |    第二个参数不是排序函数，而是待排序数的操作函数而不是排序规则函数key指定的函数将作用于list的每一个元素上，并跟据key函数返回的结果进行排序 |

