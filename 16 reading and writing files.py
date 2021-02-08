from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't you want that, hit CTRL-C (^C).")  # KeyboardInterrupt 结束程序
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+') #如果不写mode的话 默认是'r'

print("Truncating the file, Goodbye!")
target.truncate() #如果open的mode是'w'的话 不需要这个 在打开时自动清除所有内容了

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("Let's see the content...")
target.seek(0)  # 让指针去到文本的开头
print(target.read())

print("And finally, we close it.")
target.close()
