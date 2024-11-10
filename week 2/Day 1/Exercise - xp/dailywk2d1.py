#Daily exercise day 1 wk2
#Old MacDonald’s Farm

class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}  
    
    #adding an animal
    def add_animal(self, animal, number_animals=1):
        if animal in self.animals:
            self.animals[animal] += number_animals
        else:
            self.animals[animal] = number_animals

    def get_info(self):
        info = f"{self.farm_name}'s farm\n\n"
        for animal, number_animals in self.animals.items():
            info += f"{animal} : {number_animals}\n"
        info += "\n    E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        sorted_animal_types = sorted(self.animals.keys())
        print(sorted_animal_types)  
        return sorted_animal_types

        

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_with_s = []  #list of animals in plural
    
        for animal in animal_types: # I am stucked with comprehensive - had to do it simple 
            if self.animals[animal] > 1:
                animals_with_s.append(f"{animal}s")  
            else:
                animals_with_s.append(animal)  
     
        return f"{self.farm_name}’s farm has {', '.join(animals_with_s)}."


macdonald = Farm("McDonald")

macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
print(macdonald.get_info())
print(macdonald.get_short_info())

