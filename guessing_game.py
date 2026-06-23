import random

def play_game():
    print("=== The Number Guessing Game ===")
    print("I am thinking of a number between 1 and 100.")
    
    # Generate a secret random integer
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nTake a guess: "))
        except ValueError:
            print("That's not a valid number. Try again.")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"🎉 Correct! You found the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
