import re

class Color:
    ANSI_RESET = "\033[0m"

    ANSI_BLACK = "\033[30m"
    ANSI_RED = "\033[31m"
    ANSI_GREEN = "\033[32m"
    ANSI_YELLOW = "\033[33m"
    ANSI_BLUE = "\033[34m"
    ANSI_MAGENTA = "\033[35m"
    ANSI_CYAN = "\033[36m"
    ANSI_WHITE = "\033[37m"

    ANSI_BRIGHT_BLACK = "\033[30;1m"
    ANSI_BRIGHT_RED = "\033[31;1m"
    ANSI_BRIGHT_GREEN = "\033[32;1m"
    ANSI_BRIGHT_YELLOW = "\033[33;1m"
    ANSI_BRIGHT_BLUE = "\033[34;1m"
    ANSI_BRIGHT_MAGENTA = "\033[35;1m"
    ANSI_BRIGHT_CYAN = "\033[36;1m"
    ANSI_BRIGHT_WHITE = "\033[37;1m"

    ANSI_BG_BLACK = "\033[40m"
    ANSI_BG_RED = "\033[41m"
    ANSI_BG_GREEN = "\033[42m"
    ANSI_BG_YELLOW = "\033[43m"
    ANSI_BG_BLUE = "\033[44m"
    ANSI_BG_MAGENTA = "\033[45m"
    ANSI_BG_CYAN = "\033[46m"
    ANSI_BG_WHITE = "\033[47m"

    ANSI_BG_BRIGHT_BLACK = "\033[40;1m"
    ANSI_BG_BRIGHT_RED = "\033[41;1m"
    ANSI_BG_BRIGHT_GREEN = "\033[42;1m"
    ANSI_BG_BRIGHT_YELLOW = "\033[43;1m"
    ANSI_BG_BRIGHT_BLUE = "\033[44;1m"
    ANSI_BG_BRIGHT_MAGENTA = "\033[45;1m"
    ANSI_BG_BRIGHT_CYAN = "\033[46;1m"
    ANSI_BG_BRIGHT_WHITE = "\033[47;1m"

    ANSI_DIM_BLACK = "\033[2;30m"
    ANSI_DIM_RED = "\033[2;31m"
    ANSI_DIM_GREEN = "\033[2;32m"
    ANSI_DIM_YELLOW = "\033[2;33m"
    ANSI_DIM_BLUE = "\033[2;34m"
    ANSI_DIM_MAGENTA = "\033[2;35m"
    ANSI_DIM_CYAN = "\033[2;36m"
    ANSI_DIM_WHITE = "\033[2;37m"

    ANSI_LIGHT_BLACK = "\033[90m"
    ANSI_LIGHT_RED = "\033[91m"
    ANSI_LIGHT_GREEN = "\033[92m"
    ANSI_LIGHT_YELLOW = "\033[93m"
    ANSI_LIGHT_BLUE = "\033[94m"
    ANSI_LIGHT_MAGENTA = "\033[95m"
    ANSI_LIGHT_CYAN = "\033[96m"
    ANSI_LIGHT_WHITE = "\033[97m"

    ANSI_BG_DIM_BLACK = "\033[2;40m"
    ANSI_BG_DIM_RED = "\033[2;41m"
    ANSI_BG_DIM_GREEN = "\033[2;42m"
    ANSI_BG_DIM_YELLOW = "\033[2;43m"
    ANSI_BG_DIM_BLUE = "\033[2;44m"
    ANSI_BG_DIM_MAGENTA = "\033[2;45m"
    ANSI_BG_DIM_CYAN = "\033[2;46m"
    ANSI_BG_DIM_WHITE = "\033[2;47m"

    ANSI_BG_LIGHT_BLACK = "\033[100m"
    ANSI_BG_LIGHT_RED = "\033[101m"
    ANSI_BG_LIGHT_GREEN = "\033[102m"
    ANSI_BG_LIGHT_YELLOW = "\033[103m"
    ANSI_BG_LIGHT_BLUE = "\033[104m"
    ANSI_BG_LIGHT_MAGENTA = "\033[105m"
    ANSI_BG_LIGHT_CYAN = "\033[106m"
    ANSI_BG_LIGHT_WHITE = "\033[107m"

    custom_colors = {} 

    @classmethod
    def apply_color_tags(cls, text):
        color_pattern = re.compile(r'\[(?P<color>\w+)\](?P<text>.*?)\[/\1\]', re.DOTALL)
        formatted_text = text

        for match in color_pattern.finditer(text):
            color_name = match.group('color').upper()

            if color_name in cls.custom_colors:
                color_code = cls.custom_colors[color_name]
            elif hasattr(cls, f'ANSI_{color_name}'):
                color_code = getattr(cls, f'ANSI_{color_name}')
            else:
                color_code = cls.ANSI_RESET

            colored_text = color_code + match.group('text') + cls.ANSI_RESET
            formatted_text = formatted_text.replace(match.group(0), colored_text)

        return formatted_text

    @classmethod
    def add_custom_color(cls, color_name, color_code):
        cls.custom_colors[color_name.upper()] = color_code

    @classmethod
    def remove_custom_color(cls, color_name):
        if color_name.upper() in cls.custom_colors:
            del cls.custom_colors[color_name.upper()]
