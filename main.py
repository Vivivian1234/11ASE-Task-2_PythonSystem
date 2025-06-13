
player_name = []

class inventory():
  inventory = {}
  print ("Use what? Options:")
  
  for i in inventory:
    print(i)



def main2():
    
    print("\n---Inventory---\n")
    inventory = ["water bottle, 1", "broken bottle holder, 1", "random wine cork, 1"]
    
    for item in inventory:
        item_desc, number = item.split(", ")
        print (f"{item_desc} x {number}")

        use = input("What dowuld you like to use?")
        use = use.lower()
        if use in inventory:
          if use == "water bottle":
            print("You grab the tiny bottle of water from your pocket, and drink it in one gulp. Your thirst is quenched sightly, but your throat still feels dry and scratchy.")
            
        
def inventory():
    inventory = {
        "water bottle": 2,
        "broken bottle holder": 1,
        "wine cork": 1
    }

    while True:
        print("\n---Inventory---\n")
        if inventory:
            for item, number in inventory.items():
                print(f"{item} x {number}")
        else:
            print("Your inventory is empty!")
            return

        use = input("\nWhat would you like to use? (type 'exit' to quit)\n ").lower()

        if use == "exit":
            return

        if use in inventory:
            if inventory[use] > 0:
                inventory[use] -= 1
                print(f"\nYou used one {use}.")
                if use == "water bottle":
                  print("You grab the tiny bottle of water from your pocket, and drink it in one gulp. Your thirst is quenched sightly, but your throat still feels dry and scratchy.")
                  return
                  if inventory[use] == 0:
                      print(f"You have no more {use}s left. Removing it from inventory.")
                      del inventory[use]  # Remove item from dictionary
            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nThat item is not in your inventory.")

    print("\nThanks for using your inventory!")

inventory()


def main():
    print("The Cellar\n")
    print("You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so homely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")

    name = input("What is your name?\n")
    name = name.lower()
    name = name.capitalize()
    player_name.append(name)

    print("Good, at least you remember your name.\n")

def cellar_direction():
    
    print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")

    action = input("What do you want to do here?\n")

    if action == "show":
      print("hi")
    elif action == "e":
      HallwayEast()
    elif action == "w":
      HallwayWest()
    elif action == "n":
      HallwayNorth()
    elif action == "s":
      lockedRoom()
    while action != "w" "e" "n" "s" "show":
      print("You don't think you can go that way right now.")
      action = input("What do you want to do here?\n")