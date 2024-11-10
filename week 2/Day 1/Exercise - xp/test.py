
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
# adding new animals to the list of animals
    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        else:
            print(f"{animal} is already in the zoo")
 #Printing out the animals   
    def get_animals(self):
        if self.animals:
            for animal in self.animals:
                print(f"{animal}")
        else:
                print("There is no animals in the zoo yet")

    def sell_animals(self, animal):
        animal = animal.strip().capitalize() 
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} has been sold.")
        else:
            print(f"{animal} is not in the zoo. Please check again.")
      

    def group_animals(self):
        grouped_animals = {}
        sorted_animals = sorted(self.animals)
        
        group_number = 1
        current_letter = None
        for animal in sorted_animals:
            first_letter = animal[0].lower()
            
            if first_letter != current_letter:
                grouped_animals[group_number] = [animal]
                group_number += 1
                current_letter = first_letter
            else:
                grouped_animals[group_number - 1].append(animal)
        
        return grouped_animals
        
    def get_grouped_animals(self):
        grouped_animals = self.group_animals() 
        print("\nAnimals grouped in alphabetical order:")
        for number, animals in grouped_animals.items():
            print(f"{number}: {(animals)}")



example = Zoo("example")

example.add_animal("Ape")
example.add_animal("Baboon")
example.add_animal("Emu")
example.add_animal("Cougar")
example.add_animal("Eel")
example.add_animal("Bear")
example.add_animal("Cat")
example.sell_animals("ape")

print("Animals in the example:")
example.get_animals()
example.group_animals()
example.get_grouped_animals()

Zoo(name="ramat_gan_safari")

def zoo_keepers_interface():
    ramat_gan_safari = Zoo("Ramat Gan Safari")
    print("Welcome to Ramat Gan Safari")

    while True:
        action = input("\nChoose an action - (add/view/sell/group/exit): ").lower()

        if action == 'add':
            animal = input("Which animal should we add to the zoo? ")
            ramat_gan_safari.add_animal(animal.capitalize())

        elif action == 'view':
            ramat_gan_safari.get_animals()

        elif action == 'sell':
            animal = input("Which animal should we sell from the zoo? ")
            ramat_gan_safari.sell_animals(animal.capitalize())

        elif action == 'group':
            ramat_gan_safari.get_grouped_animals()

        elif action == 'exit':
            print("Exiting Zoo Management System. Have a great day!")
            break

        else:
            print("Invalid action. Please try again.")
zoo_keepers_interface()


# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)