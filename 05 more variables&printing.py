name = 'Zed A. Shaw'
age = 35
height = 74
height_cm = round(height * 2.54) #去掉小数点
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#这里f和后面的不能有空格不然会报错
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
