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
