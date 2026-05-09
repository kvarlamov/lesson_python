# Задание 1.1
# - Программа TickTick - планировщик
# Класс задача. Свойства (поля): 
# Идентификатор, 
# Название, 
# Идентификатор списка (в который входит),
# Время начала
# Время напоминания (nullable)
# IsRepeatable (bool)
# Массив тэгов 
#
# - Программа кинопоиск. 
# Класс Фильм. 
# Свойства: 
# Идентификатор, 
# Год выпуска, 
# Режиссер, 
# Жанр, 
# Список актеров


# Задание 1.2

class Hero:
    name = "Unknown" 
    health = 100  
    level = 1
    weapon = None 
    armor = None


class Weapon:
    name = "Unnamed"
    damage = 10
    weight = 1.0
    durability = 100


class Armor:
    name = "Unnamed"
    defense = 5
    weight = 2.0
    durability = 100

elf = Hero()
human = Hero()

sword = Weapon()
shield = Armor()

elf.name = "Legolas"
elf.health = 150
elf.level = 5

sword.name = "Longsword"
sword.damage = 25
sword.weight = 2.5
sword.durability = 80

shield.name = "Wood Shield"
shield.defense = 15
shield.weight = 5.0
shield.durability = 120


print(f"Герой: {elf.name}, здоровье: {elf.health}, уровень: {elf.level}")
print(f"  Оружие: {elf.weapon.name} (урон {elf.weapon.damage}, вес {elf.weapon.weight})")
print(f"  Броня: {elf.armor.name} (защита {elf.armor.defense}, вес {elf.armor.weight})")

# Задание 1.3 - побочный эффект передачи по ссылке

class User:
    name = "Unknown"
    account = 100

user1 = User()
user1.name = "Michail"
user1.account = 10000

# before
print("\n До изменения")
print(f"char1: {user1.name}, здоровье: {user1.account}")

user2 = user1
print(f"char2: {user2.name}, здоровье: {user2.account}")

user2.account = 0
# after - побочный эффект
print("\n Меняем char2, char1 тоже изменяется")
print(f"char1: {user1.name}, здоровье: {user1.account}")
print(f"char2: {user2.name}, здоровье: {user2.account}")
