inventory = ["cheese, 12", "broken bottle holder, 1", "lollipop, 1"]

def main2():
    
    print("\n---Your Backpack---")
    for item in inventory:
        item_desc, number = item.split(", ")
        print (f"{item_desc} x {number}")

        while True:
            action = input("\nWhat would you like to do\nOptions: Use, Exit")
            action = action.lower()

            if action == "use":
                ajhfjosa = input("Use what?")
            elif action == "exit":
                character_list.level_up()
            elif action == "3":
                print("\nThank you for using this program.\n")
                break
            else:
                print("\nInvalid input. Please try again.\n")
        

print("Hello, welcome to the pizzzzzzzzzza shop. Here are 5 pizzas for you.")
inventory.append("pizza, 5")
print("5 pizzas added to Backpack")

main2()

