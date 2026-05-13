# 5.1 - все поля сделаны приватными, доступ оставлен только через getters
class Hero:
    def __init__(self, name="Unknown", health=100, level=1, weapon=None, armor=None, coordinates=None):
        self.__name = name
        self.__health = health
        self.__level = level
        self.__weapon = weapon
        self.__armor = armor
        self.__coordinates = coordinates

    def Move(self, new_point: Coordinate):
        self.coordinates = new_point

    def get_coordinates(self):
        return self.coordinates
    
    def get_health(self):
        return self.health

    def Heal(self, points):
        if self.health < 100:
            if self.health + points >= 100:
                self.health = 100
            else:
                self.health += points

    def Attack(self, target: Hero):
        if self.weapon:
            target.get_damage(self.weapon.get_damage())

    def get_damage(self, damage):
        defence = 0
        if self.armor:
            defence = self.armor.get_defence() 
        if defence > damage:
            return
        self.health = self.health - damage + defence

    def EquipWeapon(self, weapon: Weapon):
        self.weapon = weapon

class Coordinate:
    def __init__(self, xPoint, yPoint):
        self.__x = xPoint
        self.__y = yPoint

class Weapon:
    def __init__(self, name, damage, weight, durability):
        self.__name = name
        self.__damage = damage
        self.__weight = weight
        self.__durability = durability

    def get_damage(self):
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
        self.__name = name
        self.__defence = defense
        self.__weight = weight
        self.__durability = durability

    def get_defence(self):
        return self.defence

elf = Hero()
human = Hero()

human.Move(Coordinate(1, 2))
print(human.get_coordinates)

print("before attack")
print(f" здоровье: {human.get_health}")

elf.EquipWeapon(Weapon("sword", 40, 100, 100))
elf.Attack(human)

print("after attack")
print(f" здоровье: {human.get_health}")


#################### 
# 5.2
# example 1
class AnimalBag:
    def __init__(self, name="Unknown", weight=1, color="black"):
        self._name = name         
        self._weight = weight     
        self._color = color       

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}, {self._color}, {self._weight} kg"


class CatBag(AnimalBag):
    def __init__(self, name="Unknown", weight=1, color="black", plastic_type='none'):
        super().__init__(name, weight, color)
        self._plastic_type = plastic_type  

    def get_scratch_resistance(self):
        resistance = {
            'polycarbonate': 'high',
            'polypropylene': 'medium',
            'none': 'low'
        }
        return resistance.get(self._plastic_type, 'unknown')

    def recommended_cat_weight(self):
        max_cat_weight = self._weight * 5
        return round(max_cat_weight, 1)


class DogBag(AnimalBag):
    def __init__(self, name="Unknown", weight=1, color="black", lock_type='none'):
        super().__init__(name, weight, color)
        self._lock_type = lock_type  

    def is_lock_secure(self):
        secure_locks = ['combination', 'double_zipper', 'metal_clip']
        return self._lock_type in secure_locks

    def max_dog_weight(self):
        max_dog_weight = self._weight * 4
        return round(max_dog_weight, 1)

# example 2

class Engine:
    def __init__(self, power, weight, efficiency, manufacturer, serial_number):
        self._power = power
        self._weight = weight
        self._efficiency = efficiency
        self._manufacturer = manufacturer
        self._serial_number = serial_number

class PetrolEngine(Engine):
    def __init__(self, power, weight, efficiency, manufacturer, serial_number,
                 displacement, cylinder_count, injection_type):
        super().__init__(power, weight, efficiency, manufacturer, serial_number)
        self._displacement = displacement      
        self._cylinder_count = cylinder_count  
        self._injection_type = injection_type  

    def calculate_fuel_consumption(self, hours, avg_power_percent=70):
        load_factor = avg_power_percent / 100.0
        hourly_rate = self._displacement * 0.3 * load_factor
        return round(hourly_rate * hours, 2)

    def get_engine_signature(self):
        return (f"Бензиновый двигатель: {self._displacement}л, {self._cylinder_count} цил., "
                f"впрыск {self._injection_type}, мощность {self._power} л.с.")


class ElectricEngine(Engine):
    def __init__(self, power, weight, efficiency, manufacturer, serial_number,
                 battery_capacity, nominal_voltage, max_current):
        super().__init__(power, weight, efficiency, manufacturer, serial_number)
        self._battery_capacity = battery_capacity  
        self._nominal_voltage = nominal_voltage    
        self._max_current = max_current            

    def calculate_range(self, average_power_consumption=150):
        if average_power_consumption <= 0:
            return 0
        energy_wh = self._battery_capacity * 1000 
        return round(energy_wh / average_power_consumption, 1)

    def get_max_power_watts(self):
        electrical_power_w = self._nominal_voltage * self._max_current
        mechanical_power_w = self._power * 735.5    # 1 л.с. ≈ 735.5 Вт
        return {
            'electrical_watts': electrical_power_w,
            'mechanical_watts': round(mechanical_power_w, 1),
            'efficiency_match': electrical_power_w >= mechanical_power_w
        }


