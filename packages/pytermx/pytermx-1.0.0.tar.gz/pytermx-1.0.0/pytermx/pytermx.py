"""
made by seka / @sekateur
discord: @sekateur
cat <3
"""
import sys
import time
import ctypes
from random import choice
from os import system as sysc, name, get_terminal_size as term_size

Windows = name == "nt"

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]

class Color:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\033[90m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_PURPLE = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    RESET = "\033[0m"

    def __str__(self):
        sysc("")

class Utils:
    @staticmethod
    def set_title(title: str):
        sysc(f"title {title}" if Windows else "")

    @staticmethod
    def clear():
        sysc(f"cls" if Windows else "clear")

    @staticmethod
    def hide_cursor():
        if Windows:
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif name == 'posix':
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    @staticmethod
    def show_cursor():
        if name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif name == 'posix':
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

    @staticmethod
    def typing(text: str, interval: bool = 0.05):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(interval)
        return ""
    
class Center:
    @staticmethod
    def center(text):
        return Center.center_x(Center.center_y(text))

    @staticmethod
    def center_x(text):
        terminal_width = term_size().columns
        return "\n".join(line.center(terminal_width) for line in text.splitlines())
    
    @staticmethod
    def center_y(text):
        terminal_height = term_size().lines
        lines = text.splitlines()
        num_lines = len(lines)
        if num_lines >= terminal_height:
            return text
        top_padding = (terminal_height - num_lines) // 2
        bottom_padding = terminal_height - num_lines - top_padding
        return "\n".join(" " * term_size().lines for _ in range(top_padding)) + text + "\n".join(" " * term_size().lines for _ in range(bottom_padding))
    
class Fade:
    @staticmethod
    def in_blue(text: str, red: int, green: int):
        faded = ""
        blue = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};{green};{blue}m{line}{Color.RESET}")
            if not blue == 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    @staticmethod
    def in_red(text: str, green: int, blue: int):
        faded = ""
        red = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};{green};{blue}m{line}{Color.RESET}")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded

    @staticmethod
    def in_green(text: str, red: int, blue: int):
        faded = ""
        green = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};{green};{blue}m{line}\n{Color.RESET}")
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded
    
class Anim:
    def show_n_hide(banner: str, repeat: int = 10):
        colors = [Color.BLACK, Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE,
                  Color.PURPLE, Color.CYAN, Color.WHITE, Color.GREY, Color.BRIGHT_RED, Color.BRIGHT_GREEN,
                  Color.BRIGHT_YELLOW, Color.BRIGHT_BLUE, Color.BRIGHT_PURPLE,
                  Color.BRIGHT_CYAN, Color.BRIGHT_WHITE]

        for _ in range(repeat):
            chosen_color = choice(colors)
            centered_banner = Utils.center_y(Utils.center(f"{chosen_color}{banner}"))
            Utils.clear()
            time.sleep(0.05)
            print(centered_banner)
            time.sleep(0.05)
        print(Color.RESET)