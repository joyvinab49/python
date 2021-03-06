# Review章节
print(1 + " print")
print("print()是输出内容 里面可以是字符串等可以是变量名可以是表达式")
print("让两个print在同一行显示", end=" ")
print("就在同一行了")
print("定义新的变量直接写：变量 = 值\n")

print(3 + " 运算符")
print("加 减 乘 除：+ - * /")
print("除法/：整除会带一位小数点x.0 非整除能除尽会出结果")
print("求余数：%")
print("先除法再求余数 ", 9 / 3 % 2, " 9 / 3 % 2等于1")
print("大于(等于)、小于(等于)返回True/False\n")

print(4 + " 变量名")
print("变量命名规则跟js那些一样啦 不过好像更喜欢用_")
print("比如：do_you_love_me\n")

print(5 + " 格式化字符串")
print('f""格式化字符串')
print("在打印的时候能够将大括号{变量/表达式}换成对应的值打印出来")
print("round()能去掉数字后的小数点\n")

print(6 + " 格式化函数")
print("在print里面要用引号的话 区别最外层和内容的引号 单双引号不能重复''")
print(".format()格式化函数")
print('"{} {}".format(value1, value2)')
print("数量可以不限 顺序可以设定 如：{0}{3}{2} 如果不写就默认按顺序")
print('可以在行内设定参数 如："{ok}".format(ok="bad")')
print("可以通过列表索引设定参数")
print('"id:{0[1]}, iq:{0[0]}".format(列表名) "0"不能省略')
my_list = [11, 12, 13]
print("{0[0]},{0[1]}".format(my_list))  # 这个拿到的是里面的数字
my_list2 = [11, 12, 13], [21, 22, 23]
print("{0[0]},{0[1]}".format(my_list2))  # 这个拿到的是列表[]
print("还可以对数字进行格式化")
print('"{:.2f}".format(数字) 保留2位小数')
print('"{:+.2f}".format(数字) 带符号（+/-）保留2位小数\n')

print(7 + " 字符串运算")
print("字符串不能直接和数字相加 报错")
print("两个字符串数字相加就是写在一起而已")
print("字符串*数字x 相当于字符串出现x次\n")

print(8)
print(".format()格式化函数和{}不写在一起 就可以多次赋值使用\n")

print(9)
print("\\n是换行符")
print('"""三行单/双引号"""可以里面写多行内容\n')

print(10 + " 反斜杠")
print("Escape Sequences")
print("\\\两个\会显示一个反斜杠\\")
print("如果要写单双引号也可以用：\\'", '和 \\"')
print("\\a运行到的时候会有铃响")
print("\\b会删除反斜杠前的一个字符 如果写在字符串最后则不起作用")
print("\\r将光标移动到那一行开始的地方")
print("如果\\r前面后面都有内容 后面的len大于/小于前面的 会将前面的完全/不完全覆盖掉")
print("所以一般\\n和\\r一起用")
print("\\t水平制表符 等于Tab键 它后面的第一个字符是在该行的第8*n列")
print("\\v垂直制表符 在反斜杠前字符x的下一行开始输出 且在x所在列的后一列\n")

print(11 + " 正数和浮点数")
print("int()是整数型")
print("float()是浮点数型 有小数点")
print("float(True) == 1.0")
print("float(False) == 0.0")
print("int和float可以互相转换")
print("input()输入的数字是字符串类型的\n")

print(13 + " 引用模板")
# https://blog.csdn.net/qq_30815237/article/details/93203934
print("import xxx 导入模块xxx到程序")
print("如果写在代码开头就是全局通用 写在函数里面就只有函数里面能用")
print("from xxx import xx 从模块xxx中引用方法/属性/变量xx")
print("一般用import 如：import math 后面引用如：math.pi")
print("用from xxx import xx 要注意后面自定义的变量名不能和xx一样 不然会被xx覆盖掉")
print("import xxx from* 是引用模块xxx的所有功能/变量 不建议使用")
print("form sys import argv 中 argv是一个字符串列表")
print("定义a,b,c... = argv 在命令行设置相对应的参数")
print("程序的文件名永远是argv列表的第一个参数")
print("参数之间用空格隔开 类型都是字符串\n")

print(15 + " 文件的函数")
# https://www.runoob.com/python/file-methods.html
print("打开文件 open(filename,mode='r')")
print("mode不写默认为r 即只读模式")
print("当mode = 'w'时 意为只写入")
print("若文件已存在 打开并清除里面原有内容后开始编辑 若不存在则创建新文件")
print("当mode = 'a'时 意为追加")
print("若文件已存在 打开 指针放到文件末尾后开始编辑 若不存在则创建新文件")
print("当mode = 'r+/w+/a+'时 都意为可读写文件")
print("默认为文本模式t 啥都不写就是rt 如果要以二进制模式打开 则加上b 即如：rb、wb+等")
print("还有一些不常用的参数：")
print("encoding 指明对文件编码 仅适用于文本文件 一般用utf-8")
print("errors 用来指明编码和解码错误时怎么样处理 不在二进制模式下使用")
print("当errors = 'ingore'时 意为忽略产生的错误")
print("当errors = 'strict'时 编码出错则抛出异常ValueError")
print("当errors = 'replace'时 使用某字符进行替代模式 比如使用'?'来替换出错的")
print("可以设置一个变量x=open(filename) 会给x返回一个16进制表示的正整数")
print("读取文件内容 xx.read([size]) size代表读取的字节数量 不写/负数即读取全部")
print("按行读取文件内容 xx.readline([size]) 读取整行 包括最后的\\n")
print("写入内容到文件 file.write(str) 返回的是写入字符串的长度")
print("关闭文件 xxx.close()\n")

print(16 + " 文件的函数")
print("程序运行时 按CTRL+C即可结束程序")
print("fileObject.truncate([size]) 用于截断文件")
print("设定size即从size个字符后开始截断 没有设置则从头截断 即清空文件")
print("file.seek(offset[, whence]) offset是移动偏移的字节数")
print("file.seek(0,0)或(0) 指针去到文件开头")
print("file.seek(x,1) 代表从当前位置向后移x(正数)个字节 若x是负数则向前移")
print("file.seek(x,2) 代表从文件末尾向后移x(正数)个字节 若x是负数则向前移")

print(17 + " 文件的函数")
print("file.close() 关闭文件可近似看作电脑的'刷新'功能 关闭文件后 文件内容才同步到磁盘")
print("如果不关闭 资源释放就要等到垃圾回收时完成")
print("打开太多文件不关闭可能会导致资源耗尽无法再打开新的文件")

print(18 + " function")
print("用'def'定义函数")
print("def 函数名(参数1,参数2...) 也可以没有参数")
print("def 函数名(*xxx) 即获取引用函数时括号里的所有参数 如：函数名(as,dsf,ss,et,dd)")

print(19 + " function")
print("运行自定义函数的n种方法")

print(20)
print("x = x + y 可以缩写成 x += y")

print(21)
print("函数是从里到外运算的")
print("函数结尾加上return的话 引用函数得到的就是return后参数/表达式的值")
