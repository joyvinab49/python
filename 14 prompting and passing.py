from sys import argv
script, user_name, favourite_food = argv
prompt = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"Your favourite food is {favourite_food}, I love it, too!")
print("What about your favourite drinks?")
drinks = input(prompt)

print(f"""
    Alright, so you said {likes} about liking me.
    You live in {lives}. Not sure whre that is.
    And you have a {computer} computer. Nice.
    Your favourite drinks is {drinks}.
    """)
