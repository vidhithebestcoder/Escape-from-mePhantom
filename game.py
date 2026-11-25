"""
ESCAPE FROM ME
This game is a game where you are kidnapped 
and then you have to try and escape from the kidnapper
rooms:
-Garden
-Kitchen
-Bedroom (where you start)
-Closet
-Living room
-Basement
-Dining room
"""
#Imports the library so I can use it
import random

# Introduction to the game
print("\n\nWelcome to Escape From Me By VIDHI SONI!!!")
print("You find yourself locked in a bedroom that is not yours.")
print("You find a note beside you.")
print("It says, 'You will find the door locked. I have kidnapped you.'")
print("To find your way out, you need to find all 6 keys.")
print("Every room has a key and to find the key, you need to solve the puzzle.")
print("Start with this room.")
print("Good luck!")

# Checks the number of keys and starts the variables
keys = 0
has_key1 = False
has_key2 = False
has_key3 = False
has_key4 = False
has_key5 = False
has_key6 = False

# BEDROOM
print("\nAfter you read the note, you start looking around for a challenge.")
print("You open the second drawer on the left and you find a note telling you to unscramble this phrase.")

while not has_key1:
    bedroom_answer = input("\nUnscramble this: hte dn2 wraerd ot het thigr: ").lower().strip()
    if bedroom_answer == "the 2nd drawer to the right" or bedroom_answer == "the":
        has_key1 = True
        keys += 1
        print("\nYou look in the second drawer to the right and find the key! Great Job!")
        print("You have", keys, "key so far!")
    else:
        print("\nTry again please! Make sure you wrote the whole thing out!")

# GARDEN
def enter_garden():
    global keys, has_key2
    print("\n\nYou open the door and find yourself outside.")
    print("You see a garden and walk up to it. You see another note.")
    print("If you plant this plant for me, I will show you where the key is.")
    print("First take the magical seed and push it into an empty spot in the soil.")
    print("Then water it and then make sure the sun is coming toward it.")
    
    while not has_key2:
        garden_answer = input("\n6 = Water it\n8 = Push the seed into the soil\n3 = Make sure the sun is coming toward it\nWhat order will you plant the seed? ").strip()
        if garden_answer == "863":
            has_key2 = True
            keys += 1
            print("\nYou watch the magical seed grow. After it's done, it pops out a key to the next door!")
            print("You have", keys, "keys so far!")
        else:
            print("Invalid answer, please try again.")

# KITCHEN
def enter_kitchen():
    global keys, has_key3
    print("\n\nThe next door you see opens up to a very messy kitchen.")
    print("You see a heavy 4-digit lock and you try a few combinations, but they don't work.")
    print("You open the fridge, the oven and some drawers but you don't see much.")
    print("Then you notice the microwave is set to 05:59 minutes.")
    
    while not has_key3:
        kitchen_answer = input("\nWhat code will you put into the lock? ").strip()
        if kitchen_answer == "0559":
            has_key3 = True
            keys += 1
            print("\nYou enter the code and the door unlocks! Great job!")
            print("You have", keys, "keys so far!")
        else:
            print("Look at the microwave timer. Don't forget the zero!")

# CLOSET
def enter_closet():
    global keys, has_key4
    batteries = False
    print("\n\nYou open the next door and find yourself in a pitch dark space.")
    print("You start to feel your way through and find a flashlight!")
    print("But it has no batteries.")
    
    while not has_key4:
        top_shelf = input("\nEnter 1 if you want to look on the top shelf or enter 2 if you want to look at the bottom shelf: ").strip()
        if top_shelf == "1":
            print("\nYou find some batteries! You can see now!")
            batteries = True
            print("You start looking for a key in the piles and piles of messy clothes.")
            print("Yes! You find the key in a coat pocket!")
            print("It works! You go out to the next adventure.")
            has_key4 = True
            keys += 1
            print("You have", keys, "keys so far!")
        elif top_shelf == "2":
            print("\nYou find some batteries, but they are not the ones for the flashlight. Maybe look up?")
        else:
            print("\nYou entered an invalid input. Please enter 1 or 2.")

# LIVING ROOM 
def enter_living_room():
    global keys, has_key5
    print("\n\nYou walk into the next room and it opens up to a living room.")
    print("There are some comfy couches and a TV where the family can sit and have fun.")
    print("You start searching and you find a note in the remote holder. It says . . . ")
    living_room_answer=input("I am tall when I am young, and short when I am old. What am I? ")
    if living_room_answer=="candle":
        print("You look at the candle and there was the key.")
        has_key5 = True
        keys += 1
        print("You have", keys, "keys so far!")
    else:
        print("Not really, think about something with wax in it that you light.")

# BASEMENT
def enter_basement():
    global keys, has_key6
    print("\n\nYou open the door and walk down the stairs to what seems like the basement")
    print("You notice a poster on the other side of the room.")
    print("It was for the band Neon 808")
    print("You see a lock on the next door. You walk up to it.")
    basement_answer=input("What code do you put into the lock?")
    if basement_answer=="808":
        print("Great job! You enetred the right code!")
        has_key6 = True
        keys += 1
        print("You have", keys, "keys so far!")
    else:
        print("You got it wrong. Maybe look at the poster and write that code.")

# DINING ROOM
def enter_dining_room():
    global keys, has_key7
    print("\n\nYou open the door and walk upatairs and find yourself to the dining room.")
    print("There is so much food on the table and your parents are here. ")
    print("You enjoy dinner and you are surprised that your long lost uncle tricked you")
    print("and made you do the entire escape room for fun.")

# Main Game Loop 
while keys < 6:
    if not has_key2:
        enter_garden()
    if not has_key3:
        enter_kitchen()
    if not has_key4:
        enter_closet()
    if not has_key5:
        enter_living_room()
    if not has_key6:
        enter_basement()

print("\n\nCONGRATULATIONS! You found all the keys and escaped!")