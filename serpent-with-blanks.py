# Import the Turtle Graphics and random modules
import turtle
import random

from src.const import Parameters
from utils import get_distance

# Cell dimensions to navigate in the serpent matrix
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Snake movements
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def game_loop():
    """
        The main loop to run the gaim
    """
    global snake_direction
     # Cleaning the environment for a new start
    stamper.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()  # save the snake head
    new_head[0] += offsets[snake_direction][0]  # Transition action
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - Parameters.WIDTH / 2 or new_head[0] > Parameters.WIDTH / 2 \
            or new_head[1] < - Parameters.HEIGHT / 2 or new_head[1] > Parameters.HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw snake for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"Snake Game. Score: {0}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, Parameters.DELAY)

def food_collision():
    """
        Returns true if the snake eats the food, false otherwise
    """
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_pos()
        food.goto(food_position)
        return True
    return False

def get_random_food_pos():
    """
        Create a random position of food.
        Returns (x,y) the food position. Do not forget to consider FOOD_SIZE
    """
    x = random.randint(- Parameters.WIDTH / 2 + Parameters.FOOD_SIZE, Parameters.WIDTH / 2 - Parameters.FOOD_SIZE)
    y = random.randint(- Parameters.HEIGHT / 2 + Parameters.FOOD_SIZE, Parameters.HEIGHT / 2 - Parameters.FOOD_SIZE)
    return (x, y)

def reset():
    """
        Initialize all parameters to restart the game
        The initial snake positions parameters are snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    """
    global snake,snake_direction,food_position ,stamper
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = 'up'
    food_position = get_random_food_pos()
    food.goto(food_position)
    game_loop()


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(Parameters.WIDTH, Parameters.HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(Parameters.FOOD_SIZE / 20)
food.penup()

# Set animation in motion
reset()

# Finish nicely
turtle.done()