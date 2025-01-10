# Imports the random module to generate random numbers to choose emojis randomly
import random

def generate_emoji_question():
    """
    Generates a random number of emojis (between 1 and 10) and returns:
    - A string containing the emojis.
    - The count of emojis as an integer.
    """
    emoji = random.choice(['⭐', '🚀', '💖', '🌊'])  # Randomly select an emoji
    count = random.randint(1, 10)  # Randomly choose a number between 1 and 10
    return emoji * count, count

def check_answer(user_input, correct_count):
    """
    Checks if the user's input matches the correct count of emojis.
    
    Args:
        user_input (int): The number entered by the user.
        correct_count (int): The correct number of emojis.
    
    Returns:
        bool: True if the user's input matches the correct count, False otherwise.
    """
    return user_input == correct_count

