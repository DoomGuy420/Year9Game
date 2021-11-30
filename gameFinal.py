from art import *
from random import *
import textgamelib
from playsound import playsound

homescreenart = text2art("Brave", font="asdfsasdfsasdfdsseeebdfdfhaerdhfjfgjf")
print(homescreenart)
textgamelib.printDivider("-", 40)
print("Welcome to Brave, a text based game. You might be familiar with Jabari from the book Jabari Jumps. In this game you will be playing as Jabari's son. Before you can get to   the game, you have to go through the tutorial and learn the ropes. Here we go!")
textgamelib.printDivider("-", 40)
gameScore = 0
while gameScore == 0:
    chapter0art = tprint("Chapter 0", font="bulbhead")
    #change tprint to text2art when at school
    print("Wake up, it's time to get out of bed.")
    getUpTutorial = input("Try getting up by typing 'Get Up'\n")
    tutorialScore = 0
    while tutorialScore == 0:
        if "get up" in getUpTutorial.lower():
            print("You got up")
            tutorialScore += 1
        else:
            print("I can't really understand you try again.")
            getUpTutorial = input("Try getting up by typing 'Get Up'\n")
    textgamelib.printDivider("-", 40)
    print("Good job, the way you play this game is simple, you just have to type your actions with specifications after. We'll continue showing you how to do things.")
    textgamelib.printDivider("-", 40)
    pickUpTutorial = input("It's almost time for school. Your bag is by the door, pick up your bag and exit the door. \n")
    while tutorialScore == 1:
        if "pick up" in pickUpTutorial.lower() and ("backpack" in pickUpTutorial.lower() or "bag" in pickUpTutorial.lower()):
            print("You picked up your bag")
            tutorialScore += 1
        elif "pick up" in pickUpTutorial.lower():
            print("I don't understand what you are trying to pick up")
            pickUpTutorial = input("Try typing 'Pick Up Bag'\n")
        else:
            print("I don't understand what you are trying to do")
            pickUpTutorial = input("Try typing 'Pick Up Bag'\n")
    textgamelib.printDivider("-", 40)
    print("This will be an important action as you will need to pick up certain items in the game. The next action will also be very important. It's the 'go' action which will allow   you to walk and travel to other places. We'll talk later about other actions.")
    textgamelib.printDivider("-", 40)
    goTutorial = input("Time to go out of your room and eat breakfast.\n")
    while tutorialScore == 2:
        if "go out of room" in goTutorial.lower():
            print('You exited your room.')
            tutorialScore += 1
        elif "go" in goTutorial.lower():
            print("I can't really understand where you want to go")
            goTutorial = input("Try typing 'Go out of room'\n")
        else:
            print("I don't know what you are trying to do")
            goTutorial = input("Try typing 'Go out of room'\n")
    textgamelib.printDivider("-", 40)
    print("You exit your room to be greeted by your dad, Jabari.")
    print("Jabari: Good Morning son, almost time for school here's a bowl of cereal for breakfast.")
    eatTutorial = input("Time to eat your cereal for breakfast.\n")
    while tutorialScore == 3:
        if "eat" in eatTutorial.lower() and ("cereal" in eatTutorial.lower() or "breakfast" in eatTutorial.lower()):
            print("You ate your cereal, it tasted good.")
            tutorialScore += 1
        elif "eat" in eatTutorial.lower():
            print("What are you trying to eat")
            eatTutorial = input("Try typing 'Eat Breakfast'\n")
        else:
            print("I can't tell what you are trying to do.")
            eatTutorial = input("Try typing 'Eat Breakfast'\n")
    textgamelib.printDivider("-", 40)
    print("Jabari: It's time to head to school son. Have a good day!")
    print("You exit your house.")
    goTutorial2 = input("Where would you like to go?\n")
    while tutorialScore == 4:
        if "go to school" in goTutorial2.lower():
            print("You walk to school.")
            tutorialScore += 1
        elif "go" in goTutorial2:
            print("I can't understand where you want to go at the moment")
        else:
            print("I can't tell what you want to do.")
            goTutorial2 = input("Try typing 'Go to school'\n")
    print("You arrive at school to see your friend Jimmy at the front door waiting for you. \nJimmy: Hey how are you doing? \nYou: I'm doing good, school going to be boring though. \n Jimmy: It's not that bad. \nThe bell rings signifyng that classes are startng. You and Jimmy rush to class and get there right on time.")
    print("After a day of work and classes at school, you return home to eat with your father Jabari. You then finish your homework and go to bed.")
    textgamelib.printDivider("-", 40)
    endingArt = tprint("End of Tutorial", font="bulbhead")
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 1:
    chapter1art = tprint("Chapter 1", font=("bulbhead"))
    textgamelib.printDivider("-", 40)
    wakeUp = 0
    while wakeUp == 0:
        playsound('c:\\Users\\molem\\Downloads\\Python Year 9 Coding\\MyGameDesign\\alarmclockbeeping.mp3', block=False)
        getUpChapter1 = input("Time to get up\n")
        if "get up" in getUpChapter1.lower():
            wakeUp += 1
            print("You Got up")
        else:
            getUpChapter1 = input("It's time to get up")
    textgamelib.printDivider("-", 40)
    print("You wake up and look at the time. It's 8:30.....\n8:30?!?!?! That's half an hour after your school started.\nYou got up, rushed to brush your teeth and picked up your bag and headed to the living room to quickly get breakfast and head out to school. As you headed into the living   room, you realized that the lights weren't on. The lights were usually on so you decided to find the switch.")
    textgamelib.printDivider("-", 40)
    chapter1Challenge = input("Objective: Find The Light Switch\n")
    findLights = 0
    while findLights == 0:
        if "go" in chapter1Challenge.lower() and "light switch" in chapter1Challenge.lower():
            print("You walk towards the light switch")
            findLights += 1
        elif "go out of living room" in chapter1Challenge.lower():
            print("You can't really see well.")
            chapter1Challenge = input("Try finding the light switch\n")
        elif "go" in chapter1Challenge.lower() and "to room" in chapter1Challenge.lower():
            print("You have to get to school but first you need to turn on the lights. Something might be in the house.")
            chapter1Challenge = input("Try finding the light switch\n")
        else:
            print("I can't really understand what you are trying to do")
            chapter1Challenge = input("Try finding to light switch\n")
    textgamelib.printDivider("-", 40)
    chapter1Challenge = input("Try turning on the light switch\n")
    turnOnLights = 0
    while turnOnLights == 0:
        if "turn on" in chapter1Challenge.lower() and ("lights" in chapter1Challenge.lower() or "light" in chapter1Challenge.lower() or "light switch" in chapter1Challenge.lower()):
            playsound('c:\\Users\\molem\\Downloads\\Python Year 9 Coding\\MyGameDesign\\lightswitchclick.mp3')
            print("Nothing happened")
            turnOnLights += 1
        elif "turn on" in chapter1Challenge.lower():
            print("What are you trying to turn on?")
            chapter1Challenge = input("Try turning on the light switch\n")
        else:
            print("I can't really tell what you are tring to do.")
            chapter1Challenge = input("Try turning on the light switch\n")
    textgamelib.printDivider("-", 40)
    print("???: Oh there you are son\nYou turn around to see your father Jabari standing behind you.\nJabari: There's a really bad storm outside, flooding in a bunch of areas. The school is closed for today.\nYou were a bit happy because there would be no school but flooding was bad. You were wondering what you would do.\nJabari: Since it's still a school day, you should do some practice with your math and english. Luckily, the thing that you are studying in english is a book about me so you shouldn't have too much problem with that")
    print("Time to study a bit of math. Get 3 questions right to move on.")
    mathScore = 0
    while mathScore < 3:
        num1 = randint(1,100)
        num2 = randint(1,100)
        print("What is ", num1, "+ ", num2)
        answer1 = input()
        while not answer1.isnumeric():
            answer1 = input("Please type a number\n")
        answer1 = int(answer1)
        if answer1 == num1 + num2:
            print("Correct!")
            mathScore += 1
        else:
            print("Sorry, that's not right.")
        textgamelib.printDivider("-", 40)
    print("Jabari: Good Job! Since it's a special day out of school, we'll stop for today. It's time to look at the book Jabari Jumps!")
    englishQuiz = input("What was Jabari scared of?\n")
    englishScore = 0
    while englishScore == 0:
        if "jumping off" in englishQuiz.lower() and "diving board" in englishQuiz.lower():
            print("That is correct")
            englishQuiz = input("Who helped Jabari overcome his fear?\n")
            if "his" in englishQuiz.lower() and ("dad" in englishQuiz.lower() or "father" in englishQuiz.lower()):
                print("That is correct")
                englishQuiz = input("What did we learn about in Jabari Jumps?\n")
                if "bravery" in englishQuiz.lower() or "to be brave" in englishQuiz.lower() or "overcome your fears" in englishQuiz.lower():
                    print("That is correct")
                    englishScore += 1
                else:
                    print("That is not correct, try again.")
                    englishQuiz = input("What did we learn about in Jabari Jumps?\n")
            else:
                print("That is not correct, try again.")
                englishQuiz = input("Who helped Jabari overcome his fear?\n")
        else:
            print("That is not correct, try again.")
            englishQuiz = input("What was Jabari scared of?\n")
    textgamelib.printDivider("-", 40)
    print("Jabari: Good Job Son. It's nice to know that you know about me from my book. It's time to take a break and have fun. It's a day off, let's use it well!")
    textgamelib.printDivider("-", 40)
    chapter1EndingArt = tprint("End Of Chapter 1", font="bulbhead")
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 2:
    textgamelib.printDivider("-", 40)
    chapter2Art = tprint("Chapter 2", font="bulbhead")
    textgamelib.printDivider("-", 40)
    print("It's currently the afternoon and your dad Jabari is preparing a gas stove so that he could cook lunch.\nJabari: Hey son, could you do me a favour? I need you to open the windows in the kitchen, the living room, and the dining room. I need this so that we are safe to cook the food. Could you do that for me?")
    print("Objective: Open the windows in the living room, the kitchen and the dining room. You are in the \nkitchen. \nType 'Where am I' to find out where you are. The kitchen can only go to the dining room.")
    roomList = ["Kitchen", "Dining Room", "Living Room", "Your Bedroom", "Closet"]
    room = 0
    kitchenWindowOpen = False
    diningWindowOpen = False
    livingWindowOpen = False
    while kitchenWindowOpen == False or diningWindowOpen == False or livingWindowOpen == False:
        whichRoom = (roomList[room])
        if whichRoom == (roomList[0]):
            openWindows = input("What would you like to do? Type 'go out' to leave the kitchen. Type 'open window' to open the windows.\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and kitchenWindowOpen == False:
                kitchenWindowOpen = True
                print("You opened the window in the kitchen")
            elif "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and kitchenWindowOpen == True:
                print("The window is already open")
            elif "go out" in openWindows.lower():
                room += 1
                whichRoom = (roomList[room])
                print("You entered the", whichRoom)
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
            else:
                print("I can't really understand what you want to do.")
        if whichRoom == (roomList[1]):
            openWindows = input("What would you like to do?\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and diningWindowOpen == False:
                diningWindowOpen = True
                print("You opened the window in the dining room.")
            elif "open" in openWindows.lower() and "windows" in openWindows.lower() and diningWindowOpen == True:
                print("The window is already open")
            elif "go to" in openWindows.lower():
                whereGo = input("Where would you like to go? The Kitchen, the living room, your bedroom or the closet?\n")
                if "kitchen" in whereGo.lower():
                    room -= 1
                    print("You entered the kitchen.")
                elif "living room" in whereGo.lower():
                    room += 1
                    print("You entered the living room.")
                elif "bedroom" in whereGo.lower():
                    room += 2
                    print("You enter your bedroom but remember that you need to open the windows, you go back to the dining room.")
                    room -= 2
                elif "closet" in whereGo.lower():
                    room += 3
                    print("You check out the closet but remember you ned to open the windows, you head back out to the dining \nroom.")
                    room -= 3
                else:
                    print("I don't understand where you want to go.")
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
            else:
                print("I can't really understand what you want to do.")
        if whichRoom == (roomList[2]):
            openWindows = input("What would you like to do? Type 'go out' to leave the living room. Type 'open window' to open the \nwindows.\n")
            if "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and livingWindowOpen == False:
                livingWindowOpen = True
                print("You opened the window in the living room.")
            elif "open" in openWindows.lower() and ("windows" in openWindows.lower() or "window" in openWindows.lower()) and livingWindowOpen == True:
                print("The window is already open")
            elif "go out" in openWindows.lower():
                room -= 1
                whichRoom = (roomList[room])
                print("You entered the", whichRoom)
            elif "where am i" in openWindows.lower():
                print("The", whichRoom)
            else:
                print("I can't really understand what you want to do.")
    print("You head back to the kitchen where you see your father.\nJabari: Thanks son. I'm just going to start getting the stove ready. Could you head to the basement to get some beef?\nYou wanted to help but the basement was really dark and scary.")
    basementGo = input("Do you want to go to the basement to get food for your dad? Yes or No?\n")
    if "yes" in basementGo.lower():
        print("Jabari: Thanks so much, I know you are scared of the basement but it will help me cook more efficiently.")
    if "no" in basementGo.lower():
        print("Jabari: I understand that it is really scary the basement and I know you don't want to go but it would be great if you went.")
    print("In the end, your dad convinced you to go to the basement. You were scared of the dark but it was only to get some beef. It would be quick and easy to help your dad cook. Nothing's down there that will scare you...Right?")
    textgamelib.printDivider("-", 40)
    chapter2EndingArt = tprint("End Of Chapter 2", font="bulbhead")
    textgamelib.printDivider("-", 40)
    gameScore += 1
while gameScore == 3:
    chapter3Art = tprint("Chapter 3", font="bulbhead")
    textgamelib.printDivider("-", 40)
    print("You enter the basement to much of your discomfort. While you did agree to get the beef, you were still scared. Your dad said that the beef was in the top shelf of the fridge in the room left of the staircase.")
    print("Objective: Find the beef and get back upstairs. The is a door ahead and a door to the left.Type go to to choose which door to enter.")
    gotBeef = False
    whichRoom = "stairroom"
    if gotBeef == False:
        actionGetBeef = input("What would you like to do?\n")
        if "go to" in actionGetBeef:
            whichDoor = input("Which door would you like to enter? Left or Forward?\n")
            if "left" in whichDoor:
                print("You open and enter the left door. It's pretty dark so you can't really see but you can try inspecting the room to see what's in it.")
            if "forward" in whichDoor:
                print("You open and enter the door in front of you. It's pretty dark here so you can't see well but if you inspect the room you might find some things. Something smells and you thought you heard some growling. You left the room just to be safe.")
