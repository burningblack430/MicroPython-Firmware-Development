# python pyboard.py --device COM3 -f cp main2.py :

from time import sleep
from machine import Pin, I2C
import neopixel
import ssd1306

n = 64 # Define LED quantity
np = neopixel.NeoPixel(Pin(2), n)  # Create the NeoPixel object
np[0] = (64, 0, 0)
np.write()

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

btn_1 = Pin(33, Pin.IN)
btn_2 = Pin(32, Pin.IN)
btn_3 = Pin(35, Pin.IN)
btn_4 = Pin(34, Pin.IN)

oled_width: int = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

my_text = 'When was the micro:bit foundation created?'
my_text_1 = my_text[0:15]
my_text_2 = my_text[15:30]
my_text_3 = my_text[30:45]
my_text_4 = my_text[45:]

oled.text(my_text_1, 0, 0)
oled.text(my_text_2, 0, 10)
oled.text(my_text_3, 0, 20)
oled.text(my_text_4, 0, 30)

oled.show()


while True:
    # noinspection PyArgumentList
    if btn_1.value():
        print('hi')
        sleep(0.25)

