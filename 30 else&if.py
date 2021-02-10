people = 30
cars = 40
trucks = 15

if people < cars:
    print("Too many cars!")
elif people > cars:
    print("Not many cars!")
else:
    print("We can't decide.")

if trucks > cars:
    print("Too many trucks!")
elif trucks < cars:
    print("Not many trucks!")
else:
    print("We still can't decide.")

if people > trucks and cars < trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
