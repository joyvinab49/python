from sys import argv #导入参数变量模组

script, filename = argv

#打开某个文件 创建一个file对象
#open(name[, mode[, buffering]])
#mode决定了打开文件的模式：只读 写入 追加等 默认是只读（r）
#buffering寄存 可取的值有0 1 >1三个
#0代表buffer关闭（只适用于二进制模式）
#1代表line buffer（只适用于文本模式）
#>1表示初始化的buffer大小
txt = open(filename) #用open函数接收文件名参数 并返回一个值 此处把返回值赋予了txt变量
#返回值不是文件的内容 是十六进制表示的正整数

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again!")
file_again = input(">>>")

txt_again = open(file_again)

print(txt_again.read())
