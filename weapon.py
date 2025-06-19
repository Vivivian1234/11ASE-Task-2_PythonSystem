

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_stats(self):
        print(f"Name: {self.name}")
        print(f"Damage: {self.damage}")


class water_bottle(Weapon):
    def __init__(self):
        super().__init__("water bottle", 10)
        self.crit_damage = 30
        self.crit_chance = 80

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

class broken_bottle_holder(Weapon):
    def __init__(self):
        super().__init__("broken bottle holder", 20)
        self.crit_damage = 70
        self.crit_chance = 25

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

class wine_cork(Weapon):
    def __init__(self):
        super().__init__("wine cork", 1)
        self.crit_damage = 2
        self.crit_chance = 99

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

#------------------------------------------------------------------------------------------------------------------------

class Key1(Weapon):
    def __init__(self):
        super().__init__("key1", 0)
        self.stun_chance = 100

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

class Key2(Weapon):
    def __init__(self):
        super().__init__("key2", 0)
        self.stun_chance = 100

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

class Key3(Weapon):
    def __init__(self):
        super().__init__("key3", 0)
        self.stun_chance = 100

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

#------------------------------------------------------------------------------------------------------------------------

class bone(Weapon):
    def __init__(self):
        super().__init__("bone", 20)
        self.crit_damage = 30
        self.crit_chance = 40

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

class laser_pen(Weapon):
    def __init__(self):
        super().__init__("laser pen", 50)
        self.rebound_chance = 45

    def get_stats(self):
        super().get_stats()
        print(f"Rebound Chance: {self.rebound_chance}%")

class cookbook(Weapon):
    def __init__(self):
        super().__init__("cookbook", 15)
        self.stun_chance = 20

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

class coffee(Weapon):
    def __init__(self):
        super().__init__("coffee", 80)
        self.rebound_chance = 95

    def get_stats(self):
        super().get_stats()
        print(f"Rebound Chance: {self.rebound_chance}%")

class lever(Weapon):
    def __init__(self):
        super().__init__("lever", 10)
        self.crit_damage = 45
        self.crit_chance = 10

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

class coin(Weapon):
    def __init__(self):
        super().__init__("coin", 5)
        self.crit_damage = 10
        self.crit_chance = 85

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")

class note(Weapon):
    def __init__(self):
        super().__init__("note", 0)
        self.stun_chance = 5

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

class helpful_casino_reminder(Weapon):
    def __init__(self):
        super().__init__("helpful casino reminder", 0)
        self.stun_chance = 35

    def get_stats(self):
        super().get_stats()
        print(f"Stun Chance: {self.stun_chance}%")

class socks(Weapon):
    def __init__(self):
        super().__init__("socks", 15)
        self.crit_damage = 20
        self.crit_chance = 75

    def get_stats(self):
        super().get_stats()
        print(f"Crit Damage: {self.crit_damage}")
        print(f"Crit Chance: {self.crit_chance}%")


#------------------------------------------------------------------------------------------------------------------------


def create_weapon(name):
    name = name.lower()
    if name == "water bottle":
        return water_bottle()
    elif name == "broken bottle holder":
        return broken_bottle_holder()
    elif name == "wine cork":
        return wine_cork()
    
    elif name == "key1":
        return Key1()
    elif name == "key2":
        return Key2()
    elif name == "key3":
        return Key3() 

    elif name == "bone":
        return bone()   
    elif name == "laser pen":
        return laser_pen()
    elif name == "cookbook":
        return cookbook()   
    elif name == "coffee":
        return coffee()
    elif name == "lever":
        return lever()   
    elif name == "coin":
        return coin()
    elif name == "note":
        return note()   
    elif name == "helpful casino reminder":
        return helpful_casino_reminder()
    elif name == "socks":
        return socks()   
   
    else:
        return None


