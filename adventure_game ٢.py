import random  # used to select random item from an array
from time import sleep  # used to pause the game

# game settings and options
caveMonsters = ['Vampire', 'Mouse', 'Bat', 'Demon', 'Mummy']
mallMonsters = ['Dragon', 'Ghost', 'Zombie', 'Dog']
seaMonsters = ['Shark', 'Wheat', 'kraken', 'Hydra', 'Leviathan']

places = ['Cave', 'Mall', 'Sea']
weapons = ['Hammer', 'Knife', 'Grenade', 'Fire', 'Arrow']
results = ['win', 'lose']
answers = ['yes', 'no']
monsterName = ''


# show message then pause for x seconds
def pauseMessage(message, seconds=2):
    print(message)
    sleep(seconds)


# get the name of the place that user chose
def getPlaceName(userChoice):
    if userChoice == '1':
        return 'Cave'
    elif userChoice == '2':
        return 'Mall'
    elif userChoice == '3':
        return 'Sea'
    else:
        return 'Unknown'


# get a random monster of the user chosen place
def getRandomMonster(userPlaceChoice):
    if userPlaceChoice == 'Cave':
        monsterName = random.choice(caveMonsters)
    elif userPlaceChoice == 'Mall':
        monsterName = random.choice(mallMonsters)
    elif userPlaceChoice == 'Sea':
        monsterName = random.choice(seaMonsters)

    print(monsterName)


# change weapons
def changeWeapon():
    changeـrequest = input('Do you want to change your weapon?\n')

    while changeـrequest not in answers:
        print('Please enter (yes/no).')
        changeـrequest = input('Do you want to change your weapon?\n')

    if changeـrequest == 'yes':
        userWeapon = random.choice(weapons)
        print('Your weapon is ' + userWeapon)


# print places' names
def showPlacesNames():
    for index, place in enumerate(places, start=1):
        pauseMessage("{} - The {}".format(index, place), 1)
    print('')


# Start our game
continueGame = 'yes'

while continueGame == 'yes':
    print('=============================================================')
    print('                      Monsters Slayer')
    print('=============================================================')

    pauseMessage('', 1)

    string = ("Welcome to our new game, As long as"
              "you are alive you encounter danger."'\n'
              "In this journey, you will confront dangerous monsters."'\n'
              "It depends on how fast your reaction is to kill them"'\n'
              "It is now confrontation time, Can you survive?"'\n')
    pauseMessage(string, 1)
    pauseMessage('Choose where would you like to go?\n', 1)

    currentPlace = ''

    while currentPlace not in places:
        showPlacesNames()
        placesOptions = ("Please choose the wanted ,"
                         "place: (type 1, 2, or 3):"'\n')
        userChoice = input(placesOptions)
        currentPlace = getPlaceName(userChoice)

    pauseMessage('You equipped a weapon')
    userWeapon = random.choice(weapons)
    print(userWeapon)
    changeWeapon()

    pauseMessage('\nBe ready! You are now in the ' + currentPlace +
                 ' and you are equipped with ' + userWeapon + ' weapon.')

    pauseMessage('now, in a sudden, you encounter a monster in fornt of you')
    getRandomMonster(currentPlace)
    pauseMessage('Use your weapon to kill the monster right now\n')

    if monsterName == 'Bat' and userWeapon == 'Fire':
        pauseMessage('You Win')
        print('You are strong!')
    else:
        pauseMessage('You ' + random.choice(results))
        print('Game Over')

    continueGame = input('Enjoyed our game? Would you '
                         'like to play again? (yes or no)\n')
    while continueGame not in answers:
        print('Please enter (yes or no).')
        continueGame = input('Enjoyed our game? Would you'
                             ' like to play again? (yes or no)\n')
