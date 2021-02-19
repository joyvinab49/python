"""keywords"""

"""with x as y: pass"""
"""https://blog.csdn.net/qiqicos/article/details/79200089"""
"""跟 类 及 文档打开 有关"""

"""with 表达式 [as target]：
    代码块"""

"""此格式中 用 [] 括起来的部分可以使用 也可以省略
   其中 target 参数用于指定一个变量 该语句会将 expression 指定的结果保存到该变量中
   with as 语句中的代码块如果不想执行任何语句 可以直接使用 pass 语句代替"""

"""with…as语句执行顺序：
–>首先执行expression里面的__enter__函数 它的返回值会赋给as后面的variable
  想让它返回什么就返回什么 只要你知道怎么处理就可以了 如果不写as variable 返回值会被忽略

–>然后 开始执行with-block中的语句 不论成功失败(比如发生异常、错误，设置sys.exit())
  在with-block执行完成后 会执行expression中的__exit__函数

当with...as语句中with-block被执行或者终止后 这个类对象应该做什么:
如果这个码块执行成功 则exception_type,exception_val, trace的输入值都是null
如果码块出错了 就会变成像try/except/finally语句一样 exception_type exception_val trace 这三个值系统会分配值"""

# 程序无错的例子


class sample1(object):
    def __enter__(self):  # 第一个参数永远是创建的实例本身
        print("In __enter__")
        return "Hiii"

    def __exit__(self, type, val, trace):
        print("In__exit__")


def get_sample():
    return sample1()


with get_sample() as a1:
    print("a1: ", a1)

print(sample1)  # 表示类本身 <class '__main__.sample1'>
print(sample1())  # 表示创建了一个匿名实例对象 <__main__.sample1 object at 0x0000026C516BE6A0>

"""使用 with as 操作已经打开的文件对象（本身就是上下文管理器）
   无论期间是否抛出异常 都能保证 with as 语句执行完毕后自动关闭已经打开的文件"""
with open("15 reading files sample.txt") as f:  # 这行代码结束后文档已经被关闭
    print(f.read())  # f.read()就会读出文档内的内容


"""assert False, 'Error!'"""
"""assert condition [,arguments]"""
"""arguments用来解释断言并更好的知道是哪里出了问题"""
"""https://www.cnblogs.com/hezhiyao/p/7805278.html"""
"""https://www.cnblogs.com/shangren/p/8038935.html"""

"""用来让程序测试这个condition
   如果condition为false 那么raise一个AssertionError出来
   逻辑上等同于：

if not condition:
    raise AssertionError()"""
assert 1 == 1, '1不等于1'
"""assert 10 < 8, '10不小于8' # 这里报错了 后面不运行哎"""
assert 'abd' != 'ds'


"""except ValueError as e:print(e)"""
"""https://blog.csdn.net/weixin_45494811/article/details/104216997"""
"""python的异常处理类型"""
"""https://www.runoob.com/python/python-exceptions.html"""
a = [1, 2, 3]
try:
    a[4]
    print("hihihi")  # 这个不会被执行
# 如果不确定异常类型 可以except后什么都不写
except Exception as e:  # 捕捉所有异常 这种情况适合不知道异常具体类型 但是又想存储打印异常类型
    print('错误类型是', e.__class__.__name__)
    print('错误明细是', e)
print("byebyebye")  # 这个能够被执行
"""可以像if条件句一样最后加上else 这是不报错的时候会执行的"""


"""exec 'print("hello")'"""
"""exec 执行储存在字符串或文件中的Python语句"""
"""https://www.runoob.com/python/python-func-exec.html"""


"""finally: pass"""
"""在程序中 如果一个段代码必须要执行
   即无论异常是否产生都要执行 那么此时就需要使用finally"""
"""注意try..finally的使用 可以没有except
   只有try...except... try...except...finally这三种用法"""
"""https://blog.csdn.net/qq_26442553/article/details/81780004"""
try:
    print(8 / 0)
except Exception as e:
    print('错误类型是', e.__class__.__name__)
    print('错误明细是', e)
finally:
    print("it MUST show")


"""s = lambda y: y ** y; s(3)"""
"""lambda作为一个表达式 定义了一个匿名函数"""
"""上例的代码y为入口参数 y**y为函数体
   用函数来表示为：
    def s(y):
        return y**y
    s(3)"""
"""https://www.cnblogs.com/evening/archive/2012/03/29/2423554.html"""
"""lambda并不会带来程序运行效率的提高 只会使代码更简洁"""


"""def empty(): pass"""
"""pass 是空语句 是为了保持程序结构的完整性"""
"""pass 不做任何事情 一般用做占位语句"""
"""即 写上了pass在运行的时候也不会显示"""
"""https://www.runoob.com/python/python-pass-statement.html"""


"""raise ValueError("No")"""
"""raise [exceptionName [(reason)]]"""
"""用 [] 括起来的为可选参数 其作用是指定抛出的异常名称 以及 异常信息的相关描述
   如果可选参数全部省略 则 raise 会把当前错误原样抛出
   如果仅省略 (reason) 则在抛出异常时 将不附带任何的异常描述信息"""
"""http://c.biancheng.net/view/2360.html"""

"""也就是说，raise 语句有如下三种常用的用法：
raise：单独一个 raise 该语句引发当前上下文中捕获的异常（比如在 except 块中） 或默认引发 RuntimeError 异常
raise 异常类名称：raise 后带一个异常类名称 表示引发执行类型的异常
raise 异常类名称(描述信息)：在引发指定类型的异常的同时 附带异常的描述信息"""
"""raise 语句引发的异常通常用 try except（else finally）异常处理结构来捕获并进行处理"""
try:
    a = input("number: ")
    if(not a.isdigit()):
        raise ValueError("a must be a number")
except ValueError as e:
    print("cause error: ", repr(e))


"""def x(): yield y; x().next()"""
"""带yield的函数是生成器generator"""
"""https://blog.csdn.net/mieleizhi0522/article/details/82142856/"""


def test(a):
    print("let's start it")
    while True:
        a = a + 1
        yield a
        print(a)


on_test = test(5)  # 这里不会执行test(5) 而是得到一个生成器on_test 相当于一个对象
print(next(on_test))  # 这里开始执行test函数 执行碰到 yield 停下
print("==============")  # 所以双横线前只有一个 6
print(next(on_test))  # 再次有next 从 yield 那里开始执行 print(a) 再返回循环a=a+1


def ts():
    print("come on")
    while True:
        res = yield 5
        print("res: ", res)


g = ts()  # 不执行ts() 生成一个生成器g
print(next(g))  # 开始运行ts() 碰到 yield 停下 输出5 但是没有赋值给res
print("------------")
print(next(g))  # 从刚才停下的地方继续运行 对res进行赋值 但因为刚才将5传出去了 所以右边没有值
# 于是得到的就是 res: None
# 重新返回循环 得到5
print("------------")
print(g.send(20))  # 从刚才停下的地方继续运行 send会将20赋值给res
# 由于send方法中包含next()方法 所以程序会继续向下运行执行print方法 然后再次进入while循环
# 程序执行再次遇到yield关键字 yield会返回后面的值后 程序再次暂停 直到再次调用next方法或send方法


"""Old style string formats"""
"""https://blog.csdn.net/qq_29720657/article/details/102771436"""
"""%s 通过str()字符串转换来格式化"""
"""%u 无符号的十进制整数"""
"""%d 有符号的十进制整数"""
