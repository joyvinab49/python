# Review章节
print(1)
print("print()是输出内容 里面可以是字符串等可以是变量名可以是表达式")
print("让两个print在同一行显示", end=" ")
print("就在同一行了")
print("定义新的变量直接写：变量 = 值\n")

print(3)
print("加 减 乘 除：+ - * /")
print("除法/：整除会带一位小数点x.0 非整除能除尽会出结果")
print("求余数：%")
print("先除法再求余数 ", 9 / 3 % 2, " 9 / 3 % 2等于1")
print("大于(等于)、小于(等于)返回True/False\n")

print(4)
print("变量命名规则跟js那些一样啦 不过好像更喜欢用_")
print("比如：do_you_love_me\n")

print(5)
print('f""格式化字符串')
print("在打印的时候能够将大括号{变量/表达式}换成对应的值打印出来")
print("round()能去掉数字后的小数点\n")

print(6)
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

print(7)
print("字符串不能直接和数字相加 报错")
print("两个字符串数字相加就是写在一起而已")
print("字符串*数字x 相当于字符串出现x次\n")

print(8)
print(".format()格式化函数和{}不写在一起 就可以多次赋值使用\n")

print(9)
print("\\n是换行符")
print('"""三行单/双引号"""可以里面写多行内容\n')

print(10)
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

print(11)
print("int()是整数型")
print("float()是浮点数型 有小数点")
print("float(True) == 1.0")
print("float(False) == 0.0")
print("int和float可以互相转换")
print("input()输入的数字是字符串类型的\n")

print(13)
#https://blog.csdn.net/qq_30815237/article/details/93203934
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
