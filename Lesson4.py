# Задание 4.1
# Пример 1. Иерархия двигателей. Для наглядности убрал лишние поля
class Car:
    def __init__(self, engine: Engine):
        self.__engine = engine

    # метод заведения машины использует композицию - двигатель, 
    # который полиморфно вызывает метод старт нужного типа двигателя
    def start_car(self): 
        self.__engine.start()

    def modernize(self, new_engine: Engine):
        self.__engine = new_engine

class Engine:
    def __init__(self):
        pass

    def start(self):
        print("заводим двигатель")
    
class PetrolEngine(Engine):
    def __init__(self):
        super().__init__()

    def start(self):
        print("заводим бензиновый двигатель")


class ElectricEngine(Engine):
    def __init__(self):
        super().__init__()   

    def start(self):
        print("заводим электрический двигатель")

print("\n-----1-----")
print("Устанавливаем в авто стандартный бензиновый двигатель")
petrolEngine = PetrolEngine()
car = Car(petrolEngine)
print("Заводим автомобиль с бензиновым двигателем")
car.start_car()

print("Устанавливаем в авто электрический двигатель")
electricEngine = ElectricEngine()
car.modernize(electricEngine)
print("Заводим автомобиль с электрическим двигателем")
car.start_car()


# Пример 2. Иерархия домашних животных (новая)
print("\n-----2-----")
class DomesticAnimal:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def play(self):
        print(f"{self.name} играет")

class Dog(DomesticAnimal):
    def play(self):
        print("принести мячик")

class Cat(DomesticAnimal):
    def play(self):
        print("размотать клубок шерсти")

class Human:
    def __init__(self, pet: DomesticAnimal):
        self.pet = pet   # композиция: домашнее животное

    def play_with_pet(self):
        print("Человек играет с питомцем:", end=" ")
        self.pet.play()   # вызов полиморфного метода play

# Создаём кошку и собаку
cat = Cat("Мурка", 4.2)
dog = Dog("Шарик", 12.5)

print("Человек играет с кошкой")
human1 = Human(cat)
human1.play_with_pet()

print("Человек играет с собакой")
human2 = Human(dog)
human2.play_with_pet()


#4.2
# Полиморфизм подтипов - разработчик описывает как объекты будут 
# реагировать на взаимодействие с ними через общий родительский интерфейс
# т.е. в каждом классе есть "инструмент", который говорит, как его использовать для решения общей задачи
# параметрический полиморфизм - это "универсальный ключ"

#4.3
print("\n-----3-----")
import random

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def fill_random_animals(animal_list: list):
    animal_list.clear()                     # очищаем список
    for _ in range(500):
        if random.choice([Cat, Bird]) is Cat:
            animal_list.append(Cat())
        else:
            animal_list.append(Bird())


animals = []
fill_random_animals(animals)

for animal in animals:
    animal.foo()