from xp_exercisew2d2 import Dog  # Ensure this import works



class PetDog(Dog):
    def __init__(self, name, age, height, trained=False):
        super().__init__(name, age, height)  # Initialize the base Dog class
        self.trained = trained  # Default trained status is False
        self.train()
       

    def train(self):
        self.bark()  # This assumes the bark method exists in the Dog class
        self.trained = True  # Mark this dog as trained

    def play(self, *args):
        dog_names = [dog.name for dog in args]  # Get the names of the dogs
        print(f"{', '.join(dog_names)} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print((tricks))  # Randomly pick and print a trick
        else:
            print(f"{self.name} is not trained yet.")

# Create PetDog instances
pet_dog1 = PetDog("Bobby", 3, 25)
pet_dog2 = PetDog("Rusty", 8, 40)