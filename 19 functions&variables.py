import random


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print(">>>We can just give the function numbers directly:")
cheese_and_crackers(20, 30)  # 引用function的时候直接带上了参数

print(">>>OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# 设定变量

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # 引用变量作为参数

print(">>>We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)  # 算数也可以

print(">>>And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# 引用上面的变量计算来作为参数

# 我自己design的function


def something_simple(val1, val2, val3, val4):
    print(f"The first number is: {val1}")
    print(f"The second number is: {val2}")
    print(f"The third number is: {val3}")
    print(f"The fourth number is: {val4}")


# 方法一
print(">>>直接带参数")
something_simple(1, 2, 3, 4)

# 方法二
print(">>>设置变量作为参数")
num1 = 11
num2 = 22
num3 = 33
num4 = 44
something_simple(num1, num2, num3, num4)

# 方法三
print(">>>变量之间的运算的值作为参数")
something_simple(num1, num1 + num2, num3, num3 + num4)

# 方法四
print(">>>变量运算的值作为参数")
something_simple(num1 + 10, num2 + 100, num3 + 1000, num4 + 10000)

# 方法五
print(">>>用户输入的值作为参数")
q1 = int(input("number1: "))
q2 = int(input("number2: "))
q3 = int(input("number3: "))
q4 = int(input("number4: "))
something_simple(q1, q2, q3, q4)

# 方法六
print(">>>运算的值作为参数")
something_simple(1 + 2, 2 + 3, 3 + 4, 4 + 5)

# 方法七
print(">>>用from sys import argv")

# 方法八
print(">>>利用random函数生成随机数作为参数")
p1 = random.randint(0, 9)
p2 = random.randint(0, 9)
p3 = random.randint(0, 9)
p4 = random.randint(0, 9)
something_simple(p1, p2, p3, p4)

# 方法九
print(">>>用另一个function的参数作为参数")


def another_one(val):
    something_simple(val, val + 1, val + 2, val + 3)


another_one(10)

# 方法十
print(">>>利用另一个function的值作为参数")


def tool_func(val):
    val = random.randint(0, val)
    return val #没有这行的话下面引用结果是none


something_simple(tool_func(19), tool_func(23), tool_func(33), tool_func(31))
