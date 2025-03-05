class Animal:
    def __init__(self, name, age, weight, energy=100):
        self.name = name
        self.age = age
        self.energy = 100
        self.weight = weight   

    def eat(self):
        if self.energy < 100:
            self.energy += 25
            gained_weight = self.weight * 0.0001
            self.weight += gained_weight
            if self.energy > 100:
                self.energy = 100
            print(f"{self.name} just ate and now has {self.energy} energy and weighs {self.weight} kg.")
        else:
            print(f"{self.name} is full and has {self.energy} energy and weighs {self.weight} kg.")

    def sleep(self):
        """When they sleep they will restore energy"""
        self.energy = 100
        print(f"{self.name} just slept and restored {self.energy} energy.")

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Energy: {self.energy}, Weight: {self.weight}"
    
class Cow(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.milk_produced = 0

    def produce_milk(self):
        """Produces milk only when he has enough energy"""
        if self.energy >= 40:
            self.milk_produced += 3
            self.energy -= 30
            print(f"{self.name} produced 3 liters of milk and now has {self.energy} energy.")
        else:
            print(f"{self.name} does not have enough energy to produce milk.")

    def get_info(self):
        return f"{super().get_info()}, Milk Produced: {self.milk_produced}"
    
class Chicken(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.eggs_laid = 0

    def lay_egg(self):
        """Lays an egg only when he has enough energy"""
        if self.energy >= 30:
            self.eggs_laid += 2
            self.energy -= 20
            print(f"{self.name} laid 2 eggs and now has {self.energy} energy.")
        else:
            print(f"{self.name} does not have enough energy to lay an egg.")

    def get_info(self):
        return f"{super().get_info()}, Eggs Laid: {self.eggs_laid}"
    

class Sheep(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.wool_gained = 0

    def grow_wool(self):
        """We can get his wool only when he has enough energy"""
        if self.energy >= 30:
            self.wool_gained += 1
            self.energy -= 20
            print(f"{self.name}'s wool grew. Thickness: {self.wool_gained}")
        else:
            print(f"{self.name} does not have enough energy to grow wool.")

    def get_info(self):
        return f"{super().get_info()}, Wool thickness: {self.wool_gained}"
    
def run_animal_farm():
    cow = Cow("Mallavoy", 4, 95)
    chicken = Chicken("Jack", 2, 2)
    sheep = Sheep("Baron", 3, 53)

    farm_animals = [cow, chicken, sheep]

    print("=== Welcome to my animal farm! ===")
    

    
    print("\nMorning - Feeding Time: ")
    for animal in farm_animals:
        print(f"\n{animal.get_info()}")
        animal.eat()

    print("\nAfternoon - Work Time: ")
    cow.produce_milk()
    chicken.lay_egg()   
    sheep.grow_wool()

    print("\nEvening - Status check: ")
    for animal in farm_animals:
        print(animal.get_info())

    print("\nNight - Sleep time: ")
    for animal in farm_animals:
        animal.sleep()

    print("\nEnd of the day: ")
    for animal in farm_animals:
        print(animal.get_info())

    print("\n=== End of farm simulation ===")
if __name__ == "__main__":
    run_animal_farm()


    