from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()  # 合成一行代码来写

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# in_file.close()
# 关闭文件可以近似看作我们电脑的 "刷新" 功能 关闭文件后 文件内容才会同步至磁盘
# linux系统中 每个进程打开文件数量是有限的
# 如果不关闭 资源释放就要等到垃圾回收时完成 误事
# 打开太多文件不关闭 有可能导致资源耗尽 无法再打开新的文件
