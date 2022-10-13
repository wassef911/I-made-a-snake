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