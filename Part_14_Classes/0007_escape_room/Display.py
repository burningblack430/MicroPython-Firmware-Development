from time import sleep


class Display:
    """
    Class to handle a generic oled display
    """

    @staticmethod
    def text(oled, text, wait=0, clear=False):
        """
        Method to take a text str and break it up into 4 lines
        to properly display on the oled

        Params:
            oled: object
            question: str
            wait: int, optional
            clear: bool, optional
        """
        oled.fill(0)
        oled.show()
        text_line_1 = text[0:15]
        text_line_2 = text[15:30]
        text_line_3 = text[30:45]
        text_line_4 = text[45:]
        oled.text(text_line_1, 0, 0)
        oled.text(text_line_2, 0, 10)
        oled.text(text_line_3, 0, 20)
        oled.text(text_line_4, 0, 30)
        oled.show()
        sleep(wait)
        if clear:
            oled.fill(0)
            oled.show()

    @staticmethod
    def texts(oled, text_1, text_2, text_3=None, text_4=None, wait=0, clear=False):
        """
        Method to take a 4 text strings and break it up into
        a max of 4 lines to properly display on the oled

        Params:
            oled: object
            text_1: str
            text_2: str
            text_3: str, optional
            text_4: str, optional
            wait: int, optional
            clear: bool, optional
        """
        oled.fill(0)
        oled.show()
        text_line_3 = None
        text_line_4 = None
        text_line_1 = text_1
        text_line_2 = text_2
        if text_3:
            text_line_3 = text_3
        if text_4:
            text_line_4 = text_4
        oled.text(text_line_1, 0, 0)
        oled.text(text_line_2, 0, 10)
        if text_3:
            oled.text(text_line_3, 0, 20)
        if text_4:
            oled.text(text_line_4, 0, 30)
        oled.show()
        sleep(wait)
        if clear:
            oled.fill(0)
            oled.show()

    # @staticmethod
    # def random_colors(np, led_count):
    #     """
    #     Method to display a random color animation
    #
    #     Params:
    #         np: object
    #         led_count: int
    #     """
    #     while True:
    #         for i in range(0, led_count):
    #             np[i] = (randint(0, 255), randint(0, 255), randint(0, 255))
    #             np.write()
    #             sleep(0.2)
    #
    # @staticmethod
    # def reverse_animation(np, led_count):
    #     """
    #     Method to display a reverse animation
    #
    #     Params:
    #         np: object
    #         led_count: int
    #     """
    #     while True:
    #         for i in range(led_count, 0, -1):
    #             np[i - 1] = (randint(0, 150), randint(0, 150), randint(0, 150))
    #             np.write()
    #             sleep(.2)
    #
    # @staticmethod
    # def win_animation(np, led_count):
    #     """
    #     Method to display a win animation
    #
    #     Params:
    #         np: object
    #         led_count: int
    #     """
    #     blue_red = [(0, 0, 64), (64, 0, 0), (0, 0, 64), (64, 0, 0)]
    #     while True:
    #         for i in range(0, led_count):
    #             np[i] = blue_red[randint(0, 3)]
    #             np[i - 4] = (0, 0, 0)
    #             np.write()
    #             sleep(0.05)

    @staticmethod
    def demo(np, led_count):

        # cycle
        for i in range(4 * led_count):
            for j in range(led_count):
                np[j] = (0, 0, 0)
            np[i % led_count] = (255, 255, 255)
            np.write()
            sleep(0.25)

        # bounce
        for i in range(4 * led_count):
            for j in range(led_count):
                np[j] = (0, 0, 128)
            if (i // led_count) % 2 == 0:
                np[i % led_count] = (0, 0, 0)
            else:
                np[led_count - 1 - (i % led_count)] = (0, 0, 0)
            np.write()
            sleep(0.6)

        # fade in/out
        for i in range(0, 4 * 256, 8):
            for j in range(led_count):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                np[j] = (val, 0, 0)
            np.write()

        # clear
        for i in range(led_count):
            np[i] = (0, 0, 0)
        np.write()
