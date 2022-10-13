# Import the Turtle Graphics and random modules
import turtle
import random

from src.const import Parameters

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


 # The main loop to run the gaim
def game_loop():
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
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)

 # Returns true if the snake eats the food, false otherwise
def food_collision():
    pass
    # TO COMPLETE


 # Create a random position of food.
  # Returns (x,y) the food position. Do not forget to consider FOOD_SIZE
def get_random_food_pos():
    x = random.randint(- Parameters.WIDTH / Parameters.FOOD_SIZE, Parameters.WIDTH / 5 * Parameters.FOOD_SIZE)
    y = random.randint(- Parameters.HEIGHT / Parameters.FOOD_SIZE, Parameters.HEIGHT / 5 * Parameters.FOOD_SIZE)
    return (x, y)

 # Calculate the distance between the two positions and returns the distance
def get_distance(pos1, pos2):
    pass
   # TO COMPLETE

 # Initialize all parameters to restart the game
 # The initial snake positions parameters are snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
def reset():
    global snake,snake_direction
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    # TO COMPLETE


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