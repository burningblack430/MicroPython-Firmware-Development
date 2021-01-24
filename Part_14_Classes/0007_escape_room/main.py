# python pyboard.py --device COM3 -f cp main.py :

from machine import Pin, I2C
import neopixel
import ssd1306
from Grid import Grid
from EscapeRoomPlayer import EscapeRoomPlayer
from FileManager import FileManager
from Game import Game

LED_COUNT = 64
GRID_WIDTH = 8
GRID_HEIGHT = 8
np = neopixel.NeoPixel(Pin(2), LED_COUNT)
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
btn_1 = Pin(33, Pin.IN)
btn_2 = Pin(32, Pin.IN)
btn_3 = Pin(35, Pin.IN)
btn_4 = Pin(34, Pin.IN)
grid = Grid(GRID_WIDTH, GRID_HEIGHT)
player = EscapeRoomPlayer()
file_manager = FileManager()
game = Game()

if __name__ == '__main__':
    player_location = None
    response = None
    final_question = False

    previous_player_location = player_location
    update_grid = grid.update(player)

    while True:
        # To ensure we do not generate a question if the player is hitting a wall
        # or not entering a valid move
        previous_player_location = player_location
        grid.display(np, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
        while True:
            # noinspection PyArgumentList
            if btn_1.value():
                player_location = player.move_east_btn(grid)
                update_grid = grid.update(player)
                break
            elif btn_2.value():
                player_location = player.move_west_btn(grid)
                update_grid = grid.update(player)
                break
            elif btn_3.value():
                player_location = player.move_north_btn(grid)
                update_grid = grid.update(player)
                break
            elif btn_4.value():
                player_location = player.move_south_btn(grid)
                update_grid = grid.update(player)
                break

        # random_location = (x, y) = game.generate_random_numbers(grid)
        # if random_location == player_location and random_location != previous_player_location:
        #     random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
        #         = game.ask_random_question()
        #     display.show(Image.SURPRISED)
        #     say(random_question, speed=SPEED)
        #     say('Press 1 for {0}.'.format(answer_1), speed=SPEED)
        #     say('Press 2 for {0}.'.format(answer_2), speed=SPEED)
        #     say('Press 3 for {0}.'.format(answer_3), speed=SPEED)
        #     display.show(Image.HAPPY)
        #     while True:
        #         if button_a.is_pressed():
        #             response = 1
        #             break
        #         elif pin_logo.is_touched():
        #             response = 2
        #             break
        #         elif button_b.is_pressed():
        #             response = 3
        #             break
        #     if response == correct_answer_index + 1:
        #         display.show(Image.SURPRISED)
        #         say(game.correct_answer_response(), speed=SPEED)
        #         inventory = player.get_inventory(file_manager)
        #         player.inventory.append(inventory)
        #         if 'Red Key' in player.inventory:
        #             final_question = True
        #         if 'Red Key' not in player.inventory and not final_question:
        #             receive_red_key = game.generate_random_number(grid)
        #             if receive_red_key == 2:
        #                 display.show(Image.SURPRISED)
        #                 say(player.pick_up_red_key(file_manager), speed=SPEED)
        #                 final_question = True
        #             else:
        #                 display.show(Image.SURPRISED)
        #                 say(player.without_red_key(), speed=SPEED)
        #         elif final_question:
        #             display.show(Image.SURPRISED)
        #             say(game.win(file_manager), speed=SPEED)
        #             music.play(music.POWER_UP)
        #             display.show(Image.ALL_CLOCKS, loop=True, delay=100)
        #     else:
        #         display.show(Image.SURPRISED)
        #         say(game.incorrect_answer_response(correct_answer), speed=SPEED)
