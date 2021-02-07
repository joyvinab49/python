formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#下面这个输出的是16个{}
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hello hello,",
    "What's your name?",
    "My name is Kate.",
    "Nice to meet you today!"
))
