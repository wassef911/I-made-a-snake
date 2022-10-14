import turtle

from src.helpers import get_distance, get_random_food_position

class GenericSnakeGame:
    score = 0
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    food = turtle.Turtle()
    screen = turtle.Screen()
    stamper = turtle.Turtle()
    food_position = [0, 0]
    offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
    max_accuracy = 20

    def food_collision(self):
        """
        Returns true if the snake eats the food, false otherwise
        """
        if get_distance(self.snake[-1], self.food_position) < self.max_accuracy:
            self.food_position = get_random_food_position()
            self.score += 1
            self.food.goto(self.food_position)
            return True
        return False
