
party_room_cake = False
slices = 0
slices_left = 8 - slices

player_inventory = {
    "water bottle": 2,
    "broken bottle holder": 1,
    "wine cork": 1
}

def inventory():
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
                
                elif use == "key 3":
                  print("You take out the shiny golden key out of your backpack. The glittering '3' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")

                elif use == "bone":
                  print("The bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")
                  
                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it awat for now, in case you accientally burn off one of your fingers.")

                elif use == "cookbook":
                  print("You browse the endless delicious recipes in the cokbook, your stomach rumbling in longing. You can't look for even a few seconds before you realise how hungry you are. You put the book away, trying your best to not be distracted.")

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

def main():
  print("You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so lonely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")
  
  name = input("What is your name?\n").lower()
  name = name.capitalize()

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

def DogRoom():

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

        action = input("What do you want to do? Options: use, s\n").lower()

        if action == "use":

            if "bone" not in player_inventory:
                print("There is nothing helpful in your inventory right now, best come back later to find something suitable.")
            
            else:
                while True:
                    print("Use what?\n\nYour Inventory:")
                    for item, qty in player_inventory.items():
                        print(f"- {item} (x{qty})")
                    use_what = input(">")

                    if use_what == "bone":
                        print("The black doggo gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off who knows where and reveals a key underneath the spot he was standing on. You pick up the key and a small black pen. It looks delicate, so you are careful when you pick it up, afraid of damaging it. The fancy writing on the pen read 'Laser Pen'. Laser Pen? Really? You put both items in your pocket.")
                                        
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

def Bathroom():

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
                while True:
                    print("Use what?\n\nYour Inventory:")
                    for item, qty in player_inventory.items():
                        print(f"- {item} (x{qty})")
                    use_what = input(">")

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

    while True:
        print("\n---HallwayNorth---")
        print("There are three rooms down this hallway. A party room to the east, a bedroom with a messy sign with 'Andy' scribbled on it to the west, and a cafe continuing north. You can also return to the cellar back to the south.")
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
                while True:

                    print("Use what?\n\nYour Inventory:")
                    for item, qty in player_inventory.items():
                        print(f"- {item} (x{qty})")
                    use_what = input(">")
                    
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

def PartyRoom():
    global party_room_cake
    global slices
    global slices_left
    global player_inventory
    
    print("---PartyRoom---")

    if party_room_cake == True:
        print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, who is wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
        print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
        print("On the table, there is a 5-layer birthday cake.")
        print("It looks and smells a bit stale, but would still undoubtably be delicious.")
        print(f'There are {slices_left - 1} slices left of the cake.')
        print("You reach for the cake, but an unnerving chill runs down your spine, and your appetite has disappeared completely. Now, for some strange reason, you feel repulsed by the cake, and want to leave as soon as possible.")
        print("You leave the room.")
        HallwayNorth()
        return

    print("You enter a brightly coloured room with helium balloons and a tall clown standing by opposite wall, who is wearing a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile.")
    print("You walk across the vividly decorated room, and can feel the clown's eyes following you, making eye contact when you glance at it nervously. He does not provoke you, watching quietly as you approach the table in the centre of the room.")
    print("On the table, there is a 5-layer birthday cake.")
    if slices == 0:
        print("There are 8 large slices on the table, cut perfectly for you to grab.")
    else:
        print(f'There are {slices_left} large slices on the plate, ready for you to grab.')
    print("Your mouth waters as you approach it, but as you get closer, you realise the sugary icing spells out 'HAPPY BIRTHDAY; DO NOT EAT ME'.")
    print("The cake looks so appetizing, and you're so hungry.")
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
                print("\nEach slice of the cake is delicious and filling, and every bite of it makes you feel more addictive.")
                print("Suddenly, you feel sick, and sway dangerously on your feet, and then the impact of falling to the ground on your knees.")
                print("Your head is spinning, and you try to stand back up again, your legs shaking.")
                print("Then you slowly stand up, still feeling extremely nauseous, and a piece of cloth is wrapped around your head, suffocating you, the subtle sweet smell lingering as you fall into darkness.\n")

                player_inventory = {
                    "water bottle": 2,
                    "broken bottle holder": 1,
                    "wine cork": 1
                }
                party_room_cake = True

                main()
                return
            else:
                slices += 1
                slices_left -= 1

                print("You take a slice of the huge cake and have a huge bite.")
                print("Wow.")
                print("It. Is. Delicious.")
                print("After finishing the slice, you turn around to look at the clown still staring at you, and you see a face of true horror etched across his face.")
                print("'Please...' he begged quietly, 'Please stop eating. You will regret every slice you take.'")
                print("You are unsure what to do. Should you keep eating or leave the room?")

        else:
            print("Invalid option.")

def HallwayWest():

    while True:
        print("\n---HallwayWest---")
        print("There are three rooms down this hallway. A kitchen to the north, a gym to the south, and a library continuing west. You can also return to the cellar back to the east.")
        action = input("\nWhat do you want to do? Options: show, n, e, s, w\n").lower()
        if action == "show":
            inventory()
        elif action == "n":
            Kitchen()
        elif action == "e":
            Cellar()
        elif action == "s":
            Gym()
        elif action == "w":
            Library()
        else:
            print("You don't think you can go that way right now.")


def Kitchen():
    while True:
        print("\n---HallwayWest---")

def Gym():
    while True:
        print("\n---HallwayWest---")

def Library():
    while True:
        print("\n---HallwayWest---")
main()
