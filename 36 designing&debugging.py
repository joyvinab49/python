import sys
script, name = sys.argv

print("Hi " + name + " ,welcome to THE HOUSE.")


def open():
    print("There is a wooden door in front of you, would you like to open it?")
    answer = input(">>>")
    if answer == "yes" or answer == "Yes" or answer == "YES" or answer == "y" or answer == "Y":
        print("You open the wooden door and enter THE HOUSE.")
        enter_house()
    elif answer == "no" or answer == "NO" or answer == "No" or answer == "n" or answer == "N":
        print("You walk backwards and a bear hits you. Luckly, you die.")
    else:
        open()


def enter_house():
    print("Now you enter THE HOUSE.")
    print("You walk around and know that there's a living room, a bedroom, a kicten and a study room in THE HOUSE.")
    print("Which room would you like to visit?")
    room = input(">>>")
    if room == "living room":
        print("You walk into the living room and sit on the sofa.")
        print("You feel so comfortable that you cannot help falling asleep.")
        print("Gradually, you lose all your feelings.")
        print("......")
        print("You die...in peace.")
    elif room == "bedroom":
        print("You walk into the bedroom.")
        print("There's a bed in it, and you like it very much.")
        print("You sit on the bed.")
        print("What do you want to do?")
        print("A. Go to sleep.")
        print("B. Eat some chips.")
        bed_do = input(">>>")
        if bed_do == "A":
            print("You fall asleep quicky.")
            print("You have a good dream.")
            print("Something dangerous is eating your body...")
            print("You die.")
        elif bed_do == "B":
            print("You make the bed dirty with the chips.")
            leave()
        else:
            stuck()
    elif room == "kicten":
        print("There are nice cooker and lots of delicious food in the kicten.")
        print("What would you do?")
        print("A. Eat the food.")
        print("B. Make your own dishes with the cooker.")
        kic_do = input(">>>")
        if kic_do == "A":
            print("The food is delicous but poisonous.")
            print("You die.")
        elif kic_do == "B":
            print("BOOM!")
            print("Sorry, you are not good at cooking at all.")
            print("You destory the kicten.")
            leave()
        else:
            stuck()
    elif room == "study room":
        print("There's a desk, a chair, a huge bookshelf in the study room.")
        print("You walk near the desk.")
        print("There are three books on it.")
        print("Which one would you pick?")
        print("A. The red one on the left.")
        print("B. The blue one on the right.")
        print("C. the green one on the middle.")
        book_pick = input(">>>")
        if book_pick == "A":
            print("You open the book and there's a question:")
            print("What is 8 * 7 - 12 + 6 / 3 ?")
            A1 = input(">>>")
            if A1 == "46":
                print("You answer the qustion correctly.")
                host()
            else:
                print("You give a wrong answer.")
                stuck()
        elif book_pick == "B":
            print("You open the book and there's a question:")
            print("What is hermano in English?")
            A2 = input(">>>")
            if A2 == "brother":
                print("You answer the qustion correctly.")
                host()
            else:
                print("You give a wrong answer.")
                stuck()
        elif book_pick == "C":
            print("You open the book and there's a question:")
            print("Do you like me?")
            A3 = input(">>>")
            if A3 == "Yes" or A3 == "yes" or A3 == "YES":
                print("Oh sorry, you are fake.")
                stuck()
            elif A3 == "No" or A3 == "no" or A3 == "NO":
                print("How dear you do not like me?!")
                stuck()
            elif A3 == "idk" or A3 == "I don't know":
                print("You are honest.")
                host()
            else:
                print("You give a wrong answer.")
                stuck()
        else:
            stuck()


def leave():
    print("A maid comes and asks you to leave.")
    print("You leave THE HOUSE.")
    print("You are free and safe now.")


def stuck():
    print("You seem to not follow the rules in THE HOUSE.")
    print("You are stuck in a dark room.")
    print("You try to seek help but fail.")
    print("Finally, you die of hungry.")


def host():
    print("All the maids come.")
    print("One of them announces that you are the host of THE HOUSE.")
    print("You are safe.")


open()
