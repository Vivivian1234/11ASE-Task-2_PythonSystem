
player_inventory = {
    "water bottle": 2,
    "broken bottle holder": 1,
    "wine cork": 1
}

def inventory():
    global player_inventory  # let us access and modify the shared one

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
                
                elif use == "key 1":
                  print("You take out the shiny golden key out of your backpack. The glittering '2' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                
                elif use == "key 1":
                  print("You take out the shiny golden key out of your backpack. The glittering '3' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")

                elif use == "bone":
                  print("The small bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")
                  
                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it awat for now, in case you accientally burn off one of your fingers.")

                elif use == "cookbook":
                  print("You browse the endless delicious recipes in the cokbook, your stomach rumbling in longing. You can't look for even a few seconds before you realise how hungry you are. You put the book away, trying your best to not be distracted.")

                elif use == "coffee":
                  print("You hold the warm cup of coffee in your hands, the aroma heavenly. You would drink it... but you're severely allergic to coffee. A pity.")
                
                elif use == "lever":
                  print("You pull out the small and suprisingly light metal lever from your pocket. It reminds you a but of a Minecraft lever, and you wonder where that thought came fron. Anyway, you ponder where this could be used...")

            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nInvalid request. Please try again.")


def main():
  print("What is your name?\n")
  print("Good, at least you remember your name.\n")
  
  Cellar()

def Cellar():
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

def DogRoom():
  while True:
    print("\n---Dog Room---")
    if "laser pen" in inventory:
      print("You see the now empty room, with the scent of fur and meat in the air. A metal pole reamins in the middle of the empty room. Thank goodness the dog was free from the prison.")
      print("There is no more need to be here. You return to the East Hallway.")
      HallwayEast()

    elif "laser pen" not in inventory:
      print("You enter a room with a huge black dog with glowing red eyes. You don’t notice the dog at first, its fur colour blending in with the shadows. As you approached the spot where the dog stood, it barked aggressively at you. You jumped back, finally noticing the creature. Then you realise it was tied to a pole with a metal chain. The dog howled in pain as you approached and growled as you reached out for it. Options: s, use")
      if 'bone' in inventory:
        print("But his mouth was watering when he spotted the bone in your pouch.\n")
        action = input("\nWhat do you want to do? Options: show, s\n").lower()
        if action == "show":
          inventory()
        elif action == "s":
          HallwayEast()


def Bathroom():
  while True:
    print("\n---Bathroom---")
    if 'lever' in inventory:
      print("Nothing seems out of the ordinary, except for the stench and the mould everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do?")
      action = input("Options: show, w \n")







main()