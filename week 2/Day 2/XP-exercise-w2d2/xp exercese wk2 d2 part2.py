#exercise 3
from  xp_exercisew2d2 import Dog  



class PetDog(Dog):
    def __init__(self, name, age, height, trained=False):
        super().__init__(name, age, height)
        self.trained = trained
        self.train()
        self.do_a_trick()
        self.play()

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            
        else:
            print(f"{self.name} is not trained yet.")

dog1 = Dog("Nes", 5, 30,)  
pet_dog1 = PetDog("Bobby", 3, 25,)  
pet_dog2 = PetDog("Rusty", 8, 40,) 

