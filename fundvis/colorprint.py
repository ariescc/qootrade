'''
涂色模块
'''
from colorama import init, Fore

init(autoreset=True)
class Colored(object):
    # 前景色：红色 背景色：默认
    def red(self, s):
        return Fore.LIGHTRED_EX + s + Fore.RESET
    def green(self, s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET
    def yellow(self, s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET
    def white(self, s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET
    def blue(self, s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET
