import unittest
from game_logic import generate_emoji_question, check_answer

class TestGameLogic(unittest.TestCase):

    def test_generate_emoji_question(self):
        """Test that generate_emoji_question returns valid results."""
        emojis, count = generate_emoji_question()
        # Ensure count is between 1 and 10
        self.assertGreaterEqual(count, 1)
        self.assertLessEqual(count, 10)
        # Ensure the length of the emoji string matches the count
        self.assertEqual(len(emojis), count * len(emojis[0]))

    def test_check_answer(self):
        """Test that check_answer correctly evaluates user input."""
        self.assertTrue(check_answer(5, 5))  # Correct input
        self.assertFalse(check_answer(3, 5))  # Incorrect input

# Ensure the tests run only when this file is executed directly
if __name__ == "__main__":
    unittest.main()
