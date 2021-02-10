
numbers = []
lists = []


def add_numbers(max, add):
    i = 0
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + add
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        print("-----------------")


add_numbers(8, 2)

print("The numbers: ")

for num in numbers:
    print(num)


def for_loops(max):
    for j in range(0, max):
        print(f"At the top j is {j}")
        lists.append(j)

        # j = j + add 这个不用了 会不断+1
        print("Lists now: ", lists)
        print(f"At the bottom j is {j}")
        print("-----------------")


for_loops(15)  # 结果是0-14 不包括15

print("The lists: ")

for list in lists:
    print(list)
