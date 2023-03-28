# logo.py - configuration for login.py
from colordef import FG_Colors, BG_Colors

class Config:
    logo = "\
       .__                      .__           .__       .___             \n\
______ |  | _____    ____  ____ |  |__   ____ |  |    __| _/___________  \n\
\____ \|  | \__  \ _/ ___\/ __ \|  |  \ /  _ \|  |   / __ |/ __ \_  __ \ \n\
|  |_> >  |__/ __ \\  \__\  ___/|   Y  (  <_> )  |__/ /_/ \  ___/|  | \/ \n\
|   __/|____(____  /\___  >___  >___|  /\____/|____/\____ |\___  >__|    \n\
|__|             \/     \/    \/     \/                  \/    \/       "

    logo_color_fg = FG_Colors.Cyan
    logo_color_bg = None

    important = True
    message = "Access to this system is for authorized persons only. \n\
Unauthorized use or access is regarded as a criminal act is subject to civil and criminal prosecution."

    key_color_fg = FG_Colors.White
    key_color_bg = None

    value_color_fg = FG_Colors.Magenta
    value_color_bg = None