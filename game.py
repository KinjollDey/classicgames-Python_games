## Creating a simple python based puzzle game:
from sys import exit

## Player Intro:
name = input("What's your name?  >>>")
print(f"Hello {name}. Welcome to the Game!!")

## Player consent:
print(f"Hello {name}, Since you are here do you want to carry on or leave")

## Play or leave Choice:
select = input("1.Play\n2.Leave\n>> ")


if select == "play":
    print("Well then, I could officially welcome you to the game of Life!!")
elif select == "leave":
    print("oh dear, you missed a great chance")
    exit(0)
else:
    exit("Learn to type")
    


## Game:
def play():
    print(f"Let's start the game then Mr. {name}.")
    print("Hope you've got what it takes.")
    print("A little bit favour from my side, Choose a game: game1 or game2 ?? ")

play()
## CHoice of game 1 or game 2
## user choice of game:
game = input("1. Game 1\n2. Game 2\n>>")
game = int(game) ## to convert choices from string to integers


## game1 built
def game_1():
    print("Let's get started!!!")
    print("""A table appears in the front with two bowls.
        One bowl has red coloured pills and the second one
        has blue coloured ones. It is obviously stated that you can only consume one
        of the two pills. These pills have powers that you might
        imbibe.
        """)
    pill = input("Which colour pill do you take?\nRed or Blue\n>>>") 
    
    if pill == "red":
        red_pill()
    elif pill == "blue":
        blue_pill()
## Testung Function game_pill
#game_pill()
## red pill function:
def red_pill(): ## Actions and proceeding for red pill.
    print("Now that you have consumed the red pill {} relax".format(name)) 
    print("You now have access to impressive superhuman strength")
    print(f"what would you now do with it MR. {name}")
    
    ## Choice of future
    intent = input("1.Would you visit a bank?\nOr\n2.Would you visit a museum?")
    intent = int(intent)
    
    ## Consequnces code block 
    if intent == 1:
        print("There's a scenario here!!\nThe bank is being robbed.")
        
        roberry = input("What would you do now?\n Stop the robbery\n Avoid the situation and wait\n ??")
        roberry = int(roberry)
        
        if roberry == 1:
            print("Good job {}".format(name))
            print("Would you now reveal your face??\nOr\nwould you keep a low profile")

            hero = input("1.Hero or 2. Shy??")
            hero = int(hero)
            if hero == 1:
                print("You have earned yourself fame!!")
            elif hero == 2:
                print("Watching from shadows?? That's a real superhero..!! ")
            else:
                exit_funct()
        
        elif roberry == 2:
            print("Okay!! Let's wait...")
            
            choice = input("They are running now what??\n 1. stop the robbers and take the money\n 2. stop the robbers and give away the money\n Choice is yours..>>")
            choice = int(choice)

            if choice == 1:
                print("You are stinky rich.. You bastard!!")
                exit(0)
            elif choice == 2:
                print("A real world robin hood!!!!")
                exit(0)
            else:
                print("You took too long.. They ran Away!!!")
                exit_funct()
        else:
            print("Took Too Long")
            exit_funct()

     ## Mesuem Choice conclusion       
    elif intent == 2:
        print(" There's nothing in the museum!!")
        print("You have wasted your time and soon you will be back to normal.")
        exit_funct()
    ## arbitary action    
    else:
        print("Too Long!!!")
        exit_funct()

## Blue Pill Function:
def blue_pill():
    print(f"Congrts {name}, you have gained invisibility.")
    print("how about you get to somewhere\nHow about your school or bar??")
    choice = input("The choice is yours...>>\n 1. School\n2.Bar")
    choice = int(choice)

    ## Consequence
    if choice == 1:
        print("That's nice!!")
        print(f" What would you do now {name}??")
        print("I will help... would you\n1.Steal the question paper\n2.Plant a prank\n???")

        ### User choice
        idea = input("1 or 2")
        idea = int(idea)

        ## Consequences
        if idea == 1:
            idea2 = input("What now? Leak the paper")
            if idea2 == "Yes":
                print("That's bad and you just got caught")
            elif idea2 == "No":
                print("That's fair!!")
            else:
                exit_funct()
        elif idea == 2:
            print("Thats gonna be super fun!!")
            exit(0)
        else:
            exit_funct()


## Else exit function on different user input
def exit_funct():
    print("One should learn to follow instructions..")
    exit(0)
    

        
## game2 built
def gold_room():
    print("There is a room filled with gold. How Much Would you take?")
    choice = input('Choose one >')


    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man. learn to type a Number.")


    if how_much < 50:
        print("Nice, You are not greedy, you win!!")
        exit(0)
    else:
        dead("You greedy bastard!!!")


def bear_room():
    print("There is a bear there!!!")
    print("The bear has a bunch of honey.")
    print("The Fat bear is in front of another door.")
    print("How are you going to move the bear??")
    bear_moved = False

    option = input("1. Take honey\n2. taunt bear\n3. open door")
    option = int(option)    

    if option == 1:
        dead("the Bear looks at you and then kills you.")

    elif option == 2 and not bear_moved:
        print("Congrats!! The bear has moved, you can go through.")
        bear_moved = True

    elif option == 2 and bear_moved:
        dead("The bear get pissed off and eats you!!")
    
    elif option == 3 and bear_moved:
        gold_room()
        
    else:
        print("I got no idea what that means..")


def cthulhu_room():
    print("Here is a great evil.")
    print("1. He stares at you and u go mad")
    print("2. Do you flee or eat your head??")

    choice = input(">")
    choice = int(choice)
    
    if 1 in choice:
        game_2()
    elif 2 in choice:
        dead("Well that was end")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job")
    exit(0)


def game_2():
    print(""" You are inside a dark room
            there is a door to your right and one to your left.
            CHoose one
            """)

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You suffocated.")    

## How to chang

## Choices consequences:
if game == 1:
    print(f"That's a confident choice you've made.")
    print("Welcome to the game of superpower Pills!!!")
    game_1()
elif game == 2:
    print(f"That's a confident choice you've made.")
    print("Puzzle is on the way")
    game_2()
else:
    exit_funct()