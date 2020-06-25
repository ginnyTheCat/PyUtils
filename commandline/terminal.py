import platform
import sys
from subprocess import Popen


def start_new_terminal(cmd):
    terminal_cmd = ""
    if platform.system() == "Windows":
        terminal_cmd = ["cmd.exe", "/c", "start"]
    Popen(terminal_cmd + cmd)


def start_python_script(script):
    start_new_terminal([sys.executable, script])
