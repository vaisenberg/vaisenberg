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