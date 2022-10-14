class Movement:

    snake_direction = "up"
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]

    def go_up(self):
        if self.snake_direction != "down":
            self.snake_direction = "up"

    def go_right(self):
        if self.snake_direction != "left":
            self.snake_direction = "right"

    def go_down(self):
        if self.snake_direction != "up":
            self.snake_direction = "down"

    def go_left(self):
        if self.snake_direction != "right":
            self.snake_direction = "left"
