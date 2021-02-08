print("How old are you?", end=' ')
age = input()  # input会和print的内容在同一行显示
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Please input x:", end=' ')
x = int(input())  # 整数型 是number
print("Please input y:", end=' ')
y = input()  # 字符串 是string
print(x, y)
sum1 = x * y  # 这个的结果是将y重复x遍
print("x * y = ", sum1)
sum2 = x + float(y)  # 将y转换成浮点数
print("x + y =", sum2)
