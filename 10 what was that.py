tabby_cat = "\tI'm tabbed in."  # \t等于tab键缩进功能
persian_cat = "I'm split\non a line."  # \n换行
backslash_cat = "I'm \ a \ cat"  # I'm \ a \ cat

fat_cat = """
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    """  # 最后一行实际显示出来是两行 因为有\n

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# 以上那些叫做：Escape Sequences
# \\ → Backslash(\)
print("do\\something\\interesting")
# \' → Single-quote(')  \" → Double-quote(")
print("I can \'sing\' and I can \"dance\"")
# \a → ASCII bell (BEL) 据说会发出AWARD BIOS响铃声
print("what it is?\aJust a sound fine.")
# \b → ASCII backspace (BS) 会后退删除一个字符 但放在字符串末尾时无影响
print("abc\bdefg\b")
# \f → ASCII formfeed (FF) 换页
print("123456\f654321")
# \r → Carriage return (CR) 把光标移动到该行的开始位置 经常与\n一起用
print("vue\rpython\n\rhtml")  # python会把vue覆盖掉 html会在下一行显示
# \v → ASCII vertical tab (VT) 垂直制表符
# 让\v后面的字符从下一行开始输出 且开始的列数为\v前一个字符所在列后面一列
print("0123\v456789")  # \v显示的是一个正方形？
# \t → Horizontal tab (TAB) 水平制表符
# 一般系统中 显示水平制表符将占8列 开始占据的初始位置是第8*n列（第一列下标为0）
print("1234567\t123456789")
print("12345678\t0000")  # \t后第一个0和上面的9在同一列
print("123456789\t000")  # \t后第一个0和上上面的9在同一列
# \ooo → Character with octal value ooo 1到3位八进制数所代表的任意字符
print("dsl\101")  # dslA
# \xhh → Character with hex value hh 1到2位十六进制所代表的任意字符
print("\141")  # a
