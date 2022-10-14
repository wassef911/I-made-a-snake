import unittest

from src.classes.generic import GenericSnakeGame
from src.helpers import get_distance, get_random_food_position


# python -m nose2
class TestSum(unittest.TestCase):
    def test_get_distance(self):
        self.assertEqual(get_distance([10, 80], [0, 80]), 10.0)

    def test_get_random_food_position(self):
        random_position = get_random_food_position()
        self.assertTrue(isinstance(random_position[0], (int)))
        self.assertTrue(isinstance(random_position[1], (int)))

    def test_food_collision(self):
        game = GenericSnakeGame()
        game.food_position = game.snake[-1]
        self.assertTrue(game.food_collision())


if __name__ == '__main__':
    unittest.main()
