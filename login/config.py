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

    def display():
        # Create Login object and clear screen
        login = Login()
        login.clear()

        # Main display configuration

        # --- Logo ---
        login.logo(Config.logo, Config.l_color)

        # --- Connected to (Hostname / SSH_CLIENT) ---
        login.connected_to(Config.k_color, Config.v_color)

        # --- System Information ---
        login.system(Config.k_color, Config.v_color)

        # --- Current Time ---
        login.current_time(Config.k_color, Config.v_color)

        # --- Message ---
        login.message(Config.message, Config.v_color, Config.important)