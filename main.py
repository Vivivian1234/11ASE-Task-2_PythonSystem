import random

has_entered_casino = False

has_entered_kitchen = False

has_entered_library = False

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
                  print("You browse the endless delicious recipes in every one of the 198 pages, intrested. Maybe you could try these recipes later.")

                elif use == "coffee":
                  print("You hold the warm cup of coffee in your hands, the aroma heavenly. You would drink it... but rememeber that you're severely allergic to coffee. A pity.")
                
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

    pizza_margherita = ["thin", "tomato", "mozzarell", "basil"]
    pizza_pepperoni = ["thick", "tomato", "parmesan", "pepperoni"]
    pizza_cheese = ["thin", "tomato", "provolone", "none"]

    global has_entered_kitchen

    print("\n---Kitchen---")

    if "cookbook" in player_inventory:
        print("You enter the huge kitchen and see the empty case where the cookbook was. You like this room; making pizza is fun, and it gave you a lot of food to fill you back up.")
        print("There is nothing left to do in the room.")
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
                print("You know 3 basic pizza recipes: margherita, pepperoni and cheese.")
                print("There is only enough dough to make one pizza, so choose one to make and use the correct ingredients.")
                print("You will add the ingredients in the order: dough, sauce, cheese, toppings\n")
                
                print("Recipes:")
                print("Margherita: thin, tomato, mozzarella, basil")
                print("Pepperoni: thick, tomato, parmesan, pepperoni")
                print("Cheese: thin, tomato, provolone, none\n")

                print("-Dough options-")
                
                while True:
                    dough = input("thin/thick: ").lower()
                    if dough in ["thin", "thick"]:
                        pizza.append(dough)
                        break
                    else:
                        print("Invalid option.")

                print("-Sauce-")
                while True:
                    sauce = input("avocado, tomato, banana: ").lower()
                    if sauce in ["avocado", "tomato", "banana"]:
                        pizza.append(sauce)
                        break
                    else:
                        print("Invalid option.")

                print("-Cheese-")
                while True:
                    cheese = input("mozzarella, parmesan, provolone: ").lower()
                    if cheese in ["mozzarella", "parmesan", "provolone"]:
                        pizza.append(cheese)
                        break
                    else:
                        print("Invalid option.")

                print("-Toppings-")
                while True:
                    toppings = input("pepperoni, basil, none: ").lower()
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
    
    player_inventory["cookbook"] = player_inventory.get("cookbook", 0) + 1

    print("'cookbook' added to your backpack.")
    print("\nYour updated backpack:")
    inventory()
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

        player_inventory["helpful casino reminder"] = player_inventory.get("helpful casino reminder", 0) + 1
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
                    print("Congratulations! You drew number 5.")
                    print("You patiently wait for your prize...")
                    print("A trapdoor in the ceiling above drops an item in front of you, closing back to seamlessly disappear into the hidden corner veiled by darkness.")
                    print("You grab the item, and you realise it is...")
                    print("An extremely ordinary pair a socks. Wow. Well, it's better than nothing you suppose.")
                    print("You put the socks in your backpack, and leave the room.")
                    print("When you close the door behind you, a soft click echoes across the walls, and you realise the door is locked.")
                    print("Strange, you swear the door wasn't supposed to lock when you closed it, but maybe this was intentional.")
                    print("You no longer can enter the casino again.")

                    player_inventory["socks"] = player_inventory.get("socks", 0) + 1
                    print("'socks' added to your backpack.\n")
                    has_entered_casino = True


                    HallwayWest()
                    return

                choice = input("Do you want to keep drawing? (y/n): ").lower()
                if choice == "n":
                    print("You decide to leave, this is just a game anyway.")
                    print("You exit the room.")
                    HallwayWest()
                    return

        elif action == "n":
            HallwayWest()
            return
        
        else:
            print("Invalid option.")

def Library():

    global has_entered_library

    print("\n---Library---")

    if has_entered_library == False:
        print("You enter a vast library, huge wooden shelves towering to a ceiling has high as a cathedral's. The dim ceiling lights every few steps shine down in dim pathways around the shelves, stretching left and right.")
        print("You walk up to the front desk, and unsuprisingly no one is there. You look around, unsure what to do.")
        print("Is this librbary important? Or is this just a huge trove of knowledge randomly stashed here?\n")

        print("All of a sudden, a tall woman swiftly emerges from one of the aisles, and stands behind the desks to look at you sternly.") 
        print("'Hello. What do you need?' she asks coldly, looking down at you over her pink rectangular glasses.")
        print("You awkwardly reply that you don't know what to do here, and you mumbling something about leaving and letting her go back to what she was doin, but she cuts across you sharply.")
        print("'Hmph, follow me.'\n")

        print("You follow her as she walks past the bookshelves, leading you somewhere. The aisles go on endlessly, as you soon find yourslef stopping in front of aisle 97, where the librarian walks down it.")
        print("'This is our non-fiction section. We pride ourselves with having a perfect book return rate, so EVERY. SINGLE. BOOK. should be here. There shouldn't be any missing books at all. But, in that IMPOSSIBLE event, people who fix the upheld order Please return all the books in the CORRECT PLACE when you have finsihed reading. Thank you.'")
        print("She leaves so quickly, catching you by suprise, and by the time you turn around to look where she went, the area around you is empty.\n")

        print("You walk down the aisle slowly, browing all the books with intrest. You're not sure what you're doing here, but you're intruiged enough to stay for a while longer.")
        print("You walk for a little longer, both ends of the aisle now out of sight, when you notice something.")
        print("There is an small gap between two books, labelled 'Common Cooking: Edition 1' and 'Common Cooking: Edition 3' respectively.\n")
        print("Intresting. Didn't the librarian just say that there all books were returned here? Why is there a missing book?")
        print("Logically thinking, the book that belongs in the gap must be labelled 'Common Cooking: Edition 2', so where would that be?")
        print("You think about this. Maybe you should find it and return it to it's place?")


    if has_entered_library == True:
        print("You walk through the extravagant library, your footsteps echoing on the spruce planks. The vintage style lights glow softly, illuminating the covers of thousands of books each time you pass an aisle.")
        print("")

    actions = input("\nWhat do you want to do?")

main()
