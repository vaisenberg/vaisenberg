from game import Game

def get_user_menu_choice():
    print("\n--- Rock, Paper, Scissors Menu ---")
    print("MAKE YOUR RANDOM CHOICE ANGAINST COMPUTER")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    while True:
        choice = input("Choose an option (1, 2, or 3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def print_results(results):
    """Print the results of the games played."""
    print("\n--- Game Summary ---")
    print(f"Games played: {results['win'] + results['loss'] + results['draw']}")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing Rock, Paper, Scissors!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    game = Game()

    while True:
        choice = get_user_menu_choice()

        if choice == '1':  
            game_result = game.play()

            if game_result == 'win':
                results["win"] += 1
            elif game_result == 'loss':
                results["loss"] += 1
            elif game_result == 'draw':
                results["draw"] += 1

        elif choice == '2':  
            print_results(results)

        elif choice == '3': 
            print_results(results)
            print("Goodbye!")
            break

main()
