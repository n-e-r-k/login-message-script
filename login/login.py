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

    def logo():
        self.print_color(Config.logo, Config.l_color)
        return
    
    def connected_to():
        self.print_color("Connected to: ", Config.k_color, False)
        if self.client != "localhost":
            self.print_color(self.os[1], Config.v_color, False)
            self.print_color(" through ", Config.k_color, False)
            self.print_color(self.client, Config.v_color, True)
        else:
            self.print_color(self.os[1], Config.v_color, True)
        return

    def system():
        self.print_color("System: ", Config.k_color, False)
        self.print_color(self.os[2] + " " + self.os[4], Config.v_color, True)
        return

    def current_time():
        self.print_color("Current time: ", Config.k_color, False)
        self.print_color(self.time, Config.v_color, True)
        return
    
    def message():
        if Config.important == True:
            self.print_color("*IMPORTANT*", (FG_Colors.Red, None))
        self.print_color(Config.message, Config.v_color, True)
        return

    def print_color(self, text, color = None, newline = True):
        if fg_color != None:
            print(color[0].value, end="")
        if bg_color != None:
            print(color[1].value, end="")
        
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
    Config.display()