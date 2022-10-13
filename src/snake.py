# Import the Turtle Graphics and random modules
import turtle
import random

from .utils import get_distance

from .const import Parameters
from .movement import Movement

class SnakeGame(Movement):

    screen = turtle.Screen()
    food = turtle.Turtle()
    stamper = turtle.Turtle()
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = 'up'
    food_position = [0,0]
    offsets = {
        "up": (0, 20),
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }

    def __init__(self):
        self.food_position = self.get_random_food_pos()
        # Create a window where we will do our drawing.
        screen = turtle.Screen()
        screen.setup(Parameters.WIDTH, Parameters.HEIGHT)  # Set the dimensions of the Turtle Graphics window.
        screen.title("Snake")
        screen.bgcolor("pink")
        screen.tracer(0)  # Turn off automatic animation.

        # Event handlers
        screen.listen()
        screen.onkey(self.go_up, "Up")
        screen.onkey(self.go_right, "Right")
        screen.onkey(self.go_down, "Down")
        screen.onkey(self.go_left, "Left")

        # Create a turtle to do your bidding
        self.stamper.shape("square")
        self.stamper.penup()

        # Food
        self.food.shape("circle")
        self.food.color("red")
        self.food.shapesize(Parameters.FOOD_SIZE / 20)
        self.food.penup()

        # Set animation in motion
        self.reset()

        # Finish nicely
        turtle.done()

    def food_collision(self):
        """
            Returns true if the snake eats the food, false otherwise
        """
        if get_distance(self.snake[-1], self.food_position) < 20:
            self.food.goto(SnakeGame.get_random_food_pos())
            return True
        return False

    @staticmethod
    def get_random_food_pos():
        """
            Create a random position of food.
            Returns (x,y) the food position. Do not forget to consider FOOD_SIZE
        """
        x = random.randint(- Parameters.WIDTH / 2 + Parameters.FOOD_SIZE, Parameters.WIDTH / 2 - Parameters.FOOD_SIZE)
        y = random.randint(- Parameters.HEIGHT / 2 + Parameters.FOOD_SIZE, Parameters.HEIGHT / 2 - Parameters.FOOD_SIZE)
        return (x, y)

    def reset(self):
        """
            Initialize all parameters to restart the game
            The initial snake positions parameters are snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
        """
        self.snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        self.snake_direction = 'up'
        self.food_position = SnakeGame.get_random_food_pos()
        self.food.goto(self.food_position)
        self.game_loop()
   
    def game_loop(self):
        """
            The main loop to run the gaim
        """
        # Cleaning the environment for a new start
        self.stamper.clearstamps()  # Remove existing stamps made by stamper.

        new_head = self.snake[-1].copy()  # save the snake head
        new_head[0] += self.offsets[self.snake_direction][0]  # Transition action
        new_head[1] += self.offsets[self.snake_direction][1]

        # Check collisions
        if new_head in self.snake or new_head[0] < - Parameters.WIDTH / 2 or new_head[0] > Parameters.WIDTH / 2 \
                or new_head[1] < - Parameters.HEIGHT / 2 or new_head[1] > Parameters.HEIGHT / 2:
            self.reset()
        else:
            # Add new head to snake body.
            self.snake.append(new_head)

            # Check food collision
            if not self.food_collision():
                self.snake.pop(0)  # Keep the snake the same length unless fed.

            # Draw snake for the first time.
            for segment in self.snake:
                self.stamper.goto(segment[0], segment[1])
                self.stamper.stamp()

            # Refresh screen
            self.screen.title(f"Snake Game. Score: {0}") # TODO SCORE
            self.screen.update()

            # Rinse and repeat
            turtle.ontimer(self.game_loop, Parameters.DELAY)


