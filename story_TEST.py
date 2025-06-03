#-----------import libraries

inventory = ["broken bottle holder"]

from inventory import addItem, useItem, showItem

#-------------variables

inv = [""]

#------------ places

def cellar():

  print("The Cellar\n")

  print(

      "You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so homely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?"

  )

  input("What is your name?\n")

  print("Good, at least you remember your name.\n")

  print(

      "There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible."

  )

  direction = input("What do you want to do here?\n")

  if direction == "show":

    showItem(inv)

  elif direction == "e":

    HallwayEast()

  elif direction == "w":

    HallwayWest()

  elif direction == "n":

    HallwayNorth()

  elif direction == "s":

    lockedRoom()

  while direction != "w" "e" "n" "s" "show":

    print("You don't think you can go that way right now.")

    direction = input("What do you want to do here?\n")

def HallwayNorth():

  print("NorthHallway\n")

  action = input(

      """There are are two rooms through here. You can go the bathroom in the east or the dog room in the north, or you can return to the cellar. 

  - e 

  - n

  - s\n""")

  if action == "e":

    bathroom()

  elif action == "n":

    dogRoom()

  elif action == "s":

    cellar()

def bathroom():

  print("Bathroom")

  if 'lever' in inv:

    print(

        "Nothing seems out of the ordinary, except for the stench and the mould everywhere. The mirror looks very suspicious though... maybe it's hiding something. You walk towards it and notice a small hole on the side of the mirror. Maybe a lever belongs there? What do you do? Options: use, w \n"

    )

    if use in inv:

      print("Use what?")

      if use == 'lever':

        print(

            "The mirror swings open and reveals a small hole containing a key. You grab it and swing the mirror back shut. \n"

        )

        inv.remove('lever')

        inv.append('KeyTwo')

        HallwayNorth()

  elif 'lever' not in inv:

    move = input(

        "You enter a broken down bathroom, completely unusable. There’s mold on the toilet and sink, the shower head is smashed. The once-white tiles are now brown, covered in dirt and grime. And… what is that white thing sticking out of the sink? You can go: 'w' back to North Hallway, 'take' the bone or 'show' your inventory\n"

    )

    if move == "show":

      showItem(inv)

    if move == 'w':

      HallwayNorth()

    elif move == "take":

      print(

          "You approach the 'white thing', peering into the sink, discovering that it was a large bone. The bottom part of it was stuck inside the drain. Huh. Wonder how that got here? You ran your fingers across the smooth white object and lightly tugged at it. When the bone didn't budge, you then tried pulling the bone, and after some effort, the bone was finally free from the sink. It probably would become useful later, you decided, and shoved it into your pocket."

      )

      inv.append("bone")

      showItem(inv)

      HallwayNorth()

def dogRoom():

  print("dogRoom\n")

  if "laserPen" in inv:

    print(

        "You  see the now empty room, with the scent of fur and meat in the air. A metal pole is standing in the moddle of the room. Thank goodness the dog was free from the prison."

    )

    HallwayNorth()

  elif "laserPen" not in inv:

    print(

        "You enter a room with a huge black dog with glowing red eyes. You don’t notice the dog at first, its fur colour blending in with the shadows. As you approached the spot where the dog stood, it barked aggressively at you. You jumped back, finally noticing the creature. Then you realise it was tied to a pole with a metal chain. The dog howled in pain as you approached and growled as you reached out for it. Options: s, use"

    )

  if 'bone' in inv:

    print(

        "But his mouth was watering when he spotted the bone in your pouch.\n")

    action = input("What do you want to do?")

    if action == "use":

      use = input("use what?")

      if use in inv:

        print("you decide to use the ", use)

        if use == "bone":

          print(

              "The black doggo gobbles up the bone and wags its tail at you, no longer aggressive. You pat the dog (awww) and free him from the pole. The dog runs off the who knows where and reveals a key underneath the spot he was standing on. You knew the key would be useful and grabbed it. You heard a small metal object drop to the ground as the dog disappears from sight. You follow it, and is greeted by a small, shining metal pen on the floor. It looks delicate, and you are careful when you pick it up, afraid to damage it. The fancy writing on the pen read 'Laser Pen'. Laser Pen? Wonder what that could be... You put the pen in your pocket, knowing it will be useful later."

          )

          inv.remove("bone")

          inv.append("KeyOne")

          inv.append("laserPen")

          showItem(inv)

          HallwayNorth()

    elif input != "use":

      print("Sorry, you cannot do that here.\n")

  elif input == 's':

    HallwayNorth()

  ##ITS WONT WORKKKKKKKKKKKKKKKKKK

#Maybe we send parts of the cod working in differ code i thought the same thing but we can only send one file it siad it on the notification also send me your canva ent

#Its ok I can combine it together so it looks like its together IM

def HallwayEast():

  print("EastHallway\n")

  easternhall = input(

      "There are three rooms in this hallway. A kitchen in the north, a gym in the south and the library in the east. You can also return to the cellar in the west. Which way do you go? Options: n,s,e,w \n"

  )

  if easternhall == 'e':

    Library()

  if easternhall == 's':

    Gym()

  if easternhall == 'n':

    Kitchen()

  if easternhall == 'w':

    cellar()

def HallwayWest():

  print("WestHallway\n")

  westernhall = input(

      "There are three rooms in this hallway. A cafe in the north, a bedroom in the south and a party room in the west. You can also return through the cellar in the east. Options: n, e, s, w\n"

  )

  if westernhall == 'n':

    Cafe()

  if westernhall == 'e':

    cellar()

  if westernhall == 's':

    andyRoom()

  if westernhall == 'w':

    partyRoom()

def Kitchen():

  print("Kitchen\n")

  if 'cookbook' in inv:

    print(

        "You stare at the man who is happily eating your pizza. There is nothing for you to do right now, so you should probably leave."

    )

    HallwayEast()

  pizza = input(

      """You enter the kitchen and see an angry Italian man staring right into your eyes. He says he has been tied there for days and that he knows the code. You ask what code and he says the code to open the cookbook which contains the secret code. You say you will make him a pizza but he must give you he code in exchange, he agrees and you get to work. Firstly, what is your favourite type of pizza from the options below?

  - margherita

  - pepperoni

  - cheese

  - vegan\n""")

  if pizza == "margherita":

    print(

        "this pizza is so unoriginal, but i am not one to complain after , you have fed me  and for that here is the cookbook"

    )

    inv.append("Cookbook")

    HallwayEast()

  elif pizza == "cheese":

    print(

        "why who actually calls this pizza, here is the cookbook get out of my sight you cheesy pizza lover."

    )

    inv.append("Cookbook")

    HallwayEast()

  if pizza == "vegan":

    print(

        "I AM A STRONG MEATEATER, but this is.... delicous here is the key cookbook go leave me to eat this pizza"

    )

    inv.append("Cookbook")

    HallwayEast()

  elif pizza == "leave":

    HallwayEast()

  elif pizza == "pepperoni":

    print(

        "this pizza is quite childish, i love it it reminds me of my youth, here is the key cookbook go and be free"

    )

    inv.append("Cookbook")

    HallwayEast()

  elif pizza != "margherita" "cheese" "vegan" "pepperoni" "leave":

    print(

        "Sorry we do not have the ingredients for that or you have chosen a pizza which makes no sense to feed to a chef"

    )

def Gym():

  print("Gym\n")

  option = input(

      """You enter the gym and greeted with the unpleasant smell of old sweat and decide to ignore. You continue exploring when you come across a treadmill and weights scattered everywhere. you assume this is where your kidnapper trained his men and now you have a tough decision to make to have a workout and be fit for where you believe you are met with the men or you can wait it out and explore the rest of this oddly designed place. 

- stay

- leave\n""")

  if option == "stay":

    print(

        """You get jacked and build up muscle, you run on the treadmill and then you learn about the state of your fitness, but later you learn about how strong you are after you train for a while.

    - stay

    - leave\n""")

  if option == "stay":

    print(

        "You hear the faint sound of footsteps approaching you you decicde it is too dangerous to stay in the gym, you run out the door and leave, if you come back, you dont know what will happen"

    )

    HallwayEast()

  if option == "leave":

    HallwayEast()

def Library():

  print("Library\n")

  print(

      "You are greeted by a friendly woman who points you in the direction of the non-fiction books, you follow her and you inspect the shelves, you see books about history, animals and architecture, but you see a gap in the shelf. Who could possibly have borrowed a book from here? You look around and the librarian is nowhere to be found, so you look at your backpack, for things in their that might help you. Actually, what would help you?"

  )

  motion = input("""What do you want to do here? Options:

- Leave room and go back into the hallway

- place\n""")

  if motion == "place":

    use = input("place what?")

    if use in inv:

      print(

          """You place the cookbook into the slot and the bookshelf creaks open revealing the key, but suddenly the librarian reappears and you see a pair of round fluffy ears on her head. You back away from her, confusion flashes across your face. Wasn’t the librarian a normal human before? You take another glance at her, and notice her face going pale and a dark circle growing around her eyes. Then realisation hit. She’s transforming into a panda. The librarian-turned-panda is strangely adorable, but that was only until it growled at you, and you took another step back. The black and white creature stands protectively in front of the key, as if she’s guarding it. Oh. She IS guarding it. But how does one retrieve a key from an aggressive panda who could probably chomp someone’s hand off in one bite? Your only solution was to knock it out, against your will. You have to, to get out of here alive. You don’t have a choice. The panda suddenly lunges out at you, as quick as a bird. You dodge, but barely. The animal flies past you, crashing into a bookshelf, knocking it over. The bookshelf shook and collapsed, and a bucket of books were dumped onto the panda’s head. A particularly large old looking book fell on her head, knocking her out. Well, that saves you the trouble of abusing a cute furry animal at least. You head over to the panda (librarian?) and lifts the bookshelf off her. It took some effort though, that giant piece of wood isn’t the lightest thing in the world. You then proceeded to lift a heavy panda onto a nearby couch, making sure she’s okay. Gosh, you should become a professional weightlifter at this point. You turned around, grabbed the little golden key from behind the fake bookshelf-door, and left the library."""

      )

      inv.remove("Cookbook")

      inv.append("KeyThree")

      showItem()

      HallwayEast()

  elif motion == 'leave':

    HallwayEast()

  elif motion != 'leave' 'place':

    print("You can't do that here.")

def Cafe():

  print("Cafe\n")

  if "coffee" in inv:

    print(

        "You look around. You do not need to do anything here. Friendly Barista is staring blankly at a wall. You decide to leave."

    )

    HallwayWest()

  elif "coffee" not in inv:

    choice = input("Take or leave the coffee offered by friendly barista")

  if choice == "take":

    print(

        "Friendly Baraista gives a piping hot coffee in a simple mug. You gladly accept the coffee and hold on to it. Maybe you could use it later..."

    )

    inv.append("coffee")

    HallwayWest()

  elif choice == "leave":

    HallwayWest()

  elif choice != "take" "leave":

    print("You can not do that here. What do you want to do?")

def partyRoom():

  print("Party Room\n")

  party = input("""Party Room

You enter a brightly coloured room with helium balloons and a tall clown who has a bright rainbow wig and a giant red nose. The tall clown is smiling a big, bright, red smile. Making eye contact with you as you walk across the room, however, this tall clown  does not make any effort to provoke you, rendering it harmless. In the centre of the room, there is a 5-layer birthday cake. It looks and smells a bit stale, but it still is as bright as a fresh one and looks absolutely delicious. You mouth waters as you approach it, but as you get closer, you realise the sugary icing spells out 'HAPPY BIRTHDAY; DO NOT EAT ME' but the cake looks so good, and you're a bit hungry, your mouth starts watering just thinking about the cake. Would it hurt just to take a single slice?

- eat

- talk

- w\n""")

  if party == "eat":

    cake = input(

        """You eat the cake. Your tongue goes on a flavour adventure with all the yummy sweet flavours of the 5 layers, eat bite gets better and better, melting in your mouth. You want to eat the whole cake. However, your gag reflexes stop you. You start vomiting non-stop all over the room, the tall clown looks at you with a disgusted face. Your breath hitched and your vision goes blurry and you start tearing up. You feel like you have just been hit by a heavy blunt object and your entire body is on fire. Everything goes black. You wake up, the last thing you remember is eating the most delicious cake you have ever eaten and passing out right after, everything else in your memory seems to go to a blur. There is a a tall clown looking at you with a puzzled expression.

    - talk

    - w\n""")

    if cake == "talk":

      print(

          """"Wow... I'm surprised you made it out alive. Please don't do anything like that again, and please try to get out of here." You agree and quickly leave the room."""

      )

      HallwayEast()

    elif cake == "w":

      HallwayEast()

  elif party == "talk":

    print(

        "You try to start a conversation with the tall clown that is eyeing you. You ask about the 5-layer cake with the strange iced message. The tall clown nods, he warns you not to eat the cake. He looks like he he is on the verge of tears, his watery eyes were sparkling and his delicate voice trembling. Was eating this cake that bad? Oh well. The clown seems really desperate for you to not eat the cake, so you leave the cake and the party room. As you close the door, you hear a huge sigh of relief from the tall clown."

    )

    HallwayEast()

  elif party == "w":

    HallwayEast()

  elif party != "w" "eat" "talk":

    print("You don't think that will do anything for now.")

def andyRoom():

  print("Andy's Room")

  print(

      """You enter a dirty room full of mould, sweaty and dirty clothes, empty, unwashed coffee mugs and yellowed open books. It reeks of coffee and expired milk. You see a tired guy in a bad mood.

“Ugh… I’m so tired…” he groans.

You ask about the keys.

“Oh… gimme a coffee and I’ll give you the clue to the key… Zzz”. Options: use, n"""

  )

if input == "use":

  use = input("use what?")

  if use in inv:

    print("you decide to use the ", use)

    if use == "coffee":

      print(

          "He drinks it immediately, and gives you back the cup. 'Thanks for the coffee, the name's Andy, by the way.' He gives you a small lever thing, which he says 'Look at me and I'll look at you, no matter what, no matter who, you'll always see that there'll be two. To find the key, you must know yourself well. If you don't, you'll be locked in this cell! What am I?' You think to yoursself and try to think of the answer. There are three  "

      )

      inv.append("lever")

      showItem(inv)

      HallwayWest()

    elif use != "coffee":

      print(

          " No coffee, no key, it's as clear as can be, come back and hand me one and then we'll be done"

      )

elif input == 'n':

  HallwayWest()

def lockedRoom():

  if "KeyOne" "KeyTwo" "KeyThree" not in inv:

    goback = input(

        "There is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible. You can go: n to the cellar"

    )

    if goback == "n":

      cellar()

  elif "KeyOne" "KeyTwo" "KeyThree" in inv:

    print("The locked door clicks open.")

    inv.remove("KeyOne")

    inv.remove("KeyTwo")

    inv.remove("KeyThree")

    showItem()

    print(

        "There is a peculiar looking safe on a table inside of the otherwise empty room. Mybe you have to use something like a laser to cut the safe open. What do you use?"

    )

    if input == "use":

      use = input("use what?")

      if use in inv:

        print("you decide to use the ", use)

        if use == "laserPen":

          print(

              "The safe opens, with a strange blue diamond inside. It shines a bright blue glow in every direction, as if producing it's own light. You reach to grab it, but a bark distracts you. You turn around, delighted to see the puppy from the other room. It licks your hand and jumps into your arms. You touch the diamond and you suddendly get transported onto your bed, back in your own home. You have a good night's sleep with your new furry friend Teddy by your side."

          )

          print(

              """You wake up in the morning and turn on this morning's news. It reads:

  "FRIENDLY BARISTA, TIRED 'ANDY' GUY, PIZZA CHEF GUY AND TALL CLOWN KILLED IN FREAK ACCIDENT. AUTHORITIES STILL INVESTIGATING CAUSE OF DEATH." """

          )

#------------start room---------------------

cellar()

