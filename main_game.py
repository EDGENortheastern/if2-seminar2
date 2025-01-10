# Importing the functions from game_logic.py
from game_logic import generate_emoji_question, check_answer
import time  # To track the game timer

def play_game():
    """
    Runs the emoji counting game where the user is asked to count emojis
    within a 30-second time limit. The score is calculated based on correct answers.
    """
    print("Welcome to the Emoji Counting Game!\n")
    print("You have 30 seconds to count emojis and enter the correct number.\n")
    start_time = time.time()
    score = 0

    while True:
        # Generate emojis and their correct count
        emojis, correct_count = generate_emoji_question()
        print(f"How many emojis are here? {emojis}")

        try:
            # Get user input and handle quitting
            user_input = int(input("Enter the number (or -1 to quit): "))
            if user_input == -1:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number!\n")
            continue

        # Check the answer
        if check_answer(user_input, correct_count):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_count}.\n")

        # Check the timer
        elapsed_time = time.time() - start_time
        if elapsed_time > 30:  # 30-second time limit
            print("Time's up!\n")
            break

    # End the game
    print(f"Game over! Your score: {score}")

# Start the game if this script is run
if __name__ == "__main__":
    play_game()
