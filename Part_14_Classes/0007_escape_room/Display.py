class Display:
    """
    Class to handle a generic oled display
    """

    @staticmethod
    def text(oled, text):
        """
        Method to take a text str and break it up into 4 lines
        to properly display on the oled

        Params:
            oled: object
            text: str
        """
        text_line_1 = text[0:15]
        text_line_2 = text[15:30]
        text_line_3 = text[30:45]
        text_line_4 = text[45:]

        oled.text(text_line_1, 0, 0)
        oled.text(text_line_2, 0, 10)
        oled.text(text_line_3, 0, 20)
        oled.text(text_line_4, 0, 30)
