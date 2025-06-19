import copy
import random
import sys

from weapon import water_bottle, broken_bottle_holder, wine_cork, laser_pen, cookbook, coffee, lever, coin, note, helpful_casino_reminder, socks, Key1, Key2, Key3, bone
from weapon import create_weapon

found_bone = False

has_entered_casino = False

has_entered_kitchen = False

has_entered_library = False

UNFINSIHED_FIGHT = False

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
                  print("You take out the shiny golden key out of your backpack. The glittering '1' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                
                elif use == "key2":
                  print("You take out the shiny golden key out of your backpack. The glittering '2' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and you can hopefully get out of here.")
                
                elif use == "key3":
                  print("You take out the shiny golden key out of your backpack. The glittering '3' on the handle reflects the dull glow from the ceiling lights above you. Collect all three, and hopefully you can use them to get into the locked room by the cellar to get out of here.")

                elif use == "bone":
                  print("The bone is cold to the touch, and quite gross to hold in your hands. You wonder where it came from. Best put it away for now.")
                  
                elif use == "laser pen":
                  print("You take out the small black office pen, and click the red button the side. A red laser shoots out, burning a small hole into the wall, still smoking. The yellowish wallpaper is gone, but the thick metal walls behind it remains untouched. Though you certainly can't burn through the walls, you could use this to your advantage... Well, best to put it away for now, in case you accientally burn off one of your fingers.")

                elif use == "cookbook":
                  print("You browse the endless delicious recipes in every one of the 198 pages, intrested. Maybe you could try these recipes later.")

                elif use == "coffee":
                  print("You hold the warm cup of coffee in your hands, the aroma heavenly. You would drink it... but remember that you're severely allergic to coffee. A pity.")
                
                elif use == "lever":
                  print("You pull out the small and suprisingly light metal lever from your pocket. It reminds you a bit of a Minecraft lever, and you wonder where that thought came fron. Anyway, you ponder where this could be used...")

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

                elif use == "helpful casino reminder":
                    print("A helpful little reminder about yourself:")
                    print("'This machine runs on hope...You're funds are insufficient. Maybe check on that.'")
                
                elif use == "socks":
                    print("You hold the white socks in your hand. They're a little small for you. Such an incredible prize indeed.")

            else:
                print(f"\nYou don't have any {use}s left!")
        else:
            print("\nInvalid request. Please try again.")

def main():
  print("\nYou wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so lonely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")
  
  name = input("What is your name?\n").lower()
  name = name.capitalize()

  print("Good, at least you remember your name.\n")

  Cellar()

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
            print(f'You have {key_count} keys. You need {keys_left} key left to find')
        else:
            print(f'You have {key_count} keys. You need {keys_left} keys left to find')

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

    global sys

    print("You enter a really small room with walls coated in black paint, giving the illusion of entering a void of emptiness.")
    print("In front of you on a table covered by a black table cloth is a large metal safe, with no opening you can see.")
    print("You're sure the thing in the same must be able to help you escape, but you don't know how. How could you break a safe like this? It seems indestructible.")
    print("Hey...what about you try you laser pen? There's no harm in trying.")
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

                    print("\nYou aim the laser pointer at the the safe, and turn it on. The bright beam of red blinds you for a second, but you hold it steadily and try to sear the side off it.")
                    print("After a little while, you see the heat damage the safe slowly, and after a long time the side of the safe falls off (finally, your arms are getting tired!) and you peer inside the safe cautiously.")
                    print("Inside is a huge round cut diamond on a triangular stand, bigger than your head.")
                    print("You carefully take it out by the stand, and push the safe of the table to marvel at the jewel.")
                    print("It seems to shine millions of nonexistent colours across the walls from the dim light of the cellar behind you, and it gives you instant hope and calm.")

                    if "helpful casino reminder" in player_inventory:
                        print("(Ha, that helpful casino reminder was WRONG, I have plenty of hope!!!)")

                    print("You have no idea whay this diamond is doing here, and how it'll help you escape, but you should try something.")
                    print("You reach your hand tentatively to touch it when you suddently hear a bark behind you. You turn around to see the dog from before bounding up to you, tail wagging happily. It jumps up into your chest and you catch it with your other arm, accidentally brushing it with the fingers of your outstreatch hand.")
                    
                    print("You hear a soft buzzing sound, and your mind feels like it's being pulled across dimensions; you can't see anything but pitch darkness, when you land on something extremely soft and comfortable.")
                    print("You ope your eyes the tiniest bit as tiredness overwhelmes you, and the puppy still cradled in your arms, warm and soft. You think you see the faint outlines of you bedroom before you fall asleep.\n")

                    print("You wake up and turn on the morning news with your new best friend Teddy at your side. The huge headlines says:")
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

    global key_count
    
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
            print("There is nothing helpful in your backpack right now, best come back later to find something suitable.")
        
        else:
            while True:
                print("Use what?\n\nYour Backpack:")
                for item, info in player_inventory.items():
                    print(f"- {item} (x{info['count']})")
                use_what = input(">")

                if use_what == "bone":
                    print("The black doggo gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off who knows where and reveals a key underneath the spot he was standing on. You pick up the key and a small black pen. It looks delicate, so you are careful when you pick it up, afraid of damaging it. The fancy writing on the pen read 'Laser Pen'. Laser Pen? Really? You put both items in your pocket.")
                                    
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

def Bathroom():
    global found_bone
    global key_count

    print("\n---Bathroom---")

    if "lever" in player_inventory:
        print("Nothing seems out of the ordinary, except for the stench and the mould everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do?")

        while True:
            action = input("\nWhat do you want to do? Options: use, s\n").lower()

            if action == "use":
                print("Use what?\n\nYour Backpack:")
                for item, info in player_inventory.items():
                    print(f"- {item} (x{info['count']})")
                use_what = input(">")

                if use_what == "lever":
                    print("The mirror swings open and reveals a small hole containing a key. You grab it and swing the mirror back shut. The cold key in your hands has a small '2' on it. You place it in your backpack.\n")

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
                    print(f"You try to use the {use_what}, but it does nothing. You stare at the cracked reflection of you in the mirror, and you swear it is looking at you weirdly.")

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
        
            while True:
                action = input("\nWhat do you want to do? Options: use, s\n").lower()

                if action == "use":
                    while True:

                        print("Use what?\n\nYour Backpack:")
                        for item, info in player_inventory.items():
                            print(f"- {item} (x{info['count']})")
                        use_what = input(">")
                        
                        if use_what == "coin":
                            print("You hand over the small coin, and Friendly Baraista gives you piping hot coffee in a simple paper cup. You gladly accept the coffee and hold on to it. You can't drink it, because you just so happened to be allergic to coffee. Oh well, at least it's warm. You put it away. \n")
                            
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

        print("You enter a spotless and well furnished cafe, the clean wooden floors and light blue wallpaper decorated with a flower mural making it seem out of place, so comfortable and homely compared to the rest of this dark and gloomy underground structure you are in.")
        print("A barista with calm, blank eyes greets you, staring into your eyes with something less than human.")
        print("'Greetings, I am Friendly Barista. Would you like buy some coffee? It's one Cuppa Coin.'")
        print("You see a huge coin drawing behind him on the wall, silver with a coffee cup engraved on it. That must be the currency to buy a coffee.")
        print("You ask about the kidnapping and keys but he acts clueless, but still smiling as laid back as ever.")

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
            print("\nYou think about this riddle, and a few answers are possible...but only one answer appears clear as day. You know it...and it's in the bathrooom!!!\n")

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
        
        print("You enter a dirty room full of mould, sweaty and dirty clothes, empty, unwashed coffee mugs and yellowed open books. It reeks of coffee and expired milk. You see a tired guy in a bad mood sitting on his bed rubbing his face.")
        print("'Ugh... I'm so tired...' he groans.")
        print("You ask about the keys.")
        print("'Oh... gimme a coffee and I'll give you a clue to the key...zzz' he lies flat on his bed, yawning widely.")
        print("'Oh right...take these. The name's Andy by the way.' He hands you a small silver coin, with a small coffee cup engraved on it.")
        print("Is this...money? Is this how you buy the coffee? Alright...you put it away.")

        add_to_inventory("coin")

        print("\nYour updated backpack:")
        
        for item, info in player_inventory.items():
            print(f"- {item} (x{info['count']})")
            
        print("\nBest to go get Andy some coffee.. You exit the room.")
        HallwayNorth()
        return

def PartyRoom():
    global party_room_cake
    global slices
    global slices_left
    global player_inventory

    global has_entered_casino
    global has_entered_kitchen
    global has_entered_library
    global UNFINSIHED_FIGHT

    global key_count
    
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

                has_entered_casino = False

                has_entered_kitchen = False

                has_entered_library = False

                UNFINSIHED_FIGHT = False

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
                print("'Please...' he begged quietly, 'Please stop eating. You will regret every slice you take.'")
                print("You are unsure what to do. Should you keep eating or leave the room?")

        else:
            print("Invalid option.")

def HallwayWest():

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
            print("You look around the pristine kitchen, and notice on a table in a corner is a small see-through case is a cookbook. The case is extremely sturdy and doesn't break when you apply force to it, so it seems the only way to acquire the cookbook is the enter a 4 digit code on the side of the case.")
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
        print("'This machine runs on hope...You're funds are insufficient. Maybe check on that.'\n")

        add_to_inventory("helpful casino reminder")
        print("'helpful casino reminder' added to your backpack.\n")

        print("Ok...that was definetely...unexpected. You move towards the other casino machines, but each one turns off and prints the same message when you attempt to play them. Fine.")
        print("You turn to leave, but something catches your eye.")
        print("A yellow cardboard box with a small narrow hole cut in the lid in positioned on a wooden chair in a corner of the room. A piece of paper stuck on it with sticky tape says 'LOTTERY' in messy handwriting.")
        print("You approach it, eyeing it skeptically. This...is a lottery? What's stopping you from taking the box off the stool and opening it?\n")
        print("Apparently, the strongest super glue in existence, because the box does not budge when you try to take it off the stool, and neither does the lid. You end up picking the whole stool up, rotating the whole set up to see what falls out of the hole. Nothing slips out.")
        print("Instead the piece of paper stuck on the box falls off and you see the rules of the supposed 'LOTTERY' on the back.")

        print("\nThis is the LOTTERY, the most rewarding casino machine in existence! It's simple:")
        print("There are pieces of paper labelled through 1-5 in this box. All you have to do it pick out a paper with a 5 on it and you win!")
        print("You can also keep going forever until you get the 5! Simple, isn't it?")

        print("\nAh, but for people like you, where you are completely devoid of hope, you may find yourself a little unlucky...")
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
                print(f'Draws left until guarenteed 5: {draws_left}')

                if number == 5:
                    print("\nCongratulations! You drew number 5.")
                    print("You patiently wait for your prize...")
                    print("A trapdoor in the ceiling above drops an item in front of you, closing back to seamlessly disappear into the hidden corner veiled by darkness.")
                    print("You grab the item, and you realise it is...")
                    print("An extremely ordinary pair a socks. Wow. Well, it's better than nothing you suppose.")
                    print("You put the socks in your backpack, and leave the room.")
                    print("When you close the door behind you, a soft click echoes across the walls, and you realise the door is locked.")
                    print("Strange, you swear the door wasn't supposed to lock when you closed it, but maybe this was intentional.")
                    print("You no longer can enter the casino again.")

                    has_entered_casino = True                    
                    
                    add_to_inventory("socks")
                    
                    print("\nYour updated backpack:")
                    for item, info in player_inventory.items():
                        print(f"- {item} (x{info['count']})")
                        
                    print("'socks' added to your backpack.")
                    HallwayWest()
                    return

                choice = input("Do you want to keep drawing? (y/n): ").lower()
                if choice == "n":
                    print("You decide to leave, this is just a game anyway.")
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

    global has_entered_library
    global UNFINSIHED_FIGHT

    print("\n---Library---")

    if "key3" in player_inventory:
        print("You push against the door to library, but it doesn't budge. Well, you certainly don't want to go in and see the creepy robot again, so you leave the door as it is.")
        print("You are in the west hallway.")
        HallwayWest()

    if "key3" not in player_inventory:

        if UNFINSIHED_FIGHT == True:
            print("You enter the library cautiously, peering around the door looking for the knight. They're there, watching you, standing in front of the front desk where the key is.")
            print("They makes no movement as you get closer, until you're around 10 meters apart, when they swing their greatsword as a warning and wait.")
            print("Well, looks like there's only one option now: fight.")
            FIGHT()

        if has_entered_library == False:

            print("You enter a vast library, huge wooden shelves towering to a ceiling as high as a cathedral's. The dim ceiling lights every few steps shine down in dim pathways around the shelves, stretching left and right.")
            print("You walk up to the front desk, and unsurprisingly no one is there. You look around, unsure what to do.")
            print("Is this library important? Or is this just a huge trove of knowledge randomly stashed here?\n")

            print("All of a sudden, a tall woman swiftly emerges from one of the aisles, and stands behind the desks to look at you sternly.") 
            print("'Hello. What do you need?' she asks coldly, looking down at you over her pink rectangular glasses.")
            print("You awkwardly reply that you don't know what to do here, and you mumbling something about leaving and letting her go back to what she was doing, but she cuts across you sharply.")
            print("'Hmph, follow me.'\n")

            print("You follow her as she walks past the bookshelves, leading you somewhere. The aisles go on endlessly, as you soon find yourself stopping in front of aisle 97, where the librarian walks down it.")
            print("'This is our non-fiction section. We pride ourselves with having a perfect book return rate, so EVERY. SINGLE. BOOK. should be here. There shouldn't be any missing books at all. But, in that IMPOSSIBLE event, people who fix the upheld order Please return all the books in the CORRECT PLACE when you have finished reading. Thank you.'")
            print("She leaves so quickly, catching you by surprise, and by the time you turn around to look where she went, the area around you is empty.\n")

            print("You walk down the aisle slowly, browsing all the books with interest. You're not sure what you're doing here, but you're intrigued enough to stay for a while longer.")
            print("You walk for a little longer, both ends of the aisle now out of sight, when you notice something.")
            print("There is an small gap between two books, labelled 'Common Cooking: Edition 1' and 'Common Cooking: Edition 3'.\n")
            print("Interesting. Didn't the librarian just say that all books were returned here? Why is there a missing book?")
            print("Logically thinking, the book that belongs in the gap must be labelled 'Common Cooking: Edition 2', so where would that be?")
            print("You think about this. Maybe you should find it and return it to it's place?")


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
                        print("A figure, in thick, metal armour carrying a LITERAL GREATSWORD emerges from the aisle right in front of you, blocking your path. It swings its weapon dangerously towards you in an arc, and you retreat immediately, watching in pure terror and fear. The medieval visored knight’s helm blocked it's face, an empty void of darkness behind the mask.\n")
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

    print("\nYou're about to exit the room when you give the fallen librarian another glance when you open the door to leave, and you see something really strange.")
    print("The librarian is getting up, not facing you, but walking SUPER WEIRDLY. Her arms and legs are constantly twitching and jerking sharply, sometimes making her fall down again. That's...not right.")
    print("Then suddenly, with a blink of an eye, her head TURNS.")
    print("Just her head. Not her body. Her head turns a full 180° towards you, and then her face FALLS OFF.")
    print("You weren't fighting a knight or the librarian, you were fighting a robot THIS WHOLE TIME, it was only wearing the librarian's face.")
    print("That is really...creepy. Before the robot can move another step, you bolt out of the library, slamming the door behind you, a loud CLICK echoing as the door locks.")
    print("Well THAT was terrifying. Not going in there everrrr again.")
    print("You are now in the west hallway.")
    HallwayWest()
    return

def FAILED():

    global UNFINSIHED_FIGHT

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
            UNFINSIHED_FIGHT = True
            print("You quickly escape the room, slamming the door shut.")
            print("You wait nervously in the hallway, listening for the knight's footsteps that indicate it's going to follow you.")
            print("However, it's pure silence except for your heavy breathing and thumping heartbeat.")
            print("Next time you enter the library, you'll have to immediately fight the knight again, if you want the key, because you bet it won't fall for any traps or tricks.")
            print("You are in the west hallway.")
            HallwayWest()
            return
        else:
            print("Invalid option.")

main()