from dataclasses import dataclass
from custerm.ansi import Color
from custerm.exceptions import *
import re

@dataclass
class Terminal:
    @staticmethod
    def options(options_list: list) -> str:
        valid_options = [str(i) for i in range(1, len(options_list) + 1)]

        print("Select an option:")
        for i, option in enumerate(options_list, start=1):
            print(f"{i}. {option}")

        while True:
            choice = input("Enter the number of your choice: ")
            if choice in valid_options:
                return options_list[int(choice) - 1]
            else:
                raise InvalidChoiceException()

    @staticmethod
    def print(text: str, markdown: bool = False):
        if markdown:
            try:
                text = Terminal.render_markdown(text)
            except InvalidMarkdownException:
                print("Invalid markdown format")
                return

        text = Color.apply_color_tags(text)
        print(text)

    @staticmethod
    def render_markdown(text: str) -> str:
        patterns = [
            (r'^(#{1,6})\s+(?P<markdown_text>.+)', r'\033[1;36m\2\033[0m'),  # Headings
            (r'\*\*([\w\s]+)\*\*', r'\033[1m\1\033[0m'),  # Bold
            (r'__([\w\s]+)__', r'\033[4m\1\033[0m'),  # Underline
            (r'\*([\w\s]+)\*', r'\033[3m\1\033[0m'),  # Italics
            (r'-\s+([\w\s]+)', r'\033[1;32m• \1\033[0m'),  # List items
            (r'```', r'\033[1;30m'),  # Code blocks start
            (r'```(.+?)```', r'\033[1;30m\1\033[0m')  # Code blocks content
        ]

        in_code_block = False
        formatted_lines = []

        for line in text.split('\n'):
            if in_code_block:
                if "```" in line:
                    in_code_block = False
                    line = line + '\033[0m'
                else:
                    line = re.sub(r'\*\*|__|\*|_', '', line)
            else:
                for pattern, replace in patterns:
                    line = re.sub(pattern, replace, line)
                if "```" in line:
                    in_code_block = True

            formatted_lines.append(line)

        return '\n'.join(formatted_lines)
