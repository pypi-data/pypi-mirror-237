#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sudipta Sarkar"
__credits__ = ["Sudipta Sarkar"]
__Lisence__ = "BSD"
__maintainer__ = "Sudipta Sarkar"
__email__ = "sarkar.sudipta1976@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

# Default python packages
import logging
import os
import time

# pip installed python packages
# from pynput.keyboard import Key, Controller


class WorkLogin:
    """Class that performs functions for login"""

    def __init__(self, name):
        """Saves config file location"""

        self.name = name

    def login(self):
        """logging the name"""

        # Configures config file if not done so already
        logging.warning("name is => %s", self.name)
        #     self.configure()
        # # Opens a terminal
        # os.system("gnome-terminal")
        # time.sleep(1)
        # with open(self.conf_path, "r") as f:
        #     for cmd in f:
        #         self._run_cmd(cmd)

    # def configure(self):
    #     """Configures file that will contain commands to run"""
    #
    #     logging.info("Configuring work login")
    #     cmds = [input("Next command, or hit enter:\n")]
    #     # Ugh needs 3.6 compatibility, but with 3.8 could use walrus here
    #     while cmds[-1] != "":
    #         cmds.append(input("Next command, or hit enter:\n"))
    #     with open(self.conf_path, "w+") as f:
    #         f.write("\n".join(cmds))
    #
    # def _run_cmd(self, cmd):
    #     """Runs a command slowly so as not to error"""
    #
    #     new_cmd = cmd.replace("\n", "")
    #     for c in new_cmd:
    #         self._type_key(c)
    #     self._type_key(Key.enter)
    #     time.sleep(.1)
    #
    # def _type_key(self, key):
    #     """Types a key with a delay"""
    #
    #     self.keyboard.press(key)
    #     time.sleep(.005)
    #     self.keyboard.release(key)
    #     time.sleep(.005)

# if __name__ == "__main__":
#     WorkLogin("Titli").login()
