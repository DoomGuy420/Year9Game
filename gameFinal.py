from art import *
from MyGameDesign import textgamelib

homescreenart = text2art("Brave", font="asdfsasdfsasdfdsseeebdfdfhaerdhfjfgjf")
print(homescreenart)

gameScore = 0
while gameScore == 0:
    textgamelib.printDivider("-", 10)
    print("Welcome to Brave, a text based game. You might be familiar with Jabari from the book Jabari Jumps. In this game you will be playing as Jabari's son. Before you can get to the game, you have to go through the tutorial and learn the ropes. Here we go!")
    textgamelib.printDivider("-", 10)
    print("Wake up, it's time to get out of bed.")
    getUpTutorial = 0
    getUpTutorial = input("Try getting up by typing 'Get Up'")
    if "get up" in getUpTutorial.lower():
        print("You got up")
    else:
        print("I can't really understand you try again.")
        getUpTutorial = input("Try getting up by typing 'Get Up'")
