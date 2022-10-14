import random

from src.enum import Parameters

def get_distance(pos1, pos2):
    """
        Calculate the distance between the two positions and returns the distance
    Returns:
        Float: distance
    """
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def get_random_food_position():
    """
    Create a random position of food.
    Returns (x,y) the food position. Do not forget to consider FOOD_SIZE
    """
    x = random.randint(
        -Parameters.WIDTH / 2 + Parameters.FOOD_SIZE,
        Parameters.WIDTH / 2 - Parameters.FOOD_SIZE,
    )
    y = random.randint(
        -Parameters.HEIGHT / 2 + Parameters.FOOD_SIZE,
        Parameters.HEIGHT / 2 - Parameters.FOOD_SIZE,
    )
    return (x, y)