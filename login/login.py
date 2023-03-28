# login.py - Nerk Cypher

# --- lib import ---
import os
import re
import time

from config import Config
from colordef import FG_Colors, BG_Colors

class Login:
    def __init__(self):
        self.os = os.uname()
        # five tuple with system information:
        #   - [0]sysname (i.e. linux)
        #   - [1]nodename (i.e. hostname)
        #   - [2]release (i.e. x.x.x-arch1-1)
        #   - [3]version 
        #   - [4]machine (i.e. x86_64)

        parse_client = os.getenv("SSH_CLIENT")
        if parse_client != None:
            parse_client = re.search("^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", parse_client)
            self.client = parse_client.group()
        else:
            self.client = "localhost"
        # Currently Connected SSH client. (i.e. 127.0.0.1)
        # if no SSH client, assume connection from local host.

        self.time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())



    def display(self, key_color_fg, value_color_fg, key_color_bg = None, value_color_bg = None):
        # --- Logo ---
        self.print_color(Config.logo, Config.logo_color_fg, Config.logo_color_bg)

        # --- Connected to ---
        self.print_color("Connected to: ", key_color_fg, key_color_bg, False)
        if self.client != "localhost":
            self.print_color(self.os[1], value_color_fg, value_color_bg, False)
            self.print_color(" through ", key_color_fg, key_color_bg, False)
            self.print_color(self.client, value_color_fg, value_color_bg, True)
        else:
            self.print_color(self.os[1], value_color_fg, value_color_bg, True)

        # --- System ---
        
        self.print_color("System: ", key_color_fg, key_color_bg, False)
        self.print_color(self.os[2] + " " + self.os[4], value_color_fg, value_color_bg, True)

        # --- Current time ---
        self.print_color("Current time: ", key_color_fg, key_color_bg, False)
        self.print_color(self.time, value_color_fg, value_color_bg, True)

        # --- Message ---
        
        if Config.important == True:
            self.print_color("*IMPORTANT*", FG_Colors.Red, None)
        self.print_color(Config.message, value_color_fg, value_color_bg, True)
        
        return



    def print_color(self, text, fg_color = None, bg_color = None, newline = True):
        if fg_color != None:
            print(fg_color.value, end="")
        if bg_color != None:
            print(bg_color.value, end="")
        
        if newline != False:
            print(text)
        else:
            print(text, end="")
        
        print(FG_Colors.Reset.value, end="")
        print(BG_Colors.Reset.value, end="")
        return
        
            

    def clear(self):
        print("\x1B[2J", end="")
        return



    def refresh(self):
        self.__init__
        return
    


# --- Main ---

if __name__ == "__main__":
    login = Login()

    login.clear()
    login.display(Config.key_color_fg, Config.value_color_fg, Config.key_color_bg, Config.value_color_bg)