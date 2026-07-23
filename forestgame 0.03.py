import random

inventory = []
cabin_found = 0


def clear():
    i = 0
    while i <= 8:
        print("\n")
        i = i + 1


def ask(question):
    clear()
    print(question)
    answer = input()
    return answer


ask("FORESTGAME v0.03\nby anon-aardvark\n\nEnter anything to play")


def choice_1():
    choice = ask("You found an run-down log cabin.\n1: go inside\n2: keep walking")
    if choice == "1":
        choice = ask(
            "There's a chest to the side of the door, an empty chair, and a bed.\n1: look in the chest\n2: leave")
        if choice == "1":
            choice = ask("There's an axe and a loaf of bread in the chest.\n1: take them\n2: leave them")
            if choice == "1":
                inventory.append("axe")
                inventory.append("loaf of bread")
                choice_0()
            elif choice == "2":
                choice_0()
    elif choice == "2":
        choice_2()


def choice_2():
    choice = ask("You walk around. There isn't anything but endless forest.\n1: keep walking\n2: scavenge\n3: call for help")
    if choice == "1":
        if random.randint(1, 8) == 1 and cabin_found == 0:
            choice_1()
        else:
            choice_2()
    elif choice == "2":
        choice_3()
    elif choice == "3":
        ask("You scream, but nobody hears you.")
        choice_0()


def choice_3():
    if random.randint(1, 2) == 1:
        if random.randint(1, 2) == 1:
            choice = ask("You found some nuts on the ground.\n1: pick them up\n2: leave them")
            if choice == "1":
                inventory.append("nuts")
                choice_0()
            elif choice == "2":
                choice_0()
        elif random.randint(1, 2) == 1:
            choice = ask("You find some pebbles laying around.\n1: pick them up\n2: leave them")
            if choice == "1":
                inventory.append("pebbles")
                choice_0()
            elif choice == "2":
                choice_0()
        elif random.randint(1, 2) == 1:
            choice = ask("You find an apple on the ground.\n1: pick it up\n2: leave it")
            if choice == "1":
                inventory.append("apple")
                choice_0()
            elif choice == "2":
                choice_0()
        elif "axe" in inventory:
            choice = ask("You found a log lying around. You can't pick it up, but you can chop it.\n1: chop it up\n2: leave it")
            if choice == "1":
                choice = ask("The wood is small enough to carry.\n1:pick some up\n2: leave it")
                if choice == "1":
                    inventory.append("wood")
                    choice_0()
                elif choice == "2":
                    choice_0()
            elif choice == "2":
                choice_0()
        else:
            ask("You didn't find anything of interest.\nPress anything to move on.")
            choice_0()
    else:
        ask("You didn't find anything of interest.\nPress anything to move on.")
        choice_0()


def choice_0():
    if not inventory:
        choice = ask("You are in a dark forest.\nWhat do you want to do?\n\n1: walk around\n2: scavenge\n3: call for help")
    else:
        choice = ask("You are in a dark forest.\nWhat do you want to do?\n\n1: walk around\n2: scavenge\n3: call for help\n4: check inventory")
    if choice == "1":
        if "axe" in inventory:
            if random.randint(1, 4) == 1:
                choice = ask("You found a tree. Would you like to chop it?\n1: yes \n2: no")
                if choice == "1":
                    inventory.append("wood")
                    choice_0()
                if choice == "2":
                    choice_0()
        else:
            if random.randint(1, 8) == 1 and cabin_found == 0:
                choice_1()
            else:
                choice_2()
    elif choice == "2":
        choice_3()
    elif choice == "3":
        ask("You scream, but nobody hears you.\nPress anything to move on.")
        choice_0()
    elif choice == "4" and inventory:
        ask(list(inventory), "press anything to move on")
        choice_0()


choice_0()
