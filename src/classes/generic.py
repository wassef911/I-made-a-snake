import turtle


class GenericSnakeGame:
    food = turtle.Turtle()
    screen = turtle.Screen()
    stamper = turtle.Turtle()
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = 'up'
    food_position = [0, 0]
    offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
