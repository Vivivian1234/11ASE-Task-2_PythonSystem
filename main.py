

player_name = []

class inventory():
  inventory = {}
  print ("Use what? Options:")
  
  for i in inventory:
    print(i)

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

thisdict = {
  "A": 21,
  "B": 47,
  "C": 89
}

print(thisdict)

def main2():
    inventory = ["cheese, 12", "broken bottle holder, 1", "lollipop, 1"]
    
    for item in inventory:
        item_desc, number = item.split(", ")
        print (f"{item_desc} x {number}")
        

def main():
    print("The Cellar\n")
    print("You wake up, the last thing you remember is suffocating in gassy fabric, closing in from behind. This place looks familiar, you have definitely been here sometime before, but you can't seem to remember anything. The yellowish wallpaper and the cold floor all feel so homely, but that doesn't matter now. Why can't you remember anything and yet everything seems so familiar?")

    name = input("What is your name?\n")
    name = name.lower()
    name = name.capitalize()
    player_name.append(name)

    print("Good, at least you remember your name.\n")
    print("There are 3 hallways in front of you. One to the north, east and west. To the south is a locked door with 3 keyholes in it. Perhaps that is the way out. You should find the 3 keys to the door as soon as possible.")

    action = input("What do you want to do here?\n")