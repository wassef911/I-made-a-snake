import turtle

class GenericSnakeGame:
    score = 0
    food = turtle.Turtle()
    screen = turtle.Screen()
    stamper = turtle.Turtle()
    food_position = [0, 0]
    offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
    max_accuracy = 20
