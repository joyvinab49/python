#impot sys: 导入模块 sys模块包含了与python解释器和它的环境有关的函数
#当python执行import sys语句的时候 它在sys.path变量中所列目录中寻找sys.py模块
#如果找到了这个文件 这个模块的主块中的语句被运行 这个模块能被使用
#sys.argv表示sys模块中的argv变量 实际上它是一个字符串的列表
#sys.argv包含了命令行参数的列表 即使用命令行传递给程序的参数
from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#input和argv的区别
#input是在程序执行的时候用户输入东西
#argv是在命令行写参数
input("type in ok: ")

#执行这个文件要输入
#python 文件名 参数1 参数2 参数3
#文件名总是sys.argv列表的第一个参数
#参数之间以空格区分 都是string
