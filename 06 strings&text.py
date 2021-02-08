types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


# .format()格式化函数
# https://www.runoob.com/python/att-string-format.html

# 可以接受不限个参数 位置可以不按顺序
print("{} {}".format("hello", "world"))  # 不设置指定位置 按默认顺序
print("{1} {0}".format("hello", "world"))  # 设置指定位置
print("{1} {0} {1} {0}".format("hello", "world"))

# 可以设置参数
print("name:{name}, id {id}".format(name="zoe", id="joyvinab"))

site = {"name": "zoe", "id": "joyvinab"}  # 通过字典设置参数
print("name:{name}, id {id}".format(**site))

my_list = ["zoe", "joyvinab"]  # 通过列表索引设置参数
print("name:{0[0]}, id {0[1]}".format(my_list))  # "0"是必须的

# 输出结果都是：name:zoe, id joyvinab
