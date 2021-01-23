from time import sleep


class Grid:
    """
    Class to represent a grid
    """

    def __init__(self, led_height=0, led_width=0, led_on='9', led_off='0'):
        """
        Attrs:
            led_height: int
            led_width: int
            led_on: int
            led_off: int
        """
        self.led_height = led_height
        self.led_width = led_width
        self.led_on = led_on
        self.led_off = led_off
        self.available_height = led_height - 2
        self.available_width = led_width - 2

    def create(self):
        """
        Method to create a grid

        Returns:
             str, str, str
        """
        top_wall = self.led_on * self.led_width
        side_walls = ''
        for _ in range(self.available_height):
            side_walls += self.led_on + self.led_off * self.available_width + self.led_on
        bottom_wall = self.led_on * self.led_width
        return top_wall, side_walls, bottom_wall

    def update(self, player):
        """
        Method to handle update with each event where we re-draw
        grid with player's current position

        Params:
            player: object

        Returns:
            grid: str
        """
        top_wall, side_walls, bottom_wall = self.create()
        grid = top_wall + side_walls + bottom_wall
        # Convert to a list so that the element can be mutable to add player char
        temp_grid = list(grid)
        # For each step in y, needs to increment by jumps of row width
        y_adjustment = (player.dy - 1) * self.led_width
        # The index position of player marker in the list-formatted grid
        position = self.led_width + player.dx + y_adjustment
        temp_grid[position] = self.led_on
        grid = ''
        grid = grid.join(temp_grid)
        return grid

    def display(self, np, grid_height, grid_width, led_count, process_grid):
        """
        Method to display grid

        Params:
            np: object
            grid_height: int
            grid_width: int
            led_count: int
            process_grid: str
        """
        black = (0, 0, 0)
        red = (64, 0, 0)
        green = (0, 64, 0)
        index = 0
        for pixel in range(len(process_grid)):
            led = process_grid[index]
            if led == self.led_on:
                # Turn on the wall led's of the top_wall+1 and the 1-bottom_wall
                if (0 <= index <= grid_width) or \
                        index >= (grid_width * grid_width - grid_width):
                    np[index] = red
                else:
                    # Turn on the player led at their current location
                    np[index] = green
                for _ in range(2, grid_height):
                    index_ = grid_height * _
                    # Turn on the right wall led's
                    np[index_ - 1] = red
                    # Turn on the left wall led's less the top two
                    np[index_] = red
            elif led == self.led_off:
                # Available movable space less the current player location
                np[index] = black
            else:
                pass
            if index < led_count-1:
                index += 1
        np.write()
        sleep(0.25)
