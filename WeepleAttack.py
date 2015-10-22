#Weeple Attack!
#by Daniel Kawamoto

# TO-DO's
# Fix error during attack when weeples < 0
# Get rid of global variables and use 'class'


import time
import random
import sys

global loot
global weeples
global name
loot = 100
weeples = 0
name = None

# DEFENSE LEVELS?
# global defense
# if defense = 0:
#     defensive_power = eww*1
# if defense = 1:
#     defensive_power = int(eww*0.95)
# if defense = 2:
#     defensive_power = int(eww*0.90)
# if defense = 3:
#     defensive_power = int(eww*0.85)
# ETC...

def start():
    print("Howdy there, partner!")
    global name
    name = input("What's your name?\n")
##    if name.upper() == "SARAH":
##        print("Sorry Sarah, you may win at clue but you will NEVER win this game.")
##        sys.exit()
##    else:
##        pass
    choice = input("Welcome, {}!\nAre you ready to lead your weeple army to victory? Y/N\n".format(name))
    if choice.upper() == "Y":
        begin()
    elif choice.upper() == "N":
        print("\nThere is a place in this world for sissies too. You'd better run. An army of weeples is coming for you. \nBy the way...\n")
        time.sleep(1)
        print("I'd sleep with one eye open if I were you.")
    else:
        print("\nLearn how to read and come back later...")
        time.sleep(3)
        second_choice = input("Just kidding, but please pay attention to what you type in the future. Wanna play? Y/N")
        if second_choice.upper() == "Y":
            begin()
        elif second_choice.upper() == "N":
            print("\nThere is a place in this world for sissies too. You'd better run. An army of weeples is coming for you. \nBy the way...\n")
            time.sleep(1)
            print("I'd sleep with one eye open if I were you.")
        else:
            print("Come back when you put your big-kid pants on.")
            exit()

def begin():
    print("\nLet's get this party started...\n")
    time.sleep(.5)
    # REWRITE INTRO
    print("The Evil Weeple Warriors or E.W.W. are rebels travelling in groups of 800-1200.\nBattles are simple. Each time you attack, you will lose weeples and E.W.W. will lose rebels.\nHowever, when you attack, a small number of E.W.W. will likely join your army of weeples.\n")
    time.sleep(5)
    train_or_attack()

def are_you_sure(): #NOT YET USED
    certainty = input("Come on... play one round? Y/N")
    if certainty.upper() == "Y":
        train_or_attack()
    elif certainty.upper() == "N":
        exit()
    else:
        are_you_sure()

def train_or_attack():
    action = input("Okay, {}, what would you like to do?\n1. TRAIN WEEPLES\n2. ATTACK\n3. GET INFO ABOUT YOUR ARMY AND LOOT\n4. Quit while you're ahead\nPlease enter the number coresponding with your choice:\n".format(name))
    if action == "1":
        train()
    elif action == "2":
        attack()
    elif action == "3":
        get_info()
    elif action == "4":
        print("\n---      ---   --------    ----    ---- \n ***    ***   **********   ****    **** \n  ---  ---   ----    ----  ----    ---- \n   ******    ***      ***  ****    **** \n    ----     ---      ---  ----    ---- \n    ****     ****    ****  ************ \n    ----      ----------   ------------ \n    ****       ********    ************ \n\n---      ---   --------    ----    ---- \n***  **  ***   ********    *****   **** \n---  --  ---     ----      ------  ---- \n***  **  ***     ****      ************ \n---  --  ---     ----      ------------ \n************     ****      ****  ****** \n ----------    --------    ----   ----- \n  ********     ********    ****    **** \n")
        exit()
    else:
        train_or_attack()

def train():
    global weeples
    global loot
    while True:
        try:
            possible = (loot * 10)//1
            numWeeples = int(input("\nTraining 10 WEEPLES costs 1 LOOT - you have {} LOOT and can train up to {} weeples. You should also know that we round up for the cost of training weeples, so try to purchase sets of 10 units. How many weeples would you like to train?\n".format(loot, possible)))
            break
        except ValueError:
            print ("Could you at least provide an actual number?")
            continue
    if loot - numWeeples/10 < 0:
        print("Sorry, you don't have enough loot to train that many weeples. ")
        train()
    elif loot - numWeeples/10 >= 0:
        loot = int((loot - numWeeples/10)//1)
        weeples = (weeples + numWeeples)//1
        time.sleep(1)
        get_info()
        # ADD IN A CATCH FOR ENTERING A NEGATIVE NUMBER AND GAINING LOOT
    else:
        print ("Try a different number")

def attack():
    global weeples
    global loot
    eww = random.randrange(800, 1200)
    rebels = eww
    print("  ......(\_/)\n  ......( ‘_’)\n  ..../''''''''''''\======░\n  ../'''''''''''''''''''\\\n  ..\_@___@___@___@___@_/\n")
    time.sleep(1)
    print("\nYou've encountered a group of {} E.W.W. nomads.\n".format(eww))
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Your army of {} weeples attacks with great vigor.\n".format(weeples))
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

    # TURN THIS INTO A FUNCTION?
    # FIX YOUR MATH!

    weeples_lost = int((rebels*.25)//1)
    loot_gained = int((rebels*.04)//1)
    converted = int((rebels*.07)//1)
    weeples = weeples - weeples_lost + converted
    loot = loot + loot_gained
    rebels = int(rebels - (weeples *.3)//1)
    if weeples >0:
        print("BATTLE RESULTS!\n\nREBELS REMAINING: {}\nWeeples lost: {}\nWeeples gained: {}\nTOTAL WEEPLES: {}\nLoot gained: {}\nTOTAL LOOT: {}\n".format(rebels, weeples_lost, converted, weeples, loot_gained, loot))

        def attack_or_retreat():
            global weeples
            battle_choice = input("What would you like to do, {}?\n1. Attack again\n2. Retreat (You will lose 50\% of your weeples)\n".format(name))
            if battle_choice == "1":
                attack_again()
            elif battle_choice == "2":
                weeples = weeples * .5
                train_or_attack()
            else:
                print("Please, only type a '1' or a '2'... your computer confuses easily.")
                attack_again()
    else:
        game_over()

    def attack_again():
        global weeples
        global loot
        nonlocal rebels

        print("  ......(\_/)\n  ......( ‘_’)\n  ..../''''''''''''\======░\n  ../'''''''''''''''''''\\\n  ..\_@___@___@___@___@_/\n")
        time.sleep(1)
        print("\nYour army stares down the remaining {} E.W.W. nomads.\n".format(rebels))
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Your army of {} weeples attacks with great vigor.\n".format(weeples))
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)

        weeples_lost = int((rebels*.25)//1)
        loot_gained = int((rebels*.04)//1)
        converted = int((rebels*.07)//1)
        weeples = weeples - weeples_lost + converted
        loot = loot + loot_gained
        rebels = int(rebels - (weeples *.3)//1)
        print("BATTLE RESULTS!\n\nREBELS REMAINING: {}\nWeeples lost: {}\nWeeples gained: {}\nTOTAL WEEPLES: {}\nLoot gained: {}\nTOTAL LOOT: {}\n".format(rebels, weeples_lost, converted, weeples, loot_gained, loot))
    time.sleep(2)
    while rebels > 50:
        if weeples > 0:
            print("The E.W.W. Rebels are standing their ground... \n")
            time.sleep(1)
            attack_or_retreat()
        else:
            game_over()
            break
    else:
        print("The E.W.W. have realized they are scum in the face of your mighty weeple army.\n")
        train_or_attack()

def get_info():
    print("\nYou have", weeples, " WEEPLES and", loot, " LOOT.\n")
    time.sleep(1)
    train_or_attack()

def game_over():
    choice = input("You have been defeated by the forces of E.W.W. and all hope is lost. Would you like to play again?")
    if choice.upper() == "Y":
        start()
    elif choice.upper() == "N":
        exit()
    else:
        print("\nLearn how to read and come back later...")
        time.sleep(3)
        second_choice = input("Just kidding, but please pay attention to what you type in the future. Wanna play? Y/N")
        if second_choice.upper() == "Y":
            begin()
        elif second_choice.upper() == "N":
            print("\nThere is a place in this world for sissies too. You'd better run. An army of weeples is coming for you. \nBy the way...\n")
            time.sleep(1)
            print("I'd sleep with one eye open if I were you.")
        else:
            print("Come back when you put your big-kid pants on.")
            exit()


# OTHER IDEAS
    # ADD OPTION TO PLAY AGAIN
    # How many weeples do you want to attack with?
    # enemies have between x and y weeples. if you win with less weeples than your enemy, you will recruit some of them to join your weeple army
    # SOLVE random math problems to train weeples?
    # retreat or stand your ground
        #retreat - leave behind x weeples as a decoy and return home
        #attack - lose small percentage of weeples
        #defend - lose greater percentage of weeples
        #loser - whoever drops to less than 100 weeples first

start()
