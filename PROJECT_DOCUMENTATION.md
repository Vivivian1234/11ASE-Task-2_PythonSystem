# **11SE Assesment Task 2 2025 - Text Based Adventure**

### By Vivian Ding
---
---
<br>

# **Sprint 1- 11/6/25**
## **Requirements Definition**

### *Functional Requirements*

* The application should be able to import data and consistently update the player's progress
* The application should be able to use classes and objects to model entities
* The application should be able to accept user inputs and should validate inputs and handle invalid inputs without breaking
* The application should be able to handle errors and not crash

### *Non-Functional Requirements*

* The application should be able to respond to uer inputs and update the game state without delays
* The application should be able to reliale and consistent without any unexpected behaviour during normal gameplay.
* The application should be clear and easily understandable with clear prompts and messages.
* The application should be stored securely to prevent corruption or unauthorised access.
* The application should be able to work on multiple platforms.

## __Determining Specifications__
---
### *Functional Specifications*

* The user navigates through different rooms using directional commands ("n", "e", "s", "w").
* The user can interact with objects in specific contects for story purposes ("use", "eat", "talk", "play").
* The user can view their inventory by typing "show".
* The user can view items in their inventory through viewing the inventory.

* The system displays descriptions of the current location and available options.
* The system updates the player inventory every time the uer gains or loses an item.
* The system tracks what has been completed (keys collected, items found, etc).


### *Non-functional Specifications*

* The user can re enter past rooms and the decription will be changed according to what is in their inventory and past events.
* The user can enter rooms with no story purpose except to disadvange themselves.
*  The user can view items decriptions in their inventory when not used.

### *Use cases*

1. Room Navigation
* Player selects a direction available (n/e/s/w)
*  Application sends player there and describes the room.

2. View Inventory
*  Player views inventory by typing "show"
*  Application lists all items in the inventory and it's quantities.

3. Use Item
*  Player uses an object in a specific scenario
*  Application checks if it's valid or not, and proceeds from there.

## __Design__

### *Storyboard*
*  Player enters cellar
*  Player enters the east hallway, which leads to the bathroom and dog room
*  Player finds bone in the bathroom
*  Player enters dog room and gets the dog the bone
*  Player finds key1 and a laser pen

### *Data Flow Diagram*

#### DFD Level 0

![Sprint1_Level0](/images.py/Sprint1_Level_0.png)

#### DFD Level 1
![Sprint1_Level0](/images.py/Sprint1_Level_1.png)


### **Structure Chart**
![Structure_Chart](/images.py/Structure_Chart.png)

### Gantt Chart
![Gantt_chart](/images.py/Gantt_chart.png)

## __Build and Test__
---
```python
# Dictionary to store the player's inventory and item counts
player_inventory = {
    "water bottle": 2,
    "broken bottle holder": 1,
    "wine cork": 1
}

def inventory():
    """
    Displays and manages the player's inventory.

    This function allows the player to view their current inventory and select an item to use.
    Using an item may cause a description to be printed and potentially remove the item from the inventory.
    The function loops until the user types 'exit'.

    Side Effects:
        - makes `player_inventory` accessible by making it global in this function.
        - Prints to the console.
        - Handles in-game item interactions based on player input.
    """
    global player_inventory

    while True:
        print("\n---Inventory---\n")
        if player_inventory:
            for item, number in player_inventory.items():
                print(f"{item} x {number}")
        else:
            print("Your inventory is empty!")
            return

        use = input("\nWhat would you like to use? (type 'exit' to quit)\n> ").lower()

        if use == "exit":
            return

        if use in player_inventory:
            if player_inventory[use] > 0:
                
                if use == "water bottle":
                    player_inventory[use] -= 1
                    print("You grab the tiny bottle of water from your pocket and drink it in one gulp.\n"
                          "Your thirst is quenched slightly, but your throat still feels dry and scratchy.")
                    print(f"\nYou used one {use}.")
                    
                    if player_inventory[use] == 0:
                        print(f"\nYou have no more {use}s left. Removing it from inventory.")
                        del player_inventory[use]

                elif use == "broken bottle holder":
                  print("You awkwardly wave the broken bottle holder. It's mostly useless. You wonder why you still have it.")

                elif use == "wine cork":
                  print("You stare at the cork. It stares back.")
                    
                elif use == "key 1":
                  print("You take out the shiny golden key out of your backpack. The glittering '1' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                

                elif use == "bone":
                  print("The bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")
                  
                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it awat for now, in case you accientally burn off one of your fingers.")

            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nInvalid request. Please try again.")

#Spawn text
def main():

    """
    Starts the game and prompts the player for their name.

    This function introduces the game setting, asks the player for their name, 
    and starts the game by entering the Cellar.
    
    Side Effects:
        - Prints to the console.
        - Takes user input for the player's name.
        - Moves to Cellar() function to begin.
    """

  print("You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so lonely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")
  
  name = input("What is your name?\n").lower()
  name = name.capitalize()

  print("Good, at least you remember your name.\n")

  Cellar()

#First room
def Cellar():

    """
    The main starting room (the Cellar) in the game.

    Displays room description and provides options to move to different hallways
    or check inventory. The goal is to find 3 keys to unlock the southern door.

    Side Effects:
        - Accepts player input to navigate to other rooms.
        - Calls other room functions.
    """

    while True:
        print("\n---The Cellar---")
        print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()

        if action == "show":
            inventory()
        elif action == "e":
            HallwayEast()
        elif action == "w":
            HallwayWest()
        elif action == "n":
            HallwayNorth()
        elif action == "s":
            lockedRoom()
        else:
            print("You don't think you can go that way right now.")
        
def HallwayEast():
    """
    The eastern hallway.

    Provides the player with options to explore the Dog Room, Bathroom,
    or return to the Cellar.

    Side Effects:
        - Navigates between rooms by user's input.
    """
    while True:
        print("\n---HallwayEast---")
        print("There are two rooms down this hallway, a dog room to the north and a bathroom continuing east. You can also return to the cellar back to the west.")
        action = input("\nWhat do you want to do? Options: show, n, e, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
            DogRoom()
        elif action == "e":
            Bathroom()
        elif action == "w":
            Cellar()
        else:
            print("You don't think you can go that way right now.")

# Key1 and laser here
# Lose bone
def DogRoom():

    """
    The Dog Room with a hostile dog.

    If the player has a 'bone', they can use it to calm the dog, 
    freeing it and gaining a key and a laser pen. Once resolved, the the dog leaves and the room is empty.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Interacts with game items and progression.
        - Prints narrative and takes user input.
    """

    while True:
        print("\n---Dog Room---")

        if "laser pen" in player_inventory:
            print("You see the now empty room, with the scent of fur and meat in the air. A metal pole remained in the middle of the empty room. Thank goodness the dog was free from the prison.")
            print("There is no more need to be here. You return to the East Hallway.")
            HallwayEast()
            return

        print("You enter a room with a huge black dog with glowing red eyes. You don’t notice the dog at first, its fur color blending in with the shadows. As you approach, it barks aggressively at you. You realize it’s tied to a pole with a metal chain. The dog howls in pain as you reach forward.")

        if 'bone' in player_inventory:
            print("But his mouth is watering when he spots the bone in your pouch.\n")

        action = input("\nWhat do you want to do? Options: use, s\n").lower()

        if action == "use":

            if "bone" not in player_inventory:
                print("There is nothing helpful in your inventory right now, best come back later to find something suitable.")
            else:
                use_what = input("Use what?\n").lower()
                if use_what == "bone":
                    print("The black doggo gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off who knows where and reveals a key underneath the spot he was standing on. You pick up the key and a small black pen left behind.")
                    
                    player_inventory["bone"] -= 1
                    if player_inventory["bone"] == 0:
                        del player_inventory["bone"]

                    player_inventory["key 1"] = player_inventory.get("key 1", 0) + 1
                    player_inventory["laser pen"] = player_inventory.get("laser pen", 0) + 1

                    print("You used the bone. 'key 1' and 'laser pen' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. The dog stares reproachfully at you, hungry yet still hostile.")

        elif action == "s":
            HallwayEast()
            return

        else:
            print("Invalid option.")

# bone here
def Bathroom():
    """
    The Bathroom room.

    They collect a bone the first time they enter here.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Provides a branching narrative based on collected items.
        - Prints to the console and prompts user input.
    """

    print("\n---Bathroom---")

    if "key 2" in player_inventory:
        print("The grimy walls and dirty floor are an unpleasant sight.")
        print("There is no more need to be here. You return to the East Hallway.")
        HallwayEast()
        return

    if "bone" not in player_inventory:
        print("You enter a broken down bathroom, completely unusable. There’s mold on the toilet and sink, the shower head is smashed. The once-white tiles are now brown, covered in dirt and grime. And… what is that white thing sticking out of the sink?")
        print("You approach the sink, and see a bone lying inside. It doesn't seem human...maybe it came from a butcher? Hopefully? You're unsure when you place it in your backpack.")
        print("'bone' added to our backpack.")
        player_inventory["bone"] = player_inventory.get("bone", 0) + 1
        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your inventory that may be helpful.")
        print("\nYour updated backpack:")
        inventory()
        print("You exit the room.")
        HallwayEast()
        return

    if "lever" in player_inventory:
        print("Nothing seems out of the ordinary, except for the stench and the mould everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do?")

        while True:
            action = input("\nWhat do you want to do? Options: use, s\n").lower()

            if action == "use":
                use_what = input("Use what?\n").lower()
                if use_what == "lever":
                    print("The mirror swings open and reveals a small hole containing a key. You grab it and swing the mirror back shut. The cold key in your hands has a small '2' on it. You place it in your backpack. \n")
                    player_inventory["lever"] -= 1
                    if player_inventory["lever"] == 0:
                        del player_inventory["lever"]

                    player_inventory["key 2"] = player_inventory.get("key 2", 0) + 1

                    print("You used the lever. 'key 2' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. You stare at the cracked relfection of you in the mirror, and you swear it is looking at you weirdly.")
            elif action == "s":
                print("You exit the room.")
                HallwayEast()
                return
            else:
                print("Invalid option.")
    else:
        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your inventory that may be helpful.")
        print("You exit the room.")
        HallwayEast()
        return
```
## __Review__
---

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.

So far, my code has met most of the functional requirements regarding the inventory systen, as items can be added and used in certain situations. I can travel between the rooms easily, so the room navigation concept is complete, and the interactive user options have been fufilled wheneever there are options.  Some fufilled non-functional requirements include it's usability, performance and error handiling, which is good to see.

I know I am missing a lot of things right now, but I will implement them later now that I have an idea of how this system should work.

### 2. Analyse the performance of your program against the key use-cases you identified.

The output of the program's current code is correct and what is to be expected. It responds to the user's inputs quickly and effectively, with no errors at all. The user can freely move between connected rooms smoothly, view their inventory when they want too and and can interact with objects.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability.

The code is structured well as it is organised and logically. All variables are named descriptively and the story is well formatted. Each room is it's own function which makes it very easy to manage and easily shared across structures, as well as global variables. The basic "What do you want to do?" line is easy to understand and can be applied anywhere, so that is a positive thing.  would say the quality is passable right now, but I will see in the future as I don't know how much text I will have all together.

### 4. Explain the improvements that should be made in the next stage of development.

I will add the second hallway to the code (HallwayNorth), which will have more rooms. I will make the code a little more open so user's can choose to explore around in new rooms without affecting the story. I'll add a lot more story in the next sprint as I feel it is currently lacking.

# **Sprint 2- 11/6/25**

## __Design__

### *Storyboard*
*  Player enters cellar
*  Player enters the east hallway, which leads to the bathroom and dog room
*  Player finds bone in the bathroom
*  Player enters dog room and gets the dog the bone
*  Player finds key1 and a laser pen
*  Player returns to east hallway
*  Player returns to cellar
*  Player enters north hallway, which leads to the cafe, Andy's beadroom and partyroom.
*  Player enters Andy's room
*  Player recieves a coin to buy coffee
*  PLayer returs to the north hallway
*  Player enters cafe
*  Player buys coffee
*  Player returns to the north hallway
*  Player enter's Andy's room
*  Player recieves lever and note
*  Clue in note leads to bathroom
*  Player returns to the north hallway
*  Player returns to the cellar
*  Player enters the east hallway
*  Player enters bathroom
*  Player uses lever on mirror
*  Player finds key 2

### **Structure Chart**


### **Algorithm**

```
BEGIN GetKeyFromDogRoom
    Start in Cellar
    East to HallwayEast
    East to Bathroom
    EnterBathroom()
    West to HallwayEast
    North to DogRoom
    GiveBoneToDog()
    END
End GetKeyFromDogRoom
```

### **Subroutine**

```
BEGIN EnterBathroom
        Output "You entered the bathroom."
        IF bone exists in Bathroom then
            Add "bone" to inventory
            Remove "bone" from Bathroom
            Output "You picked up a bone."
        ElSE
            Output "There is nothing to pick up."
        ENDIF
END EnterBathroom
```

### **Subroutine**

```

BEGIN GiveBoneToDog
    If "bone" is in inventory then
        Remove "bone" from inventory
        Add "key1" to inventory
        Add "laser pen" to inventory
        Output "You gave the bone to the dog."
        Output "You received key1 and a laser pen!"
    
    ELSE
        Output "The dog growls... you have nothing to give."
    ENDIF
END GiveBoneToDog

```


### **Structure Chart**


### Gantt Chart
![Gantt_chart](/images.py/Gantt_chart.png)

## __Build and Test__
---
```python
# Dictionary to store the player's inventory and item counts
party_room_cake = False

slices = 0
slices_left = 8 - slices

player_inventory = {
    "water bottle": 2,
    "broken bottle holder": 1,
    "wine cork": 1
}

def inventory():

    """
    Displays and manages the player's inventory.

    This function allows the player to view their current inventory and select an item to use.
    Using an item may cause a description to be printed and potentially remove the item from the inventory.
    The function loops until the user types 'exit'.

    Side Effects:
        - makes `player_inventory` accessible by making it global in this function.
        - Prints to the console.
        - Handles in-game item interactions based on player input.
    """

    global player_inventory

    while True:
        print("\n---Inventory---\n")
        if player_inventory:
            for item, number in player_inventory.items():
                print(f"{item} x {number}")
        else:
            print("Your inventory is empty!")
            return

        use = input("\nWhat would you like to use? (type 'exit' to quit)\n> ").lower()

        if use == "exit":
            return

        if use in player_inventory:
            if player_inventory[use] > 0:

                if use == "water bottle":
                    player_inventory[use] -= 1
                    print("You grab the tiny bottle of water from your pocket and drink it in one gulp.\n"
                          "Your thirst is quenched slightly, but your throat still feels dry and scratchy.")
                    print(f"\nYou used one {use}.")

                    if player_inventory[use] == 0:
                        print(f"\nYou have no more {use}s left. Removing it from inventory.")
                        del player_inventory[use]

                elif use == "broken bottle holder":
                  print("You awkwardly wave the broken bottle holder. It's mostly useless. You wonder why you still have it.")

                elif use == "wine cork":
                  print("You stare at the cork. It stares back.")

                elif use == "key 1":
                  print("You take out the shiny golden key out of your backpack. The glittering '1' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")

                elif use == "key 2":
                  print("You take out the shiny golden key out of your backpack. The glittering '2' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")


                elif use == "bone":
                  print("The bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")

                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it awat for now, in case you accientally burn off one of your fingers.")

                elif use == "coffee":
                  print("You hold the warm cup of coffee in your hands, the aroma heavenly. You would drink it... but rememeber that you're severely allergic to coffee. A pity.")

                elif use == "lever":
                  print("You pull out the small and suprisingly light metal lever from your pocket. It reminds you a but of a Minecraft lever, and you wonder where that thought came fron. Anyway, you ponder where this could be used...")

                elif use == "coin":
                  print("The small coin is shiny and warm in your hands. It's fun to play with, as much fun as a coin can be in such a dull environment. Losing it wouldn't be the best idea...you put it away for now.")

                elif use == "note":
                  print("You take out the scribbled note. It reads:")
                  print("'Look at me and I'll look at you,") 
                  print("No matter what, no matter who,")
                  print("You'll always see that there'll be two.")
                  print("To find the key, you must know yourself well.")
                  print("If you don't, you'll be locked in this cell!")
                  print("What am I?'")
                  print("You think about this riddle, and a few answers are possible...but only one answer appears clear as day. You know it...and it's in the bathrooom!")

            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nInvalid request. Please try again.")

#Spawn text
def main():

    """
    Starts the game and prompts the player for their name.

    This function introduces the game setting, asks the player for their name, 
    and starts the game by entering the Cellar.
    
    Side Effects:
        - Prints to the console.
        - Takes user input for the player's name.
        - Moves to Cellar() function to begin.
    """

  print("You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so lonely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")

  name = input("What is your name?\n").lower()
  name = name.capitalize()

  print("Good, at least you remember your name.\n")

  Cellar()

#First room
def Cellar():

    """
    The main starting room (the Cellar) in the game.

    Displays room description and provides options to move to different hallways
    or check inventory. The goal is to find 3 keys to unlock the southern door.

    Side Effects:
        - Accepts player input to navigate to other rooms.
        - Calls other room functions.
    """

    while True:
        print("\n---The Cellar---")
        print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()

        if action == "show":
            inventory()
        elif action == "e":
            HallwayEast()
        elif action == "w":
            HallwayWest()
        elif action == "n":
            HallwayNorth()
        elif action == "s":
            lockedRoom()
        else:
            print("You don't think you can go that way right now.")

def HallwayEast():
    """
    The eastern hallway.

    Provides the player with options to explore the Dog Room, Bathroom,
    or return to the Cellar.

    Side Effects:
        - Navigates between rooms by user's input.
    """
    while True:
        print("\n---HallwayEast---")
        print("There are two rooms down this hallway, a dog room to the north and a bathroom continuing east. You can also return to the cellar back to the west.")
        action = input("\nWhat do you want to do? Options: show, n, e, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
            DogRoom()
        elif action == "e":
            Bathroom()
        elif action == "w":
            Cellar()
        else:
            print("You don't think you can go that way right now.")

# Key1 and laser here
# Lose bone
def DogRoom():

    """
    The Dog Room with a hostile dog.

    If the player has a 'bone', they can use it to calm the dog, 
    freeing it and gaining a key and a laser pen. Once resolved, the the dog leaves and the room is empty.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Interacts with game items and progression.
        - Prints narrative and takes user input.
    """

    while True:
        print("\n---Dog Room---")

        if "laser pen" in player_inventory:
            print("You see the now empty room, with the scent of fur and meat in the air. A metal pole remained in the middle of the empty room. Thank goodness the dog was free from the prison.")
            print("There is no more need to be here. You return to the East Hallway.")
            HallwayEast()
            return

        print("You enter a room with a huge black dog with glowing red eyes. You don’t notice the dog at first, its fur color blending in with the shadows. As you approach, it barks aggressively at you. You realize it’s tied to a pole with a metal chain. The dog howls in pain as you reach forward.")

        if 'bone' in player_inventory:
            print("But his mouth is watering when he spots the bone in your pouch.\n")

        action = input("\nWhat do you want to do? Options: use, s\n").lower()

        if action == "use":

            if "bone" not in player_inventory:
                print("There is nothing helpful in your inventory right now, best come back later to find something suitable.")
            else:
                use_what = input("Use what?\n").lower()
                if use_what == "bone":
                    print("The black doggo gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off who knows where and reveals a key underneath the spot he was standing on. You pick up the key and a small black pen left behind.")

                    player_inventory["bone"] -= 1
                    if player_inventory["bone"] == 0:
                        del player_inventory["bone"]

                    player_inventory["key 1"] = player_inventory.get("key 1", 0) + 1
                    player_inventory["laser pen"] = player_inventory.get("laser pen", 0) + 1

                    print("You used the bone. 'key 1' and 'laser pen' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. The dog stares reproachfully at you, hungry yet still hostile.")

        elif action == "s":
            HallwayEast()
            return

        else:
            print("Invalid option.")

# bone here
def Bathroom():
    """
    The Bathroom room.

    They collect a bone the first time they enter here.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Provides a branching narrative based on collected items.
        - Prints to the console and prompts user input.
    """

    print("\n---Bathroom---")

    if "key 2" in player_inventory:
        print("The grimy walls and dirty floor are an unpleasant sight.")
        print("There is no more need to be here. You return to the East Hallway.")
        HallwayEast()
        return

    if "bone" not in player_inventory:
        print("You enter a broken down bathroom, completely unusable. There’s mold on the toilet and sink, the shower head is smashed. The once-white tiles are now brown, covered in dirt and grime. And… what is that white thing sticking out of the sink?")
        print("You approach the sink, and see a bone lying inside. It doesn't seem human...maybe it came from a butcher? Hopefully? You're unsure when you place it in your backpack.")
        print("'bone' added to our backpack.")
        player_inventory["bone"] = player_inventory.get("bone", 0) + 1
        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your inventory that may be helpful.")
        print("\nYour updated backpack:")
        inventory()
        print("You exit the room.")
        HallwayEast()
        return

    if "lever" in player_inventory:
        print("Nothing seems out of the ordinary, except for the stench and the mould everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do?")

        while True:
            action = input("\nWhat do you want to do? Options: use, s\n").lower()

            if action == "use":
                use_what = input("Use what?\n").lower()
                if use_what == "lever":
                    print("The mirror swings open and reveals a small hole containing a key. You grab it and swing the mirror back shut. The cold key in your hands has a small '2' on it. You place it in your backpack. \n")
                    player_inventory["lever"] -= 1
                    if player_inventory["lever"] == 0:
                        del player_inventory["lever"]

                    player_inventory["key 2"] = player_inventory.get("key 2", 0) + 1

                    print("You used the lever. 'key 2' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. You stare at the cracked relfection of you in the mirror, and you swear it is looking at you weirdly.")
            elif action == "s":
                print("You exit the room.")
                HallwayEast()
                return
            else:
                print("Invalid option.")
    else:
        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your inventory that may be helpful.")
        print("You exit the room.")
        HallwayEast()
        return

def HallwayNorth():

    """
    The northern hallway of the map.

    Offers navigation options to a party room, Andy’s bedroom, and a café.
    Allows the player to return to the Cellar or check their inventory.

    Side Effects:
        - Routes player to other rooms based on input.
    """

    while True:
        print("\n---HallwayNorth---")
        print("There are three rooms down this hallway, a party room to the east, a bedroom with a messy sign with 'Andy' scribbled on it to the west, and a cafe continuing north. You can also return to the cellar back to the south.")
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()
        if action == "show":
          inventory()
        elif action == "n":
          Cafe()
        elif action == "e":
          PartyRoom()
        elif action == "s":
          Cellar()
        elif action == "w":
          AndyRoom()
        else:
          print("You don't think you can go that way right now.")

def Cafe():

    """
    Represents the Café room with the Friendly Barista.

    The player can buy coffee if they have a coin, which is used later to progress the game.
    The barista responds differently depending on the player's inventory.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Progresses narrative depending on item usage.
        - Displays dialogue and prompts for interaction.
    """

    while True:
        print("---Cafe---")

        if "coffee" in player_inventory:
            print("You look around. You do not need to do anything here. Friendly Barista is staring blankly at a wall. Let's give the coffee to Andy to get the clue about the keys. You decide to leave.")
            HallwayNorth()
            return

        if "note" in player_inventory:
            print("You look around. You do not need to do anything here. Friendly Barista is staring blankly at a wall. Has Andy been down here this whole time? If so, surely he has talked the the Friendly Barista before to order more coffee right?")
            print("You ask the barista about Andy. He smiles back blankly, not saying a single word, his eyes seemingly looking past you to the opposite wall. You decide to leave.")
            HallwayNorth()
            return

        if "coin" in player_inventory:
            print("You enter the brightly lit and calming cafe.")
            print("A barista with calm, blank eyes greets you, staring into your eyes with something less than human.")
            print("'Greetings, I am Friendly Barista. Would you like buy some coffee? It's one Cuppa Coin.'")
            print("You see the huge coin drawing behind him on the wall, silver with a coffee cup engraved on it. The coin Andy gave you is identical.")

            action = input("\nWhat do you want to do? Options: use, s\n").lower()

            if action == "use":
                use_what = input("Use what?\n").lower()
                if use_what == "coin":
                    print("You hand over the small coin, and Friendly Baraista gives you piping hot coffee in a simple paper cup. You gladly accept the coffee and hold on to it. You can't drink it, because you just so happened to be allergic to coffee. Oh well, at least it's warm. You put it away. \n")

                    player_inventory["coin"] -= 1
                    if player_inventory["coin"] == 0:
                        del player_inventory["coin"]

                    player_inventory["coffee"] = player_inventory.get("coffee", 0) + 1

                    print("You used the coin. 'coffee' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayNorth()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. Friendly Barista stares at you, smiling.")
            elif action == "s":
                print("You exit the room.")
                HallwayNorth()
                return
            else:
               print("Invalid option.")

        print("You enter a spotless and well furnished cafe, the clean wooden floors and light blue wallpaper decorated with a flower mural making it seem out of place, so comfortable and homely compared to the rest of this dark and gloomy underground structure you are in.")
        print("A barista with calm, blank eyes greets you, staring into your eyes with something less than human.")
        print("'Greetings, I am Friendly Barista. Would you like buy some coffee? It's one Cuppa Coin.'")
        print("You see a huge coin drawing behind him on the wall, silver with a coffee cup engraved on it. That must be the currency to buy a coffee.")
        print("You ask about the kidnapping and keys but he acts clueless, but still smiling as laid back as ever.")

        action = input("\nWhat do you want to do? Options: use, s\n").lower()

        if action == "use":
            print("There is nothing helpful in your inventory right now, best come back later to find something suitable.")
        elif action == "s":
            HallwayNorth()
            return
        else:
            print("Invalid option.")

def AndyRoom():

    """
    Represents Andy's bedroom, where the player meets Andy.

    Andy exchanges important items like a coin, lever, and a clue note
    depending on whether the player has given him coffee.
    Returns the player to HallwayNorth afterward.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Displays story progression and character dialogue.
    """

    while True:
        print("---AndyRoom---")

        if "note" in player_inventory:
            print("You enter the dirty room again. Andy is happily drinking the coffee, much less tired looking already. There isn't anything left here do, and you should leave Andy with this coffee in peace...")
            print("You exit the room.")
            HallwayNorth()
            return

        if "coffee" in player_inventory:
            print("You enter the room with a warm cup of coffee in your hands. Andy wakes up to the sound of footsteps, and you hand it to him.")
            print("'Thanks!' he cheers, happily gulping down the coffee with great delight. 'Oh wait, right, the clue...'")
            print("He pulls out a small note from his pants pocket and rummages through on of the drawers and pulls out what seems to be... a lever?")
            print("He hands them both to you, when you give the small lever a confused look, he shrugs, returning to his coffee.")
            print("You put the lever in your backback at read the scribbled note.")
            print(" It reads:\n")
            print("'Look at me and I'll look at you,") 
            print("No matter what, no matter who,")
            print("You'll always see that there'll be two.")
            print("To find the key, you must know yourself well.")
            print("If you don't, you'll be locked in this cell!")
            print("What am I?'")
            print("You think about this riddle, and a few answers are possible...but only one answer appears clear as day. You know it...and it's in the bathrooom!")

            player_inventory["coffee"] -= 1
            if player_inventory["coffee"] == 0:
                del player_inventory["coffee"]

            player_inventory["lever"] = player_inventory.get("lever", 0) + 1
            player_inventory["note"] = player_inventory.get("note", 0) + 1

            print("You used the coffee. 'lever' and 'note' added to your backpack.")
            print("\nYour updated backpack:")
            inventory()
            print("\nThere is nothing left to do here. You exit the room.")
            HallwayNorth()
            return

        if "coin" in player_inventory:
            print("You enter the dirty room again. Andy is still lying on his bed, and the softest of snores tell you he's somehow fallen asleep already. Best to go get him some coffee...")
            print("You exit the room.")
            HallwayNorth()
            return

        print("You enter a dirty room full of mould, sweaty and dirty clothes, empty, unwashed coffee mugs and yellowed open books. It reeks of coffee and expired milk. You see a tired guy in a bad mood sitting on his bed rubbing his face.")
        print("'Ugh... I'm so tired...' he groans.")
        print("You ask about the keys.")
        print("'Oh... gimme a coffee and I'll give you a clue to the key...zzz' he lies flat on his bed, yawning widely.")
        print("'Oh right...take these. The name's Andy by the way.' He hands you a small silver coin, with a small coffee cup engraved on it.")
        print("Is this...money? Is this how you buy the coffee? Alright...you put it away.")

        player_inventory["coin"] = player_inventory.get("coin", 0) + 1

        print("\nYour updated backpack:")
        inventory()
        print("\nBest to go get Andy some coffee.. You exit the room.")
        HallwayNorth()
        return

# Eat 3 slices, you restart the whole game.
def PartyRoom():

    """
    The Party Room with a clown and a mysterious cake.

    The player can eat cake slices, talk to the clown, or leave. Eating too much cake
    results in restarting the game. Talking to the clown provides a warning.

    Side Effects:
        - Can trigger a game restart after eating three slices.
        - Provides narrative clues and tension through dialogue and interaction.
    """

    global party_room_cake

    while True:
        print("---PartyRoom---")

        if party_room_cake == True:
            print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, who is wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
            print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
            print("On the table, there is a 5-layer birthday cake.")
            print("It looks and smells a bit stale, but would still undoubtably be delicious.")
            print(f'There are {slices_left} slices left of the cake.')
            print("You reach for the cake, but a unnerving chill runs down your spine, and your appetite has disappeared completely. Now, for some strange reason, you feel repulsed by the cake, and want to leave as soon as possible.")
            print("You leave the room.")
            HallwayNorth()
            return

        print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, who is wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
        print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
        print("On the table, there is a 5-layer birthday cake.")
        print("It looks and smells a bit stale, but would still undoubtably be delicious.")
        if slices == 0:
            print("There are 8 large slices on the table, cut perfectly for you to grab.")
        else:
            print(f'There are {slices_left} large slices on the plate, ready for you to grab.')
        print("Your mouth waters as you approach it, but as you get closer, you realise the sugary icing spells out 'HAPPY BIRTHDAY; DO NOT EAT ME'.")
        print("The cake looks so appetizing, and you're so hungry.")
        print("Would it hurt just to take a single slice?")
        print("Should you go talk to the quiet clown watching you?")

        action = input("\nWhat do you want to do? Options: show, eat, talk, w\n").lower()
        if action == "show":
            inventory()

	elif action == "talk":
            print("You try to start a conversation with the tall clown that is eyeing you. You ask about the 5-layer cake with the strange iced message. The tall clown nods, and warns you not to eat the cake. He looks like he is on the verge of tears, his watery eyes sparkling and his delicate voice trembling. Was eating the cake that dangerous? Oh well. The clown seems really desperate for you to not eat the cake, so you leave the cake and the party room. As you close the door, you hear a huge sigh of relief from the tall clown.")
            print("You exit the room.")
            HallwayNorth()
            return
        elif action == "w":
            print("As you close the door, you hear a huge sigh of relief from the tall clown. You exit the room.")
            HallwayNorth()
            return

        while action == "eat":

            if slices == 3:
                print("Each slice of the cake is delicious and filling, and every bite of it makes you feel more addictive.")
                print("Suddenly, you feel sick, and sway dangerously on your feet, and then the impact of falling to the ground on your knees.")
                print("Your head is spinning, and you try to stand back up again, your legs shaking.")
                print("The turn your head around frantically, trying to ask for help. The clown is no where in your sight.")
                print("You slowly stand up, still feeling extremely nausous, and then a picece of cloth is wrapped around your head, suffocating you, the subtle sweet smell lingering as you fall into darkness.")
                ##--------------------------------------------------------------
            
            slices = slices + 1
            
            print("You take a slice of the huge cake and have a huge bite.")
            print("Wow.")
            print("It. Is. Delicious.")
            print("After finishing the slice, you turn around to look at the clown still staring at you, and you see a face of true horror etched across his face.")
            print("'Please...' he begged quietly,'Please stop eating. You will regret every slice you take.")
            print("You are unsure what to do. Should you keep eating or leave the room?")

            action = input("\nWhat do you want to do? Options: show, eat, talk, w\n").lower()

            if action == "show":
                inventory()

            elif action == "talk":
                print("You try to start a conversation with the tall clown that is eyeing you. You ask about the 5-layer cake with the strange iced message. The tall clown nods, and warns you not to eat the cake. He looks like he is on the verge of tears, his watery eyes sparkling and his delicate voice trembling. Was eating the cake that dangerous? Oh well. The clown seems really desperate for you to not eat the cake, so you leave the cake and the party room. As you close the door, you hear a huge sigh of relief from the tall clown.")
                print("You exit the room.")
                HallwayNorth()
                return
            elif action == "w":
                print("As you close the door, you hear a huge sigh of relief from the tall clown. You exit the room.")
                HallwayNorth()
                return

        else:
            print("You don't think you can go that way right now.")

```
## __Review__
---

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.

My code is similar to the last sprint related to the requirements, as I added 3 more rooms more for the story part of the system.  The navigation between the rooms is smooth and correct, the inventory management is identical to the last, but with extra informtaion for the new items, and there are much more interactions for this code. The performance has not changed in any way which is reasssuring to hear, proving the system's realiability.

I am still missing many things neccessary for the final code, but right now I am slowly building up to it.

### 2. Analyse the performance of your program against the key use-cases you identified.

The output for the system is just as expected and high performing as there were no large changes that could affect it's performance. The program is the same as it was before, so it's performance is just as good, if net better because of the new code and implementations.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability.

The code is still as structured and organised as before, all following a logical pattern. Maintaining the inentory is simple and not annoying, but I have noticed that the readability of the story may be a bit harder to follow because of the sudden increase in text. I wrote more per room which may also lead disatisfaction, and I will see how I can try to deal with it in the next sprint, depending on how much text there is and how it works for me.

### 4. Explain the improvements that should be made in the next stage of development.

I will add much more complicated code in the next stage of development to fit in the criteria of the functional and non-functional requirements. I am thinking of adding the inheritance code, so I will have to improve the current strcuture and code of my system for that to happen.

# **Sprint 3- 19/6/25**

## __Design__

### *Storyboard*
*  Player enters cellar
*  Player enters the east hallway, which leads to the bathroom and dog room
*  Player finds bone in the bathroom
*  Player enters dog room and gets the dog the bone
*  Player finds key1 and a laser pen
*  Player returns to east hallway
*  Player returns to cellar
*  Player enters north hallway, which leads to the cafe, Andy's beadroom and partyroom.
*  Player enters Andy's room
*  Player recieves a coin to buy coffee
*  PLayer returs to the north hallway
*  Player enters cafe
*  Player buys coffee
*  Player returns to the north hallway
*  Player enter's Andy's room
*  Player recieves lever and note
*  Clue in note leads to bathroom
*  Player returns to the north hallway
*  Player returns to the cellar
*  Player enters the east hallway
*  Player enters bathroom
*  Player uses lever on mirror
*  Player finds key 2
*  Player return to east hallway
*  Player returns to cellar
*  Player enters west hallway
*  Player enters kitchen
*  Player cooks pizza and gets cookbook
*  Player returns to the west hallway
*  Player enters librabry
*  Player ends cookbok
*  Plays fights for the 3rd
*  Player wins and finds key 3
*  Player return to the west hallway
*  Player return to cellar
*  Player open the locked rom

### *UML diagram*
![UML_diagram](/images.py/UML_diagram.png)
??? made this up completely


## __Build and Test__
---
```python
import copy
import random
import sys

from weapon import water_bottle, broken_bottle_holder, wine_cork, laser_pen, cookbook, coffee, lever, coin, note, helpful_casino_reminder, socks, Key1, Key2, Key3, bone
from weapon import create_weapon

found_bone = False

has_entered_casino = False

has_entered_kitchen = False

has_entered_library = False

UNFINISHED_FIGHT = False

party_room_cake = False
slices = 0
slices_left = 8 - slices

key_count = 0

player_inventory = {
    "water bottle": {"count": 2, "weapon": water_bottle()},
    "broken bottle holder": {"count": 1, "weapon": broken_bottle_holder()},
    "wine cork": {"count": 1, "weapon": wine_cork()}
}

def add_to_inventory(name, amount=1):
    name = name.lower()
    if name in player_inventory:
        player_inventory[name]["count"] += amount
    else:
        player_inventory[name] = {
            "count": amount,
            "weapon": create_weapon(name)
        }

def inventory():

    """
    Displays and manages the player's inventory.

    This function allows the player to view their current inventory and select an item to use.
    Using an item may cause a description to be printed and potentially remove the item from the inventory.
    The function loops until the user types 'exit'.

    Side Effects:
        - makes `player_inventory` accessible by making it global in this function.
        - Prints to the console.
        - Handles in-game item interactions based on player input.
    """


    global player_inventory

    while True:
        print("\n---Inventory---\n")
        if player_inventory:
            for item, info in player_inventory.items():
                print(f"{item} x {info['count']}")
        else:
            print("Your backpack is empty!")
            return

        use = input("\nWhat would you like to use? (type 'exit' to quit)\n> ").lower()

        if use == "exit":
            return

        if use in player_inventory:
            if player_inventory[use]["count"] > 0:
                if use == "water bottle":
                    player_inventory[use]["count"] -= 1
                    print("You grab the tiny bottle of water from your pocket and drink it in one gulp.\n"
                          "Your thirst is quenched slightly, but your throat still feels dry and scratchy.")
                    print(f"\nYou used one {use}.")

                    if player_inventory[use]["count"] == 0:
                        print(f"\nYou have no more {use}s left. Removing it from your backpack.")
                        del player_inventory[use]

                elif use == "broken bottle holder":
                    print("You awkwardly wave the broken bottle holder. It's mostly useless. You wonder why you still have it.")

                elif use == "wine cork":
                    print("You stare at the cork. It stares back.")
                    
                elif use == "key1":
                  print("You take the shiny golden key out of your backpack. The glittering '1' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                
                elif use == "key2":
                  print("You take the shiny golden key out of your backpack. The glittering '2' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                
                elif use == "key3":
                  print("You take the shiny golden key out of your backpack. The glittering '3' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and hopefully you can use them to get into the locked room by the cellar to get out of here.")

                elif use == "bone":
                  print("The bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")
                  
                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it away for now, in case you accidentally burn off one of your fingers.")

                elif use == "cookbook":
                  print("You browse the endless delicious recipes in every one of the 198 pages, interested. Maybe you could try these recipes later.")

                elif use == "coffee":
                  print("You hold the warm cup of coffee in your hands, the aroma heavenly. You would drink it... but remember that you're severely allergic to coffee. A pity.")
                
                elif use == "lever":
                  print("You pull out the small and surprisingly light metal lever from your pocket. It reminds you a bit of a Minecraft lever, and you wonder where that thought came from. Anyway, you ponder where this could be used...")

                elif use == "coin":
                  print("The small coin is shiny and warm in your hands. It's fun to play with, as much fun as a coin can be in such a dull environment. Losing it wouldn't be the best idea...you put it away for now.")

                elif use == "note":
                  print("You take out the scribbled note. It reads:")
                  print("'Look at me and I'll look at you,") 
                  print("No matter what, no matter who,")
                  print("You'll always see that there'll be two.")
                  print("To find the key, you must know yourself well.")
                  print("If you don't, you'll be locked in this cell!")
                  print("What am I?'")
                  print("You think about this riddle, and a few answers are possible...but only one answer appears clear as day. You know it...and it's in the bathroom!")

                elif use == "helpful casino reminder":
                    print("A helpful little reminder about yourself:")
                    print("'This machine runs on hope... Your funds are insufficient. Maybe check on that.'")
                
                elif use == "socks":
                    print("You hold the white socks in your hand. They're a little small for you. Such an incredible prize indeed.")

            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nInvalid request. Please try again.")

#Spawn text
def main():

    """
    Starts the game and prompts the player for their name.

    This function introduces the game setting, asks the player for their name, 
    and starts the game by entering the Cellar.
    
    Side Effects:
        - Prints to the console.
        - Takes user input for the player's name.
        - Moves to Cellar() function to begin.
    """

  print("\nYou wake up, the last thing you remember is suffocating in gas-filled fabric, closing in from behind. This place looks familiar, you have definitely been here some time before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so lonely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")
  
  name = input("What is your name?\n").lower()
  name = name.capitalize()

  print("Good, at least you remember your name.\n")

  Cellar()

#First room
def Cellar():

    """
    The main starting room (the Cellar) in the game.

    Displays room description and provides options to move to different hallways
    or check inventory. The goal is to find 3 keys to unlock the southern door.

    Side Effects:
        - Accepts player input to navigate to other rooms.
        - Calls other room functions.
    """

    while True:
    print("\n---The Cellar---")
    print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")
           
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()

        if action == "show":
            inventory()
        elif action == "n":
            HallwayNorth()        
        elif action == "e":
            HallwayEast()
        elif action == "s":
            LockedRoom()        
        elif action == "w":
            HallwayWest()
        else:
            print("You don't think you can go that way right now.")

def LockedRoom():
    """
    Handles interaction with the locked final room.
    Checks if the player has collected all three keys. 
    If so, allows access to the final room (DIAMOND_ROOM), otherwise prompts the player to search more.
    Offers options to show inventory, try to open the door, or return to the cellar.
    """
    
    global key_count

    keys_left = 3 - key_count

    print ("\n---Locked Room---\n")

    print("You try to open the locked door, but it doesn't budge at all. The three keyholes labelled '1', '2', and '3' above the handle show that you must have all 3 keys to open the door.\n")

    if key_count == 3:
        print("You have all 3 keys in your backpack.")

    else:
        if keys_left == 1:
            print(f'You have {key_count} keys. You need {keys_left} key left to find.')
        else:
            print(f'You have {key_count} keys. You need {keys_left} keys left to find.')

    while True:
        action = input("\nWhat do you want to do? Options: show, open, n\n").lower()

        if action == "show":
            inventory()      
        elif action == "open":
            if key_count == 3:
                print("\nYou open the door.")
                DIAMOND_ROOM()
            else:
                print("You do not have enough keys.")
                print("You should search for them.")
                print("You return to the cellar.")
                Cellar()
                return

        elif action == "n":
            Cellar()
            return
        else:
            print("Invalid option.")
    
def DIAMOND_ROOM():
    """
    Represents the final sequence of the game.
    Allows the player to use the laser pen to open a safe containing a mysterious diamond.
    Triggers the game ending if the correct item is used, leading to the end and program exit.
    """

    global sys

    print("You enter a really small room with walls coated in black paint, giving the illusion of entering a void of emptiness.")
    print("In front of you on a table covered by a black table cloth is a large metal safe, with no opening you can see.")
    print("You're sure the thing in the safe must be able to help you escape, but you don't know how. How could you break a safe like this? It seems indestructible.")
    print("Hey...what about you try your laser pen? There's no harm in trying.")
    print("But you leave the door open behind you, just in case.")

    while True:
        action = input("\nWhat do you want to do? Options: use\n").lower()
        if action == "use":
            while True:
                print("Use what?\n\nYour Backpack:")
                for item, info in player_inventory.items():
                    print(f"- {item} (x{info['count']})")
                use_what = input(">")

                if use_what == "laser pen":

                    print("\nYou aim the laser pointer at the safe, and turn it on. The bright beam of red blinds you for a second, but you hold it steadily and try to sear the side off it.")
                    print("After a little while, you see the heat damage the safe slowly, and after a long time the side of the safe falls off (finally, your arms are getting tired!) and you peer inside the safe cautiously.")
                    print("Inside is a huge round cut diamond on a triangular stand, bigger than your head.")
                    print("You carefully take it out by the stand, and push the safe off the table to marvel at the jewel.")
                    print("It seems to shine millions of nonexistent colours across the walls from the dim light of the cellar behind you, and it gives you instant hope and calm.")

                    if "helpful casino reminder" in player_inventory:
                        print("(Ha, that helpful casino reminder was WRONG, I have plenty of hope!!!)")

                    print("You have no idea why this diamond is doing here, and how it'll help you escape, but you should try something.")
                    print("You reach your hand tentatively to touch it when you suddenly hear a bark behind you. You turn around to see the dog from before bounding up to you, tail wagging happily. It jumps up into your chest and you catch it with your other arm, accidentally brushing it with the fingers of your outstretched hand.")
                    
                    print("You hear a soft buzzing sound, and your mind feels like it's being pulled across dimensions; you can't see anything but pitch darkness, when you land on something extremely soft and comfortable.")
                    print("You open your eyes the tiniest bit as tiredness overwhelms you, and the puppy still cradled in your arms, warm and soft. You think you see the faint outlines of your bedroom before you fall asleep.\n")

                    print("You wake up and turn on the morning news with your new best friend Teddy at your side. The huge headlines reads:")
                    print("FRIENDLY BARISTA, TIRED 'ANDY' GUY, PIZZA CHEF GUY AND TALL CLOWN KILLED IN FREAK ACCIDENT. AUTHORITIES STILL INVESTIGATING CAUSE OF DEATH.")
                    print("\n")
                    print("\n")
                    print("\n")
                    sys.exit()

                else:
                    print(f'You try to use the {use_what}, but it does nothing. Surely the laser pen is worth a go at least...')

        else:
            print("Invalid option (You are SO close to the end!!!)")

def HallwayEast():
    """
    The eastern hallway.

    Provides the player with options to explore the Dog Room, Bathroom,
    or return to the Cellar.

    Side Effects:
        - Navigates between rooms by user's input.
    """
    while True:     

        print("\n---HallwayEast---")
        print("There are two rooms down this hallway. A dog room to the north and a bathroom continuing east. You can also return to the cellar back to the west.")
        
        action = input("\nWhat do you want to do? Options: show, n, e, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
            DogRoom()
        elif action == "e":
            Bathroom()
        elif action == "w":
            Cellar()
        else:
            print("You don't think you can go that way right now.")

# Key1 and laser here
# Lose bone
def DogRoom():

    """
    The Dog Room with a hostile dog.

    If the player has a 'bone', they can use it to calm the dog, 
    freeing it and gaining a key and a laser pen. Once resolved, the the dog leaves and the room is empty.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Interacts with game items and progression.
        - Prints narrative and takes user input.
    """

    
    global key_count
    
    print("\n---Dog Room---")

    if "laser pen" in player_inventory:
        print("You see the now empty room, with the scent of fur and meat in the air. A metal pole remains in the middle of the empty room. Thank goodness the dog is free from the prison.")
        print("There is no more need to be here. You return to the East Hallway.")
        HallwayEast()
        return

    print("You enter a room with a huge black dog with glowing red eyes. At first, you don’t notice the dog, its dark fur blending into the shadows. As you approach, it barks aggressively at you. You realize it’s tied to a pole with a metal chain. The dog howls in pain as you reach forward.")

    if 'bone' in player_inventory:
        print("But its mouth waters when it spots the bone in your pouch.\n")

    action = input("What do you want to do? Options: use, s\n").lower()

    if action == "use":

        if "bone" not in player_inventory:
            print("There is nothing helpful in your backpack right now, best come back later to find something suitable.")
        
        else:
            while True:
                print("Use what?\n\nYour Backpack:")
                for item, info in player_inventory.items():
                    print(f"- {item} (x{info['count']})")
                use_what = input(">")

                if use_what == "bone":
                    print("The black dog gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off who knows where and reveals a key underneath the spot he was standing on. You pick up the key and a small black pen. It looks delicate, so you are careful when you pick it up, afraid of damaging it. The fancy writing on the pen read 'Laser Pen'. Laser Pen? Really? You put both items in your pocket.")
                                    
                    player_inventory["bone"]["count"] -= 1
                    if player_inventory["bone"]["count"] == 0:
                        del player_inventory["bone"]

                    add_to_inventory("key1")
                    add_to_inventory("laser pen")

                    key_count = key_count + 1

                    print("You used the bone. 'key1' and 'laser pen' added to your backpack.")
                    print("\nYour updated backpack:")
                    
                    for item, info in player_inventory.items():
                        print(f"- {item} (x{info['count']})")
                        
                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. The dog stares reproachfully at you, hungry yet still hostile.")

    elif action == "s":
        print("You exit the room.")
        HallwayEast()
        return

    else:
        print("Invalid option.")

# bone here
def Bathroom():
    """
    The Bathroom room.

    They collect a bone the first time they enter here.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Provides a branching narrative based on collected items.
        - Prints to the console and prompts user input.
    """

    global found_bone
    global key_count

    print("\n---Bathroom---")

    if "lever" in player_inventory:
        print("Nothing seems out of the ordinary, except for the stench and the mold everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do?")

        while True:
            action = input("\nWhat do you want to do? Options: use, s\n").lower()

            if action == "use":
                print("Use what?\n\nYour Backpack:")
                for item, info in player_inventory.items():
                    print(f"- {item} (x{info['count']})")
                use_what = input(">")

                if use_what == "lever":
                    print("The mirror swings open and reveals a small hole containing a key. You grab it and swing the mirror back shut. The cold key in your hands has a small '2' engraved  on it. You place it in your backpack.\n")

                    player_inventory["lever"]["count"] -= 1
                    if player_inventory["lever"]["count"] == 0:
                        del player_inventory["lever"]

                    add_to_inventory("key2")
                    key_count += 1

                    print("You used the lever. 'key2' added to your backpack.")
                    print("\nYour updated backpack:")
                    inventory()

                    print("\nThere is nothing left to do here. You exit the room.")
                    HallwayEast()
                    return
                else:
                    print(f"You try to use the {use_what}, but it does nothing. You stare at your cracked reflection in the mirror, and you swear it is looking at you weirdly.")

            elif action == "s":
                print("You exit the room.")
                HallwayEast()
                return

            else:
                print("Invalid option.")

    if "key1" in player_inventory or "key2" in player_inventory:
        print("The grimy walls and dirty floor are an unpleasant sight.")
        print("There is no more need to be here. You return to the East Hallway.")
        HallwayEast()
        return

    if not found_bone:
        print("You enter a broken down bathroom, completely unusable. There’s mold on the toilet and sink, the shower head is smashed. The once-white tiles are now brown, covered in dirt and grime. And… what is that white thing sticking out of the sink?")
        print("You approach the sink, and see a bone lying inside. It doesn't seem human...maybe it came from a butcher? Hopefully? You're unsure when you place it in your backpack.")
        print("'bone' added to our backpack.")

        add_to_inventory("bone")
        found_bone = True

        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your backpack that may be helpful.")
        print("\nYour updated backpack:")
        inventory()

    else:
        print("You feel like there is something hiding in here, but you don't know what. Maybe come back later when you have a few more items in your backpack that may be helpful.")

    print("You exit the room.")
    HallwayEast()
    return



def HallwayNorth():

    """
    The northern hallway of the map.

    Offers navigation options to a party room, Andy’s bedroom, and a café.
    Allows the player to return to the Cellar or check their inventory.

    Side Effects:
        - Routes player to other rooms based on input.
    """

    while True:

        print("\n---HallwayNorth---")
        print("There are three rooms down this hallway. A party room to the east, a bedroom with a messy sign that has 'Andy' scribbled on it to the west, and a cafe continuing north. You can also return to the cellar back to the south.")
            
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
          Cafe()
        elif action == "e":
          PartyRoom()
        elif action == "s":
          Cellar()
        elif action == "w":
          AndyRoom()
        else:
          print("You don't think you can go that way right now.")
        
def Cafe():

    """
    Represents the Café room with the Friendly Barista.

    The player can buy coffee if they have a coin, which is used later to progress the game.
    The barista responds differently depending on the player's inventory.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Progresses narrative depending on item usage.
        - Displays dialogue and prompts for interaction.
    """

    while True:
        print("---Cafe---")

        if "coffee" in player_inventory:
            print("You look around. You do not need to do anything here. Friendly Barista is staring blankly at a wall. Let's give the coffee to Andy to get the clue about the keys. You decide to leave.")
            HallwayNorth()
            return

        if "note" in player_inventory:
            print("You look around. You do not need to do anything here. Friendly Barista is staring blankly at a wall. Has Andy been down here this whole time? If so, surely he has talked the Friendly Barista before to order more coffee right?")
            print("You ask the barista about Andy. He smiles back blankly, not saying a single word, his eyes seemingly looking past you to the opposite wall. You decide to leave.")
            HallwayNorth()
            return

        if "coin" in player_inventory:
            print("You enter the brightly lit and calming cafe.")
            print("A barista with calm, blank eyes greets you, staring into your eyes with something less than human.")
            print("'Greetings, I am Friendly Barista. Would you like to buy some coffee? It's one Cuppa Coin.'")
            print("You see the huge coin drawing behind him on the wall, silver with a coffee cup engraved on it. The coin Andy gave you is identical.")
        
            while True:
                action = input("\nWhat do you want to do? Options: use, s\n").lower()

                if action == "use":
                    while True:

                        print("Use what?\n\nYour Backpack:")
                        for item, info in player_inventory.items():
                            print(f"- {item} (x{info['count']})")
                        use_what = input(">")
                        
                        if use_what == "coin":
                            print("You hand over the small coin, and Friendly Barista gives you piping hot coffee in a simple paper cup. You gladly accept the coffee and hold on to it. You can't drink it, because you just so happened to be allergic to coffee. Oh well, at least it's warm. You put it away. \n")
                            
                            player_inventory["coin"]["count"] -= 1
                            if player_inventory["coin"]["count"] == 0:
                                del player_inventory["coin"]

                            add_to_inventory("coffee")

                            print("You used the coin. 'coffee' added to your backpack.")
                            print("\nYour updated backpack:")
                            
                            for item, info in player_inventory.items():
                                print(f"- {item} (x{info['count']})")
                                
                            print("\nThere is nothing left to do here. You exit the room.")
                            HallwayNorth()
                            return
                        else:
                            print(f"You try to use the {use_what}, but it does nothing. Friendly Barista stares at you, smiling.")
                elif action == "s":
                    print("You exit the room.")
                    HallwayNorth()
                    return
                else:
                    print("Invalid option.")

        print("You enter a spotless and well-furnished cafe, the clean wooden floors and light blue wallpaper decorated with a flower mural making it seem out of place, so comfortable and homely compared to the rest of this dark, gloomy underground structure.")
        print("A barista with calm, blank eyes greets you, staring into your eyes with something less than human.")
        print("'Greetings, I am Friendly Barista. Would you like to buy some coffee? It's one Cuppa Coin.'")
        print("You see a huge coin drawing behind him on the wall, silver with a coffee cup engraved on it. That must be the currency to buy a coffee.")
        print("You ask about the kidnapping and keys but he acts clueless, still smiling as laid-back as ever.")

        while True:
            action = input("\nWhat do you want to do? Options: use, s\n").lower()
            
            if action == "use":
                print("There is nothing helpful in your backpack right now, best come back later to find something suitable.")
            elif action == "s":
                print("You exit the room.")
                HallwayNorth()
                return
            else:
                print("Invalid option.")

def AndyRoom():

    """
    Represents Andy's bedroom, where the player meets Andy.

    Andy exchanges important items like a coin, lever, and a clue note
    depending on whether the player has given him coffee.
    Returns the player to HallwayNorth afterward.

    Side Effects:
        - `player_inventory` accessible by making it global.
        - Displays story progression and character dialogue.
    """

    while True:
        print("---AndyRoom---")

        if "note" in player_inventory:
            print("You enter the dirty room again. Andy is happily drinking the coffee, much less tired looking already. There isn't anything left here to do, and you should leave Andy with this coffee in peace...")
            print("You exit the room.")
            HallwayNorth()
            return
        
        if "coffee" in player_inventory:
            print("You enter the room with a warm cup of coffee in your hands. Andy wakes up to the sound of footsteps, and you hand it to him.")
            print("'Thanks!' he cheers, happily gulping down the coffee with great delight. 'Oh wait, right, the clue...'")
            print("He pulls out a small note from his pants pocket and rummages through one of the drawers and pulls out what seems to be... a lever?")
            print("He hands them both to you, when you give the small lever a confused look, he shrugs, returning to his coffee.")
            print("You put the lever in your backpack and read the scribbled note.")
            print(" It reads:\n")
            print("'Look at me and I'll look at you,") 
            print("No matter what, no matter who,")
            print("You'll always see that there'll be two.")
            print("To find the key, you must know yourself well.")
            print("If you don't, you'll be locked in this cell!")
            print("What am I?'")
            print("\nYou think about this riddle, and a few answers are possible...but only one answer appears clear as day. You know it...and it's in the bathroom!!!\n")

            player_inventory["coffee"]["count"] -= 1
            if player_inventory["coffee"]["count"] == 0:
                del player_inventory["coffee"]

            add_to_inventory("lever")
            add_to_inventory("note")

            print("You used the coffee. 'lever' and 'note' added to your backpack.")
            print("\nYour updated backpack:")
            
            for item, info in player_inventory.items():
                print(f"- {item} (x{info['count']})")
            
            print("\nThere is nothing left to do here. You exit the room.")
            HallwayNorth()
            return
        
        if "coin" in player_inventory:
            print("You enter the dirty room again. Andy is still lying on his bed, and the softest of snores tell you he's somehow fallen asleep already. Best to go get him some coffee...")
            print("You exit the room.")
            HallwayNorth()
            return
        
        print("You enter a dirty room full of mould, sweaty and dirty clothes, empty, unwashed coffee mugs and yellowed open books. The room reeks of coffee and expired milk. You see a tired guy in a bad mood sitting on his bed rubbing his face.")
        print("'Ugh... I'm so tired...' he groans.")
        print("You ask about the keys.")
        print("'Oh... gimme a coffee and I'll give you a clue to the key...zzz' he lies flat on his bed, yawning widely.")
        print("'Oh right...take these. The name's Andy by the way.' He hands you a small silver coin, with a small coffee cup engraved on it.")
        print("Is this...money? Is this how you buy the coffee? Alright...you put it away into your backpack")

        add_to_inventory("coin")

        print("\nYour updated backpack:")
        
        for item, info in player_inventory.items():
            print(f"- {item} (x{info['count']})")
            
        print("\nBest to go get Andy some coffee... You exit the room.")
        HallwayNorth()
        return

def PartyRoom():

    """
    The Party Room with a clown and a mysterious cake.

    The player can eat cake slices, talk to the clown, or leave. Eating too much cake
    results in restarting the game. Talking to the clown provides a warning.

    Side Effects:
        - Can trigger a game restart after eating three slices.
        - Provides narrative clues and tension through dialogue and interaction.
    """

    global party_room_cake
    global slices
    global slices_left
    global player_inventory

    global has_entered_casino
    global has_entered_kitchen
    global has_entered_library
    global UNFINISHED_FIGHT

    global key_count
    
    print("---PartyRoom---")

    if party_room_cake == True:
        print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
        print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
        print("On the table, there is a 5-layer birthday cake.")
        print("It looks and smells a bit stale, but would still undoubtedly be delicious.")
        print(f'There are {slices_left - 1} slices left of the cake.')
        print("You reach for the cake, but an unnerving chill runs down your spine, and your appetite disappears completely. Now, for some strange reason, you feel repulsed by the cake, and want to leave as soon as possible.")
        print("You leave the room.")
        HallwayNorth()
        return

    print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
    print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
    print("On the table, there is a 5-layer birthday cake.")
    if slices == 0:
        print("There are 8 large slices on the table, cut perfectly for you to grab.")
    else:
        print(f'There are {slices_left} large slices on the plate, ready for you to grab.')
    print("Your mouth waters as you approach it, but as you get closer, you realise the sugary icing spells out 'HAPPY BIRTHDAY; DO NOT EAT ME'.")
    print("The cake looks so appetising, and you're so hungry.")
    print("Would it hurt just to take a single slice?")
    print("Should you go talk to the quiet clown watching you?")

    while True:
        action = input("\nWhat do you want to do? Options: show, eat, talk, w\n").lower()

        if action == "show":
            inventory()

        elif action == "talk":
            print("You try to start a conversation with the tall clown that is eyeing you. You ask about the 5-layer cake with the strange iced message. The tall clown nods, and warns you not to eat the cake. He looks like he is on the verge of tears, his watery eyes sparkling and his delicate voice trembling. Was eating the cake that dangerous? Oh well. The clown seems really desperate for you to not eat the cake, so you leave the cake and the party room. As you close the door, you hear a huge sigh of relief from the tall clown.")
            print("You exit the room.")
            HallwayNorth()
            return

        elif action == "w":
            print("As you close the door, you hear a huge sigh of relief from the tall clown. You exit the room.")
            HallwayNorth()
            return

        elif action == "eat":
            if slices_left == 6:
                print("\nEach slice of the cake is delicious and filling, and every bite of it makes you feel more addicted.")
                print("Suddenly, you feel sick, and sway dangerously on your feet, and then feel the impact of falling to the ground on your knees.")
                print("Your head is spinning, and you try to stand back up again, your legs shaking.")
                print("Then you slowly stand up, still feeling extremely nauseous, and a piece of cloth is wrapped around your head, suffocating you, the subtle sweet smell lingering as you fall into darkness.\n")

                player_inventory = {
                    "water bottle": {"count": 2, "weapon": water_bottle()},
                    "broken bottle holder": {"count": 1, "weapon": broken_bottle_holder()},
                    "wine cork": {"count": 1, "weapon": wine_cork()}
                }

                party_room_cake = True

                has_entered_casino = False

                has_entered_kitchen = False

                has_entered_library = False

                UNFINISHED_FIGHT = False

                key_count = 0


                main()
                return
            else:
                slices += 1
                slices_left -= 1

                print("You take a slice of the huge cake and have a huge bite.")
                print("Wow.")
                print("It. Is. Delicious.")
                print("After finishing the slice, you turn around to look at the clown still staring at you, and you see a face of true horror etched across his face.")
                print("'Please...' he begs quietly, 'Please stop eating. You will regret every slice you take.'")
                print("You are unsure what to do. Should you keep eating or leave the room?")

        else:
            print("Invalid option.")

def HallwayWest():

    """
    Handles player interaction in the Hallway West room.
    Provides navigation options to Kitchen, Casino, Library, or back to the Cellar.
    """

    while True: 

        print("\n---HallwayWest---")
        print("There are three rooms down this hallway. A kitchen to the north, a casino to the south, and a library continuing west. You can also return to the cellar back to the east.")

        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
            Kitchen()
        elif action == "e":
            Cellar()
        elif action == "s":
            Casino()
        elif action == "w":
            Library()
        else:
            print("You don't think you can go that way right now.")

def Kitchen():
    """
    Manages the Kitchen room logic.
    Allows player to interact with ingredients, view cookbook case, and attempt to cook pizza recipes.
    Unlocks cookbook item if the correct recipe is made.
    """

    pizza_margherita = ["thin", "tomato", "mozzarella", "basil"]
    pizza_pepperoni = ["thick", "tomato", "parmesan", "pepperoni"]
    pizza_cheese = ["thin", "tomato", "provolone", "none"]

    global has_entered_kitchen

    print("\n---Kitchen---")

    if "cookbook" in player_inventory:
        print("You enter the huge kitchen and see the empty case where the cookbook was. You like this room; making pizza is fun, and it gave you a lot of food to fill you back up.")
        print("There is nothing left to do in the room.")
        print("You exit the room.")
        HallwayWest()
        return

    if "cookbook" not in player_inventory:
        if has_entered_kitchen == True:
            print("You enter the huge kitchen with a gleaming marble counter and vintage wall lights.")
            print("You see the ingredients that you found were piled on the counter. You probably should make the pizza for the cookbook...")

        if has_entered_kitchen == False:
            has_entered_kitchen = True
            print("You enter a huge kitchen with a gleaming marble counter and vintage wall lights. There is a sticky note on the counter that says:\n")
            print("'Make and deliver me a pizza, and the code to the cookbook is yours.'\n")
            print("You look around the pristine kitchen, and notice on a table in a corner is a small see-through case is a cookbook. The case is extremely sturdy and doesn't break when you apply force to it, so it seems the only way to acquire the cookbook is to enter a 4 digit code on the side of the case.")
            print("The cookbook seems to be specifically 198 pages, with a light blue hardcover that has a cartoon of a fruit bowl on top of it. It's labelled 'Common Cooking Skills: Edition 2'")
            print("You're unsure why you need a cookbook exactly, but it could be important later, you suppose.")
            print("You look back at the note, thinking.")
            print("You don't know who this 'me' person the note could be addressing, but you don't want to mess up this pizza and getting into more trouble.\n")
            print("You look into all the shelves and cupboards, and eventually have a small collection of ingredients available.")
            

        while True:
            pizza = []

            action = input("\nWhat do you want to do? Options: show, cook, s\n").lower()

            if action == "show":
                inventory()
            elif action == "cook":
                print("\nYou know 3 basic pizza recipes: margherita, pepperoni and cheese.")
                print("There is only enough dough to make one pizza, so choose one to make and use the correct ingredients.")
                print("You will add the ingredients in the order: dough, sauce, cheese, toppings\n")
                
                print("Recipes:")
                print("Margherita: thin, tomato, mozzarella, basil")
                print("Pepperoni: thick, tomato, parmesan, pepperoni")
                print("Cheese: thin, tomato, provolone, none")

                print("\n-Dough options-")
                
                while True:
                    dough = input("thin/thick: \n").lower()
                    if dough in ["thin", "thick"]:
                        pizza.append(dough)
                        break
                    else:
                        print("Invalid option.")

                print("\n-Sauce-")
                while True:
                    sauce = input("avocado, tomato, banana: \n").lower()
                    if sauce in ["avocado", "tomato", "banana"]:
                        pizza.append(sauce)
                        break
                    else:
                        print("Invalid option.")

                print("\n-Cheese-")
                while True:
                    cheese = input("mozzarella, parmesan, provolone: \n").lower()
                    if cheese in ["mozzarella", "parmesan", "provolone"]:
                        pizza.append(cheese)
                        break
                    else:
                        print("Invalid option.")

                print("\n-Toppings-")
                while True:
                    toppings = input("pepperoni, basil, none: \n").lower()
                    if toppings in ["pepperoni", "basil", "none"]:
                        pizza.append(toppings)
                        break
                    else:
                        print("Invalid option.")

                print("\nYou finished making the pizza.")
                print(f'Your pizza: {",".join(pizza)}')

                if pizza == pizza_margherita:
                    print(f'Margherita: {",".join(pizza_margherita)}')
                    kitchen_cooked()
                    break
                elif pizza == pizza_pepperoni:
                    print(f'Pepperoni: {",".join(pizza_pepperoni)}')
                    kitchen_cooked()
                    break
                elif pizza == pizza_cheese:
                    print(f'Cheese: {",".join(pizza_cheese)}')
                    kitchen_cooked()
                    break

                else:
                    print("It seems you messed up your pizza somehow. Hmm.")
                    print("Well, you've used your ingredients, but you're not sure what to do...\n")
                    
                    print("Suddently, you hear a loud THUNK behind you, and you see more ingredients somehow appeared behind you onto the central table, the exact amount that you used for your pizza.")
                    print("You have no idea how the ingredients have appeared (perhaps it fell from the ceiling? But there doesn't seem to be any trapdoor up there), but there's no point of thinking about it.")
                    print("You eat your pizza, filling full for the first time in a long time.")

                    print("Do you want to try to make another pizza, or leave?")
                        
            elif action == "s":
                print("You exit the room.")
                HallwayWest()
                return
            
            else:
                print("Invalid option")
            
def kitchen_cooked():
    """
    Handles the event that occurs after successfully cooking a correct pizza recipe.
    Gives the player the cookbook item and returns them to the hallway.
    """

    print("\nYour pizza looks perfect and smells delicious.")
    print("You hear a quiet 'ding' in the room, and suddenly, a hole appears in the side of the wall, evidently a chute leading off somewhere. You carefully place the pizza you made on the plate provided and it gets sucked in, quickly disappearing.")
    print("The hole closes up for a moment, then opens again to spit out another small sticky note, before closing fully with a soft clang.\n")
    print("It reads:")
    print("'Thank you for the pizza! It's really good :D")
    print("Anyway, here's the 4 digit code to the case to access the cookbook:")
    print("4196'\n")
    print("You turn around and walk towards the locked case, and input '4196'. The lock clicks open and you take the very specific 198 page cookbook, pleased.")
    
    add_to_inventory("cookbook")

    print("'cookbook' added to your backpack.")
    print("\nYour updated backpack:")
    
    for item, info in player_inventory.items():
        print(f"- {item} (x{info['count']})")
    
    print("\nThere is nothing left to do here. You exit the room.")
    HallwayWest()
    return

def Casino():
    """
    Handles logic for the Casino room.
    Introduces a lottery mechanic with increasing odds and a guaranteed win after 20 draws.
    Grants player a 'socks' item after winning and permanently locks the Casino room.
    """
    global random
    global has_entered_casino

    print("\n---Casino---")

    if has_entered_casino == True:
        print("You try to open the door leading to the casino, but it won't budge at all. Hmm, guess you can't do anything about that, so you stop trying.")
        print("You remain in the west hallway.")
        HallwayWest()
        return

    if "helpful casino reminder" in player_inventory:
        print("You enter the dimly lit room, and go straight to the yellow box on the stool in the corner. Do you want to play and win something?")

    if "helpful casino reminder" not in player_inventory:
        print("You enter a darkly lit room with red carpets, gold-trimmed furniture, and crystal chandeliers glimmer. The flashing lights on top of each machine seem to imprint in your brain as you blink quickly, trying to adjust to the light change.")
        print("You walk around the machines, huge advertisements and deals exploding on the screen. You walk up to one, a classic slot machine promising how getting triple 7s will make you rich.")
        print("You try to pull down on the huge lever on the side, but it doesn't budge. Instead, the screen shuts down completely, reflecting your expression.")
        print("Slowly, a small piece of paper prints out from where the tickets should come out.")
        print("\nIn small black writing it reads:")
        print("'This machine runs on hope... Your funds are insufficient. Maybe check on that.'\n")

        add_to_inventory("helpful casino reminder")
        print("'helpful casino reminder' added to your backpack.\n")

        print("Ok...that was definitely...unexpected. You move towards the other casino machines, but each one turns off and prints the same message when you attempt to play them. Fine.")
        print("You turn to leave, but something catches your eye.")
        print("A yellow cardboard box with a small narrow hole cut in the lid in positioned on a wooden chair in a corner of the room. A piece of paper stuck on it with sticky tape says 'LOTTERY' in messy handwriting.")
        print("You approach it, eyeing it skeptically. This...is a lottery? What's stopping you from taking the box off the stool and opening it?\n")
        print("Apparently, the strongest super glue in existence, because the box does not budge when you try to take it off the stool, and neither does the lid. You end up picking the whole stool up, rotating the whole set up to see what falls out of the hole. Nothing slips out.")
        print("Instead the piece of paper stuck on the box falls off and you see the rules of the supposed 'LOTTERY' on the back.")

        print("\nThis is the LOTTERY, the most rewarding casino machine in existence! It's simple:")
        print("There are pieces of paper labelled through 1-5 in this box. All you have to do it pick out a paper with a 5 on it and you win!")
        print("You can also keep going forever until you get the 5! Simple, isn't it?")

        print("\nAh, but for people like you, who are completely devoid of hope, you may find yourself a little unlucky...")
        print("But do not fear! We have added a small helpful rule that would help let getting the 5 easier!")
        print("If you do not get the 5 within 19 attempts, your 20th attempt is guaranteed to be the lucky number!")
        print("Well then, what are you waiting for?\n")

        print("Well, there's nothing to lose from this...right? But gambling isn't a good idea...")
    
    while True:
        action = input("\nWhat do you want to do? Options: show, play, n\n").lower()

        if action == "show":
            inventory()
        
        elif action == "play":
            draws = 0
            print(f'Amount of draws done: {draws}')

            while True:
                draws += 1
                draws_left = 20 - draws 

                if draws == 20:
                    number = 5
                else:
                    if random.random() < 0.0005:
                        number = 5
                    else:
                        number = random.randint(1, 4)

                print(f"Number: {number}")
                print(f'Draws left until guaranteed 5: {draws_left}')

                if number == 5:
                    print("\nCongratulations! You drew number 5.")
                    print("You wait patiently for your prize...")
                    print("A trapdoor in the ceiling above drops an item in front of you, closing back to seamlessly disappear into the hidden corner veiled by darkness.")
                    print("You grab the item, and you realise it is...")
                    print("An extremely ordinary pair a socks. Wow. Well, it's better than nothing you suppose.")
                    print("You put the socks in your backpack, and leave the room.")
                    print("When you close the door behind you, a soft click echoes across the walls, and you realise the door is locked.")
                    print("Strange, you swear the door wasn't supposed to lock when you closed it, but maybe this was intentional.")
                    print("You can no longer enter the casino again.")

                    has_entered_casino = True                    
                    
                    add_to_inventory("socks")

                    print("'socks' added to your backpack.") 

                    print("\nYour updated backpack:")
                    for item, info in player_inventory.items():
                        print(f"- {item} (x{info['count']})")
                    
                    HallwayWest()
                    return

                choice = input("Do you want to keep drawing? (y/n): ").lower()
                if choice == "n":
                    print("You decide to leave. It's just a game anyway.")
                    print("You exit the room.")
                    HallwayWest()
                    return

        elif action == "n":
            print("You exit the room.")
            HallwayWest()
            return
        
        else:
            print("Invalid option.")

def Library():
    """
    Manages the Library room logic.
    Sets up a puzzle involving a missing book and leads into a fight if the player solves it.
    Contains branching logic based on player progress and items.
    """

    global has_entered_library
    global UNFINISHED_FIGHT

    print("\n---Library---")

    if "key3" in player_inventory:
        print("You push against the door to library, but it doesn't budge. Well, you certainly don't want to go in and see the creepy robot again, so you leave the door as it is.")
        print("You are in the west hallway.")
        HallwayWest()

    if "key3" not in player_inventory:

        if UNFINISHED_FIGHT == True:
            print("You enter the library cautiously, peering around the door looking for the knight. They're there, watching you, standing in front of the front desk where the key is.")
            print("They make no movement as you get closer, until you're around 10 meters apart, when they swing their greatsword as a warning and wait.")
            print("Well, looks like there's only one option now: fight.")
            FIGHT()

        if has_entered_library == False:

            print("You enter a vast library, huge wooden shelves towering to a ceiling as high as a cathedral's. The dim ceiling lights every few steps shine down in dim pathways around the shelves, stretching left and right.")
            print("You walk up to the front desk, and unsurprisingly no one is there. You look around, unsure what to do.")
            print("Is this library important? Or is this just a huge trove of knowledge randomly stashed here?\n")

            print("All of a sudden, a tall woman swiftly emerges from one of the aisles, and stands behind the desk to look at you sternly.") 
            print("'Hello. What do you need?' she asks coldly, looking down at you over her pink rectangular glasses.")
            print("You awkwardly reply that you don't know what to do here, and you mumble something about leaving and letting her go back to what she was doing, but she cuts across you sharply.")
            print("'Hmph, follow me.'\n")

            print("You follow her as she walks past the bookshelves, leading you somewhere. The aisles go on endlessly, as you soon find yourself stopping in front of aisle 97, where the librarian walks down it.")
            print("'This is our non-fiction section. We pride ourselves with having a perfect book return rate, so EVERY. SINGLE. BOOK. should be here. There shouldn't be any missing books at all. But, in that IMPOSSIBLE event, people who fix the upheld order Please return all the books in the CORRECT PLACE when you have finished reading. Thank you.'")
            print("She leaves so quickly, catching you by surprise, and by the time you turn around to look where she went, the area around you is empty.\n")

            print("You walk down the aisle slowly, browsing all the books with interest. You're not sure what you're doing here, but you're intrigued enough to stay for a while longer.")
            print("You walk for a little longer, both ends of the aisle now out of sight, when you notice something.")
            print("There is a small gap between two books, labelled 'Common Cooking: Edition 1' and 'Common Cooking: Edition 3'.\n")
            print("Interesting. Didn't the librarian just say that all books were returned here? Why is there a missing book?")
            print("Logically thinking, the book that belongs in the gap must be labelled 'Common Cooking: Edition 2', so where would that be?")
            print("You think about this. Maybe you should find it and return it to its place?")


        if has_entered_library == True:
            print("You walk through the extravagant library, your footsteps echoing on the spruce planks. The vintage style lights glow softly, illuminating the covers of thousands of books each time you pass an aisle.")
            print("You go straight to aisle 97, where the gap in between the two cookbooks remain.")


        while True:
            action = input("\nWhat do you want to do? Options: show, use, e\n").lower()
            
            if action == "show":
                inventory()
            
            elif action == "use":
                if "cookbook" not in player_inventory:
                    print("There is nothing helpful in your backpack right now, best come back later to find something suitable.")
                else:
                    print("Use what?\n\nYour backpack:")
                    for item, info in player_inventory.items():
                        print(f"- {item} (x{info['count']})")
        
                    use_what = input(">").lower()
        
                    if use_what == "cookbook":
                        player_inventory["cookbook"]["count"] -= 1
                        if player_inventory["cookbook"]["count"] == 0:
                            del player_inventory["cookbook"]
        
                        print("You slide the cookbook into the empty slot, perfectly in line with all the other books. After a moment of silence, you hear the quietest creak of a door opening somewhere, and you look around, confused. The noise sounded like it came from the front desk, so you hurry over there. You spot the gleaming key from a distance, and begin walking quicker towards it, your hand outstretched when...\n")
                        print("A figure, in thick, metal armour carrying a LITERAL GREATSWORD emerges from the aisle right in front of you, blocking your path. It swings its weapon dangerously towards you in an arc, and you retreat immediately, watching in pure terror and fear. The medieval visored knight’s helm blocked its face, an empty void of darkness behind the mask.\n")
                        print("What. Is. Happening.\n")
                        print("How is there the most terrifying knight in existence holding a weapon RIGHT HERE. IN THIS LIBRARY.\n")
                        print("There is no way to escape this situation...so it looks like you'll have to fight.")
                        FIGHT()
                    else:
                        print("You can't use that right now.")
        
            elif action == "e":
                has_entered_library = True
                print("You exit the room.")
                HallwayWest()
        
            else:
                print("Invalid option.")



def create_weapon(name):
    name = name.lower()
    weapon_classes = {
        "water bottle": water_bottle,
        "broken bottle holder": broken_bottle_holder,
        "wine cork": wine_cork,
        "key1": Key1,
        "key2": Key2,
        "key3": Key3,
        "bone": bone,
        "laser pen": laser_pen,
        "cookbook": cookbook,
        "coffee": coffee,
        "lever": lever,
        "coin": coin,
        "note": note,
        "helpful casino reminder": helpful_casino_reminder,
        "socks": socks
    }
    weapon_class = weapon_classes.get(name)
    if weapon_class:
        return weapon_class()
    return None

def display_choices():
    print("---Choose Weapon---")
    for i, (item, info) in enumerate(player_inventory.items(), start=1):
        print(f"{i}. {item} x {info['count']}")
        info['weapon'].get_stats()
        print()


def FIGHT():
    """
    Executes a turn-based combat sequence against an enemy (Robot Knight).
    Handles weapon selection, random chance mechanics (e.g., crits, stuns), and win/loss conditions.
    Returns to Library logic upon completion.
    """

    global player_inventory
    global create_weapon
    global water_bottle, broken_bottle_holder, wine_cork, laser_pen, cookbook, coffee, lever, coin, note, helpful_casino_reminder, socks, Key1, Key2, Key3, bone

    global original_inventory
    original_inventory = copy.deepcopy(player_inventory)


    player_health = 100
    enemy_health = 100
    stunned = False

    print("\n\nYou enter the battle...\n")
    print("---Your enemy:---")
    print("name: Robot Knight")
    print("weapon: Greatsword")
    print("damage: 30")
    print("chance of stunning itself for one turn: 20%\n")
    print("===You begin===\n")

    choice_num = 1
    turn_num = 1

    def show_choices():
        print(f"===Choice {choice_num}===\n")
        print("---Choose Weapon---\n")
        for i, (item, info) in enumerate(player_inventory.items(), start=1):
            print(f"{i}. {item} x {info['count']}")
            info["weapon"].get_stats()
            print()

    def get_weapon_choice():
        while True:
            try:
                choice = int(input("(choose weapon by number)\n> "))
                keys = list(player_inventory.keys())
                if 1 <= choice <= len(keys):
                    return keys[choice - 1]
                else:
                    print("Invalid choice.")
            except:
                print("Invalid input.")

    while player_health > 0 and enemy_health > 0:

        if not player_inventory:
            print("You ran out of weapons.")
            print("Maybe try to find more items to use against the knight.")
            FAILED()
            

        show_choices()
        weapon = get_weapon_choice()
        print(f"\n==Your Turn {turn_num}==\n")
        print(f"Your health = {player_health}")
        print(f"Enemy health = {enemy_health}\n")

        if weapon == "water bottle":
            crit = random.random() < 0.8
            dmg = 30 if crit else 10
            enemy_health -= dmg
            print(f"You use the water bottle. {'It crit!' if crit else 'It does 10 damage.'} It deals {dmg} damage.\n")

        elif weapon == "broken bottle holder":
            crit = random.random() < 0.25
            dmg = 70 if crit else 20
            enemy_health -= dmg
            print(f"You use the broken bottle holder. {'It crit!' if crit else 'It does 20 damage.'} It deals {dmg} damage.\n")

        elif weapon == "wine cork":
            crit = random.random() < 0.99
            dmg = 2 if crit else 1
            enemy_health -= dmg
            print(f"You use the wine cork. {'It crit!' if crit else 'It does 1 damage.'} It deals {dmg} damage.\n")

        elif weapon in ["key1", "key2", "key3"]:
            stunned = True
            print(f"You use {weapon}. It deals no damage, but your opponent is stunned for 1 turn, so you get to go again.\n")

        elif weapon == "bone":
            crit = random.random() < 0.40
            dmg = 30 if crit else 20
            enemy_health -= dmg
            print(f"You use the bone. {'It crit!' if crit else 'It does 20 damage.'} It deals {dmg} damage.\n")

        elif weapon == "laser pen":
            rebound = random.random() < 0.45
            if rebound:
                player_health -= 50
                print("You use the laser pen. It rebounds onto you! You take 50 damage.\n")
            else:
                enemy_health -= 50
                print("You use the laser pen. It deals 50 damage.\n")

        elif weapon == "cookbook":
            stun = random.random() < 0.20
            enemy_health -= 15
            print("You use the cookbook. It deals 15 damage.")
            if stun:
                stunned = True
                print("Your opponent is stunned for 1 turn.\n")
            else:
                print()

        elif weapon == "coffee":
            rebound = random.random() < 0.95
            if rebound:
                player_health -= 80
                print("You use the coffee. It rebounds onto you! You take 80 damage.\n")
            else:
                enemy_health -= 80
                print("You use the coffee. It deals 80 damage.\n")

        elif weapon == "lever":
            crit = random.random() < 0.10
            dmg = 45 if crit else 10
            enemy_health -= dmg
            print(f"You use the lever. {'It crit!' if crit else 'It does 10 damage.'} It deals {dmg} damage.\n")

        elif weapon == "coin":
            crit = random.random() < 0.85
            dmg = 10 if crit else 5
            enemy_health -= dmg
            print(f"You use the coin. {'It crit!' if crit else 'It does 5 damage.'} It deals {dmg} damage.\n")

        elif weapon == "note":
            stun = random.random() < 0.05
            print("You use the note. It does no damage.")
            if stun:
                stunned = True
                print("Your opponent is stunned for 1 turn.\n")
            else:
                print()

        elif weapon == "helpful casino reminder":
            stun = random.random() < 0.35
            print("You use the helpful casino reminder. It does no damage.")
            if stun:
                stunned = True
                print("Your opponent is stunned for 1 turn.\n")
            else:
                print()

        elif weapon == "socks":
            crit = random.random() < 0.75
            dmg = 20 if crit else 15
            enemy_health -= dmg
            print(f"You use the socks. {'It crit!' if crit else 'It does 15 damage.'} It deals {dmg} damage.\n")

        else:
            dmg = player_inventory[weapon]["weapon"].damage
            enemy_health -= dmg
            print(f"You use {weapon}. It deals {dmg} damage.\n")

        print(f"Your health = {player_health}")
        print(f"Enemy health = {enemy_health}\n")

        if enemy_health <= 0:
            break

        if not stunned:
            print(f"==Enemy Turn {turn_num}==\n")
            print(f"Your health = {player_health}")
            print(f"Enemy health = {enemy_health}\n")

            miss = random.random() < 0.2
            if miss:
                print("The enemy tries to hit you, but misses. It is stunned for 1 turn.\n")
                stunned = True
            else:
                player_health -= 30
                print("The enemy hits you once with its greatsword. It deals 30 damage.\n")

            print(f"Your health = {player_health}")
            print(f"Enemy health = {enemy_health}\n")
        else:
            stunned = False
            print(f"==Enemy Turn {turn_num}==\n")
            print(f"Your health = {player_health}")
            print(f"Enemy health = {enemy_health}\n")
            print("The enemy tries to hit you, but misses. It is stunned for 1 turn.\n")
            print(f"Your health = {player_health}")
            print(f"Enemy health = {enemy_health}\n")

        player_inventory[weapon]["count"] -= 1
        if player_inventory[weapon]["count"] <= 0:
            del player_inventory[weapon]

        turn_num += 1
        choice_num += 1

    if player_health > 0:
        print("=====Congratulations, you won!===\n")
        FIGHT_WON()
    else:
        print("===You lost!===\n")
        FAILED()

def FIGHT_WON():
    """
    Handles the aftermath of winning the library fight.
    Reveals a plot twist, awards a key item, and restores player's inventory.
    """

    global key_count

    global player_inventory, original_inventory

    player_inventory = original_inventory

    print("You see the knight falling to the ground, their weapon clattering on the floor. The impact of the fall causes the helmet to bounce off, and you see... the librarian? ")
    print("Was the librarian the knight this whole time? Why would she attack you? Why would she lead you to the aisle that would reveal the key, only to stop you?")
    print("You have no idea what is happening, but with the librarian defeated, you take this chance to run and grab the key from the front desk.")
    print("You see the small '3' indented on it, and you put it into your backpack.")
    print("While the knight is unconscious, you grab all the items you've used and thrown, thankfully all intact, and put them back into your backpack.\n")

    print("'key3' added to your backpack.")
    add_to_inventory("key3")

    key_count = key_count + 1

    print("\nYour updated backpack:")
    
    for item, info in player_inventory.items():
        print(f"- {item} (x{info['count']})")

    print("\nYou're about to exit the room when you give the fallen librarian another glance as you open the door to leave, and you see something really strange.")
    print("The librarian is getting up, not facing you, but walking SUPER WEIRDLY. Her arms and legs are constantly twitching and jerking sharply, sometimes making her fall down again. That's...not right.")
    print("Then suddenly, with a blink of an eye, her head TURNS.")
    print("Just her head. Not her body. Her head turns a full 180° towards you, and then her face FALLS OFF.")
    print("You weren't fighting a knight or the librarian, you were fighting a robot THIS WHOLE TIME, it was only wearing the librarian's face.")
    print("That is really...creepy. Before the robot can move another step, you bolt out of the library, slamming the door behind you, a loud CLICK echoing as the door locks.")
    print("Well THAT was terrifying. Not going in there ever again.")
    print("You are now in the west hallway.")
    HallwayWest()
    return

def FAILED():
    """
    Handles the case when the player chooses to flee the fight.
    Restores original inventory and allows retrying the battle or exiting.
    """

    global UNFINISHED_FIGHT

    global player_inventory, original_inventory

    player_inventory = original_inventory

    print("You know you can't win right now, so using all the force left in your body, you run and manage to grab all the items you used and dashed behind one of the aisles. You check your items, thankfully all of them are still intact.")
    
    while True:
        action = input("\nWhat do you want to do? Options: show, fight, exit.\n").lower()
        if action == "show":
            inventory()
        elif action == "fight":
            FIGHT()
        elif action == "exit":
            UNFINISHED_FIGHT = True
            print("You quickly escglance when youpe the room, slamming the door shut.")
            print("You wait nervously in the hallway, listening for the knight's footsteps that indicate it's going to follow you.")
            print("However, it's pure silence except for your heavy breathing and thumping heartbeat.")
            print("Next time you enter the library, you'll have to immediately fight the knight again, if you want the key, because you bet it won't fall for any traps or tricks.")
            print("You are in the west hallway.")
            HallwayWest()
            return
        else:
            print("Invalid option.")


```
## __Review__
---

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.

I finally added the code that finishes the functional requireements, side, but there's still a lot to add overall. The weapon and class system works better than expected and it effecteively enhnaces the gaemplay experience by a lot.

### 2. Analyse the performance of your program against the key use-cases you identified.

I am glad that the wepon and class system worked, espesically as I hade spent a really long time assigned each item with stats, so at least the work wasn't for mothing. It handles funtions, classes and variables well so I am pleased.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability.

I specifically spent a long time on the combat system trying to get the output just right to help with readability, and it did help a little in the end. The code is easy to maintain and structured correctly and loically. The quality is good wnough for me.  

### 4. Explain the improvements that should be made in the next stage of development.

I am unsure what to do for ny next step, as I believe I have finished everything. Hoewever, I am open to new ideas and improvements for the future.

## __Peer Evaluation__

Person 1: Zoe Chen

I really enjoyed playing through your game! The atmosphere is really immersive, and the writing is creative and your inventory system works well and responds accurately to player choices.

The navigation was very smooth and simple to follow, and the object interactions were all planned out very well. 

A sugestion I would add is how the 'use ' command is coded, as it may get a bit confusing trying random things hoping you'll get them right if you don't know what's going on. A little suggestion of what you need to use may be helpful for other people, or basically, a 'help' button for people who may of accidentally misread information or forgot.'

Person 2: Hannah Kwon

This is a solid game structure for a text adventure. You clearly put effort into the narrative detail and player interaction. There’s a good balance between exploration and puzzle solving.

The game was well made with all the code constantly updating for the player's benefit, and all the possibilities were though out, which is pretty cool.

Only thing I would suggest is maybe a more distibuted story and difficulty between the 3 keys, as they vary a lot in skill and it may be a bit challenging. Starting off with only a few sentences on screen to tens of the them in a single room did make it hard to read sometimes and dfficult to rememeber infomations and leading to less attention from users.


