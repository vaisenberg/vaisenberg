#Exercise 1 - Cats


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name 
        self.age = cat_age
    def show_details(self):
     print(f"Name: {self.name} Age:{self.age}")

cat_name = ['Ivy', 'Pearl', 'Ginger']
cat_age = [1, 5, 9]
cats = []
oldest_cat = []
for name, age in zip(cat_name, cat_age):
    cat = Cat(name, age)
    cats.append(cat)

for cat in cats:
    cat.show_details()

def oldest_age(cats):
    oldest_cat = cats[0]  
    for cat in cats:
        if cat.age > oldest_cat.age: 
            oldest_cat = cat  
    return oldest_cat

oldest_cat = oldest_age(cats)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#exercise 2 :Dogs

class Dogs:
    def __init__(self,dog_name,dog_height):
        self.name = dog_name
        self.height = dog_height
    def show_details(self):
        print(f"Name: {self.name} Height:{self.height} cm")
#Function BARK
    def bark(self):
        print(f"{self.name} goes woof!")

#Function JUMP 
    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high")

#object called davids_dog
davids_dog = Dogs("Rex", 50)
davids_dog.show_details()
davids_dog.bark()
davids_dog.jump()
#sarahs_dog
sarahs_dog = Dogs("Teacup", 20)
sarahs_dog.show_details()
sarahs_dog.bark()
sarahs_dog.jump()
if sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}")
else:
    print(f"The bigger dog is {davids_dog.name}")

#  Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
       self.lyrics = lyrics
   
    def sing_me_a_song(self):
     for line in self.lyrics:
            print(line)
   
song = Song(["There’s a lady who's sure",
    "All that glitters is gold",
    "And she’s buying a stairway to heaven"])

song.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
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



