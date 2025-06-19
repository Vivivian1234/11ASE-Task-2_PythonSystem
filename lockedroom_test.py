
key_count = 3

def Cellar():
    print("\n---The Cellar---")
    print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")
    
    while True:        
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
    
    global key_count

    keys_left = 3 - key_count

    print ("\n---Locked Room---\n")

    print("You try to open the locked door, but it doesn't budge at all. The three keyholes labelled '1', '2', and '3' above the handle show that there you must have all 3 keys to open the door.\n")

    if key_count == 3:
        print("You have all 3 keys in your backpack.")

    else:
        if keys_left == 1:
            print(f'You have {key_count} key. You need {keys_left} key left to find')
        else:
            print(f'You have {key_count} keys. You need {keys_left} keys left to find')

    while True:
        action = input("\nWhat do you want to do? Options: show, open, n\n").lower()

        if action == "show":
            inventory()
        elif action == "open":
            if key_count == 3:
                print("You open the door!")
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
    print("congrats")

Cellar()