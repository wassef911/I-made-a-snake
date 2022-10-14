# Import the Turtle Graphics and random modules
import turtle

from src.enum import Parameters
from src.helpers import get_random_food_position

from .generic import GenericSnakeGame
from .movement import Movement


class SnakeGame(GenericSnakeGame, Movement):
    def __init__(self):
        self.food_position = get_random_food_position()
        # Create a window where we will do our drawing.
        self.screen = turtle.Screen()
        self.screen.setup(
            Parameters.WIDTH, Parameters.HEIGHT
        )  # Set the dimensions of the Turtle Graphics window.
        self.screen.title("Snake")
        self.screen.bgcolor("white")
        self.screen.tracer(0)  # Turn off automatic animation.

        # Event handlers
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_right, "Right")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_left, "Left")

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

    def reset(self):
        """
        Initialize all parameters to restart the game
        The initial snake positions parameters are snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
        """
        self.snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        self.snake_direction = 'up'
        self.food_position = get_random_food_position()
        self.food.goto(self.food_position)
        self.score = 0
        self.game_loop()

    def game_loop(self):
        """
        The main loop to run the gaim
        """
        # Cleaning the environment for a new start
        self.stamper.clearstamps()

        new_head = self.snake[-1].copy()  # save the snake head
        new_head[0] += self.offsets[self.snake_direction][0]  # Transition action
        new_head[1] += self.offsets[self.snake_direction][1]

        # Check collisions
        if (
            new_head in self.snake
            or new_head[0] < -Parameters.WIDTH / 2
            or new_head[0] > Parameters.WIDTH / 2
            or new_head[1] < -Parameters.HEIGHT / 2
            or new_head[1] > Parameters.HEIGHT / 2
        ):
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
            self.screen.title(f"Snake Game. Score: {self.score}")
            self.screen.update()

            # Rinse and repeat
            turtle.ontimer(self.game_loop, Parameters.DELAY)
