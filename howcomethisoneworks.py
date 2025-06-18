import random

player_inventory = {
    "water bottle": 2,
    "note": 1,
    "broken bottle holder": 1,
    "key1": 1,
    "laser pen": 1
}

weapon_stats = {
    "water bottle": {
        "damage": 10,
        "crit_damage": 30,
        "crit_chance": 80
    },
    "note": {
        "damage": 0,
        "stun_chance": 5
    },
    "broken bottle holder": {
        "damage": 20,
        "crit_damage": 70,
        "crit_chance": 25
    },
    "key1": {
        "damage": 0,
        "stun_chance": 100
    },
    "laser pen": {
        "damage": 50,
        "rebound_chance": 45
    }
}

def display_choices():
    print("---Choose Weapon---")
    for i, (item, qty) in enumerate(player_inventory.items(), 1):
        print(f"\n{i}. {item} x {qty}")
        stats = weapon_stats[item]
        if "crit_chance" in stats:
            print(f"   damage = {stats['damage']}")
            print(f"   damage if crit: {stats['crit_damage']}")
            print(f"   chance of crit: {stats['crit_chance']}%")
        elif "stun_chance" in stats:
            print(f"   damage = {stats['damage']}")
            print(f"   chance of stunning enemy for one turn: {stats['stun_chance']}%")
        elif "rebound_chance" in stats:
            print(f"   damage = {stats['damage']}")
            print(f"   chance of rebounding onto player: {stats['rebound_chance']}%")

def FIGHT():
    player_health = 100
    enemy_health = 100
    enemy_stunned = False
    turn = 1

    print("You enter the battle...blah blah blah")
    print("\n---Your enemy:---")
    print("name: Robot Knight")
    print("weapon: Greatsword")
    print("damage: 30")
    print("chance of stunning itself for one turn: 20%")

    while player_health > 0 and enemy_health > 0:
        print(f"\n===Choice {turn}===")
        display_choices()

        # Get weapon choice
        valid_choice = False
        while not valid_choice:
            try:
                choice = int(input("\nChoose your weapon by number: "))
                item = list(player_inventory.keys())[choice - 1]
                if player_inventory[item] > 0:
                    valid_choice = True
                else:
                    print("You don't have that item anymore.")
            except:
                print("Invalid choice, try again.")

        print(f"\n==Your Turn {turn}==")
        print(f"Your health = {player_health}")
        print(f"Enemy health = {enemy_health}\n")

        stats = weapon_stats[item]

        # Perform attack
        if "crit_chance" in stats:
            crit_roll = random.randint(1, 100)
            if crit_roll <= stats["crit_chance"]:
                damage = stats["crit_damage"]
                print(f"You use the {item}. It crit! It deals {damage} damage.")
            else:
                damage = stats["damage"]
                print(f"You use the {item}. It deals {damage} damage.")
            enemy_health -= damage

        elif "stun_chance" in stats:
            stun_roll = random.randint(1, 100)
            if stun_roll <= stats["stun_chance"]:
                enemy_stunned = True
                print(f"You use the {item}. It deals no damage, but your opponent is stunned for 1 turn.")
            else:
                print(f"You use the {item}, but nothing happens.")

        elif "rebound_chance" in stats:
            rebound_roll = random.randint(1, 100)
            damage = stats["damage"]
            if rebound_roll <= stats["rebound_chance"]:
                player_health -= damage
                print(f"You use the {item}, but it rebounds! You take {damage} damage.")
            else:
                enemy_health -= damage
                print(f"You use the {item}. It deals {damage} damage.")

        print(f"\nYour health = {player_health}")
        print(f"Enemy health = {enemy_health}")

        # Reduce item count
        player_inventory[item] -= 1
        if player_inventory[item] == 0:
            del player_inventory[item]

        # Check win
        if enemy_health <= 0:
            break

        # Enemy Turn
        if not enemy_stunned:
            print(f"\n==Enemy Turn {turn}==")
            print(f"Your health = {player_health}")
            print(f"Enemy health = {enemy_health}\n")

            stun_self = random.randint(1, 100)
            if stun_self <= 20:
                print("The enemy tried to attack but stunned itself.")
                enemy_stunned = True
            else:
                player_health -= 30
                print("The enemy hits you once with its greatsword. It deals 30 damage.")
        else:
            print("The enemy is stunned and misses their turn.")
            enemy_stunned = False

        print(f"\nYour health = {player_health}")
        print(f"Enemy health = {enemy_health}\n")
        turn += 1

    if player_health > 0:
        print("\n=====Congratulations, you won!=====")
        print("You defeated the evil knight, and now you won the prize!")
    else:
        print("\n===You were defeated...===")


FIGHT()
