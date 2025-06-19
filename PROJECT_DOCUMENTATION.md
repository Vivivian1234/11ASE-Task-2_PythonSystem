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
* The application should be able to work on multiple platforms

## __Determining Specifications__
---
### *Functional Specifications*

* The user navigates through different rooms using directional commands ("n", "e", "s", "w").
* The user can interact with objects in specific contects for story purposes ("use", "eat", "talk", "play").
* The user can view their inventory by typing "show".
* The user can view items in their inventory through viewing the inventory.

* The system displays descriptions of the current location and available options.
* The system updates the player inventory every time the uer gains or loses an item.
* The system tracks what has been completed (keys collected, items found, etc)


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

### *Data Flow Diagram Level 0*

#### DFD Level 0

![Sprint1_Level0](/images.py/Sprint1_Level_0.png)

#### DFD Level 1
![Sprint1_Level0](/images.py/Sprint1_Level_1.png)


### **Structure Chart**

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
        - `player_inventory` accesse by making it global.
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
