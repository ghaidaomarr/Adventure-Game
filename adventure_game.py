import time  # Imports a module to add a pause
import random  # import random to select random objects
# List Of Objects.
Places = ['Amusement Park', 'Airport', 'Jungle']
AmusementPark_Monsters = ['Zombie', 'Dog', 'Bats', 'Mouse', 'Lion']
Airport_Monsters = ['Slaughterer', 'Vampire', 'Aliens']
Jungle_Monsters = ['Tiger', 'crocodile', 'Gorilla', 'Snake', 'Dinosaur']
Weapons = ['Axs', 'Mace', 'Arrow', 'Gun', 'bomb']
Game_Result = ['Win', 'Lose']
UserـAnswer = ['yes', 'no']
Monster = ''
# end List.


# function add time
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# function User Choise Places
def UserChoise(Input):
    if Choise == Choise == '1':
        return 'Amusement Park'
    elif Choise == Choise == '2':
        return 'Airport'
    elif Choise == Choise == '3':
        return 'Jungle'
    else:
        return ''


# The function of the user's choice of location is given by the monster
def BringMonster(UserChoise):
    if UserChoise == 'Amusement Park':
        Monster = random.choice(AmusementPark_Monsters)
        print(Monster)
    if UserChoise == 'Airport':
        Monster = random.choice(Airport_Monsters)
        print(Monster)
    if UserChoise == 'Jungle':
        Monster = random.choice(Jungle_Monsters)
        print(Monster)


# function change Weapons
def changeWeapon():
    changeـrequest = input('Do you want to switch weapon?\n')
    while changeـrequest not in UserـAnswer:
        print('Please enter (yes/no).')
        changeـrequest = input('Do you want to switch weapon?\n')
    if changeـrequest == 'yes':
        weaponـchanged = random.choice(Weapons)
        print(weaponـchanged)
# Game Start


RepeatGame = 'yes'
while RepeatGame == 'yes':
    # Introduction
    print_pause("Welcome to the exciting 'adventure fire' game"'\n')
    string = ("It will take you to another side of the fantasy world full of"
              "excitement full of excitement and fun,the game provides"'\n'
              "you with choices,as you play the game you must think well"
              "before each choice so that you can win"'\n')
    print_pause(string)
    print_pause('Please Choose Which Place you want to play \n')
    for place in Places:
        print(place)
        time.sleep(1)
    Choise = ''
    while Choise not in Places:
        msg = ("Enter 1 to go inside the Amusement Park."'\n'
               "Enter 2 to go inside the airport terminal."'\n'
               "Enter 3 to discover jungle."'\n'"what do you want to do?"'\n'
               "(Please enter 1, 2 or 3)."'\n')
        Choise = input(msg)
        Choise = UserChoise(Choise)
    print_pause('you have a weapon ')
    weaponـchanged = random.choice(Weapons)
    print(weaponـchanged)
    changeWeapon()
    print_pause(
        '\nyou now in ' + Choise + ' and you have a weapon ' + weaponـchanged)
    print_pause('now you see fornt of you ')
    BringMonster(Choise)
    print_pause('Use weapon to kill monster\n')
    if weaponـchanged == 'Axs' and Monster == 'Vampire':
        print('you Win')
        time.sleep(2)
        print('Game Over')
    else:
        print('you ' + random.choice(Game_Result))
        time.sleep(2)
        print('Game Over')
    RepeatGame = input('Would you like to play again? (yes/no) \n')
    while RepeatGame not in UserـAnswer:
        print('Please enter (yes/no).')
        RepeatGame = input('Would you like to play again? (yes/no)\n')
