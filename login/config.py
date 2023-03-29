# logo.py - configuration for login.py
from colordef import FG_Colors, BG_Colors
from login import Login

class Config:
    # Logo String
    logo = "\
       .__                      .__           .__       .___             \n\
______ |  | _____    ____  ____ |  |__   ____ |  |    __| _/___________  \n\
\____ \|  | \__  \ _/ ___\/ __ \|  |  \ /  _ \|  |   / __ |/ __ \_  __ \ \n\
|  |_> >  |__/ __ \\  \__\  ___/|   Y  (  <_> )  |__/ /_/ \  ___/|  | \/ \n\
|   __/|____(____  /\___  >___  >___|  /\____/|____/\____ |\___  >__|    \n\
|__|             \/     \/    \/     \/                  \/    \/       "

    # Logo Color (foreground, background)
    l_color = (FG_Colors.Cyan, None)

    # Key Color (foreground, background)
    k_color = (FG_Colors.White, None)

    # Value Color (foreground, background)
    v_color = (FG_Colors.Magenta, None)

    # Add important flag before message
    important = True
    # Message string
    message = "Access to this system is for authorized persons only. \n\
Unauthorized use or access is regarded as a criminal act is subject to civil and criminal prosecution."

    # Display configuration
    def display():
        # Create Login object and clear screen
        login = Login()
        login.clear()

        # Main display configuration
        login.logo()

        login.connected_to()

        login.system()

        login.current_time()
        
        login.message()