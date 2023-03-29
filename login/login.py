# login.py library - Nerk Cypher

# --- lib import ---
import os
import re
import time

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

    def set_color(self, key_or_value, color):
        if key_or_value == "k":
            self.k_value == color
        elif key_or_value == "v":
            self.v_color == color
        else:
            print("ERR: Cannot set color, key_or_value flag incorrectly set")
            exit()
        return

    def logo(self, logo_text, l_color):
        self.print_color(logo_text, l_color)
        return
    
    def connected_to(self, k_color, v_color):
        self.print_color("Connected to: ", k_color, False)
        if self.client != "localhost":
            self.print_color(self.os[1], v_color, False)
            self.print_color(" through ", k_color, False)
            self.print_color(self.client, v_color, True)
        else:
            self.print_color(self.os[1], v_color, True)
        return

    def system(self, k_color, v_color):
        self.print_color("System: ", k_color, False)
        self.print_color(self.os[2] + " " + self.os[4], v_color, True)
        return

    def current_time(self, k_color, v_color):
        self.print_color("Current time: ", k_color, False)
        self.print_color(self.time, v_color, True)
        return
    
    def message(self, message, v_color, important = True):
        if important == True:
            self.print_color("*IMPORTANT*", (FG_Colors.Red, None))
        self.print_color(message, v_color, True)
        return

    def print_color(self, text, color = None, newline = True):
        if color[0] != None:
            print(color[0].value, end="")
        if color[1] != None:
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