import json
import os
import random
import sys
inventory = []
cabin_found = 0
settled = 0


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


def save():
    save_data = {
        "inventory": inventory,
        "settled": settled,
        "cabin_found": cabin_found
    }
    with open("forestgamesave.json", "w") as json_file:
        json.dump(save_data, json_file, indent=4)

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
                cabin_found = 1
            elif choice == "2":
                choice_0()
    elif choice == "2":
        choice_2()


def choice_2():
    if settled == 0 and not inventory:
        choice = ask("You walk around. There isn't anything but endless forest.\n1: keep walking\n2: scavenge\n3: call for help")
    elif settled == 0:
        choice = ask("You walk around. There isn't anything but endless forest.\n1: keep walking\n2: scavenge\n3: call for help\n4: check inventory")
    else:
        choice = ask("You walk around. There isn't anything but endless forest.\n1: keep walking\n2: scavenge\n3: call for help\n4: check inventory\n5: return to camp")
    if choice == "1":
        if random.randint(1, 8) == 1 and "axe" not in inventory and cabin_found == 0:
            choice_1()
        elif random.randint(1, 4) == 1 and settled == 0:
            choice = ask("You found an empty plot of land. Would you like to set up camp here?\n1: yes \n2: no")
            if choice == "1":
                settled = 1
                ask("You set up camp here. Press anything to move on.")
                choice_4()
        elif "axe" in inventory:
            if random.randint(1, 4) == 1:
                choice = ask("You found a tree. Would you like to chop it?\n1: yes \n2: no")
                if choice == "1":
                    inventory.append("wood")
                    choice_0()
                if choice == "2":
                    choice_0()
        else:
            choice_2()
    elif choice == "2":
        choice_3()
    elif choice == "3":
        ask("You scream, but nobody hears you.")
        choice_0()
    elif choice == "4" and inventory:
        list_inventory = list(inventory), 'press anything to move on'
        ask(list_inventory)
        choice_0()
    elif choice == "5" and settled == 1:
        choice_4()


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

def choice_4():
    choice = ask("You're at your camp. What would you like to do?\n1: leave\n2: save")
    if choice == "1":
        choice_0()
    elif choice == "2":
        choice = ask("Save data will be overwritten. \n1: ok \nanything else: no")
        if choice == "1":
            save()
            choice_4()
        else:
            choice_4()

def choice_0():
    global settled
    if not inventory:
        choice = ask("You are in a dark forest.\nWhat do you want to do?\n\n1: walk around\n2: scavenge\n3: call for help")
    elif settled == 0:
        choice = ask("You are in a dark forest.\nWhat do you want to do?\n\n1: walk around\n2: scavenge\n3: call for help\n4: check inventory")
    else:
        choice = ask("You are in a dark forest.\nWhat do you want to do?\n\n1: walk around\n2: scavenge\n3: call for help\n4: check inventory\n5: return to camp")
    if choice == "1":
        if "axe" in inventory:
            if random.randint(1, 4) == 1:
                choice = ask("You found a tree. Would you like to chop it?\n1: yes \n2: no")
                if choice == "1":
                    inventory.append("wood")
                    choice_0()
                if choice == "2":
                    choice_0()
            elif random.randint(1, 4) == 1 and settled == 0:
                choice = ask("You found an empty plot of land. Would you like to set up camp here?\n1: yes \n2: no")
                if choice == "1":
                    settled = 1
                    ask("You set up camp here. Press anything to move on.")
                    choice_4()
                elif choice == "2":
                    choice_0()
            else:
                choice_2()


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
        list_inventory = list(inventory),  'press anything to move on'
        ask(list_inventory)
        choice_0()
    if choice == "5" and settled == 1:
        choice_4()

choose = ask("FORESTGAME v0.04\nby anon-aardvark\n\nEnter anything to play\nType 'save' for save file info")
if choose == "save" and os.path.exists("forestgamesave.json"):
    choose = ask("load: load file\n delete: delete save")
    if choose == "load":
        with open ("forestgamesave.json", "r") as json_file:
            save_data = json.load(json_file)
        inventory = save_data["inventory"]
        settled = save_data["settled"]
        cabin_found = save_data["cabin_found"]
    elif choose == "delete":
        randomdeletenumber = str(random.randint(1, 99999))
        deletestuff = ("WARNING!!! YOUR SAVE DATA WILL BE DELETED AND YOU WILL NOT BE ABLE TO RECOVER IT!!! If you're sure about deleting it, type this random number:", randomdeletenumber)
        choose = ask(deletestuff)
        if choose == randomdeletenumber:
            os.remove("forestgamesave.json")
            ask("Save deleted. Press anything to exit.")
        else:
            ask("Deletion aborted. Press anything to quit out.")
            sys.exit()
elif choose == "save" and not os.path.exists("forestgamesave.json"):
    ask("No save data found. Make sure the name is 'forestgamesavesave.json', or maybe it got deleted.")
    sys.exit()
else:
    print("")

choice_0()
