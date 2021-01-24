# esptool.py --chip esp32 --port COM3 erase_flash
# esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 *.bin
# python pyboard.py --device COM3 -f cp main.py :

from machine import Pin, SoftI2C, PWM
import neopixel
import ssd1306
from Grid import Grid
from EscapeRoomPlayer import EscapeRoomPlayer
from FileManager import FileManager
from Game import Game
from Display import Display

LED_COUNT = 64
GRID_WIDTH = 8
GRID_HEIGHT = 8
np = neopixel.NeoPixel(Pin(2), LED_COUNT)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
pwm = PWM(Pin(5, Pin.OUT))
pwm.deinit()  # Turn off sound on init
btn_1 = Pin(13, Pin.IN)
btn_2 = Pin(12, Pin.IN)
btn_3 = Pin(14, Pin.IN)
btn_4 = Pin(27, Pin.IN)
grid = Grid(GRID_WIDTH, GRID_HEIGHT)
player = EscapeRoomPlayer()
file_manager = FileManager()
game = Game()
display = Display()

if __name__ == '__main__':
    player_location = None
    response = None
    final_question = False
    generate_random_location = True
    random_location = None

    previous_player_location = player_location
    update_grid = grid.update(player)

    while True:
        # To ensure we do not generate a question if the player is hitting a wall
        # or not entering a valid move
        previous_player_location = player_location
        grid.display(np, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)

        while True:
            # noinspection PyArgumentList
            if not btn_1.value():
                player_location = player.move_east(grid)
                update_grid = grid.update(player)
                break
            elif not btn_2.value():
                player_location = player.move_west(grid)
                update_grid = grid.update(player)
                break
            elif not btn_3.value():
                player_location = player.move_north(grid)
                update_grid = grid.update(player)
                break
            elif not btn_4.value():
                player_location = player.move_south(grid)
                update_grid = grid.update(player)
                break

        if generate_random_location:
            random_location = (x, y) = game.generate_random_numbers(grid)
            print(random_location)
            generate_random_location = False

        if random_location == player_location and random_location != previous_player_location:
            grid.display(np, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
            random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer \
                = game.ask_random_question()
            display.text(oled, random_question, 5)
            display.texts(oled, answer_1, answer_2, answer_3)
            while True:
                # noinspection PyArgumentList
                if not btn_1.value():
                    response = 1
                    break
                elif not btn_2.value():
                    response = 2
                    break
                elif not btn_3.value():
                    response = 3
                    break
            if response == correct_answer_index + 1:
                display.text(oled, game.correct_answer_response(), 3)
                inventory = player.get_inventory(file_manager)
                player.inventory.append(inventory)
                if 'Red Key' in player.inventory:
                    final_question = True
                if 'Red Key' not in player.inventory and not final_question:
                    receive_red_key = game.generate_random_number(grid)
                    if receive_red_key == 2:
                        display.text(oled, player.pick_up_red_key(file_manager), 1, True)
                        final_question = True
                    else:
                        display.text(oled, player.without_red_key(), 3, True)
                elif final_question:
                    display.text(oled, game.win(file_manager), 3, True)
                    # music.play(music.POWER_UP)
                    # display.show(Image.ALL_CLOCKS, loop=True, delay=100)
            else:
                display.text(oled, game.incorrect_answer_response(correct_answer), 3, True)
            generate_random_location = True
            grid.display(np, GRID_HEIGHT, GRID_WIDTH, LED_COUNT, update_grid)
