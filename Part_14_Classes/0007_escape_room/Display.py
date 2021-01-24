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
            question: str
        """
        text_line_1 = text[0:15]
        text_line_2 = text[15:30]
        text_line_3 = text[30:45]
        text_line_4 = text[45:]
        oled.text(text_line_1, 0, 0)
        oled.text(text_line_2, 0, 10)
        oled.text(text_line_3, 0, 20)
        oled.text(text_line_4, 0, 30)

    @staticmethod
    def texts(oled, text_1, text_2, text_3=None, text_4=None):
        """
        Method to take a 4 text strings and break it up into
        a max of 4 lines to properly display on the oled

        Params:
            oled: object
            text_1: str
            text_2: str
            text_3: str, optional
            text_4: str, optional
        """
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
