class Hero:
    def __init__(self, name="Unknown", health=100, level=1, weapon=None, armor=None, coordinates=None):
        self.name = name
        self.health = health
        self.level = level
        self.weapon = weapon
        self.armor = armor
        self.coordinates = coordinates

    def Move(self, new_point: Coordinate):
        self.coordinates = new_point

    def Heal(self, points):
        if self.health < 100:
            if self.health + points >= 100:
                self.health = 100
            else:
                self.health += points

    def Attack(self, target: Hero):
        if self.weapon:
            target.GetDamage(self.weapon.GetDamage())

    def GetDamage(self, damage):
        defence = 0
        if self.armor:
            defence = self.armor.GetDefence() 
        if defence > damage:
            return
        self.health = self.health - damage + defence

    def EquipWeapon(self, weapon: Weapon):
        self.weapon = weapon

class Coordinate:
    def __init__(self, xPoint, yPoint):
        self.x = xPoint
        self.y = yPoint

class Weapon:
    def __init__(self, name, damage, weight, durability):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.durability = durability

    def GetDamage(self):
        return self.damage

    def Break(self, modifier):
        self.durability -= modifier

    def Repair(self, points, isFull):
        if isFull:
            self.durability = 100
            return
        self.durability += points
        if self.durability > 100:
            self.durability = 100

class Armor:
    def __init__(self, name, defense, weight, durability):
        self.name = name
        self.defence = defense
        self.weight = weight
        self.durability = durability

    def GetDefence(self):
        return self.defence

elf = Hero()
human = Hero()

human.Move(Coordinate(1, 2))
print(human.coordinates)

print("before attack")
print(f" здоровье: {human.health}")

elf.EquipWeapon(Weapon("sword", 40, 100, 100))
elf.Attack(human)

print("after attack")
print(f" здоровье: {human.health}")