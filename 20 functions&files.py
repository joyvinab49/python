from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # 指针回到文档开头 moves the file to the 0 byte (first byte) in the file


def print_a_line(line_count, f):  # 文件f会保留readline()读取后所在的位置
    print(line_count, f.readline())


# encoding='utf-8'写上防止报错
current_file = open(input_file, encoding='utf-8', errors='ignore')

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  # 相当于 current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1  # x = x + y → x += y
print_a_line(current_line, current_file)

#最后这三行文字中间有空行
#是因为readline()读取的时候把文件每一行末尾的\n也一起读出来了
#所以相当于有两个\n连在一起写了
