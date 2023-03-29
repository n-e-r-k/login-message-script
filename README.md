# login-message-script
A customizable python script used to display login information.

## Current features:
- Configured to display ASCII logo
- Customizable login message
- Assignable foreground and background colors for both key and value
- Informs the user the $SSH_CLIENT if applicable
- Customizable display() function to enable/disable different modules and change their location.

## Usage:
Enabled by adding a command to the end of your .bashrc, .zshrc, etc...
`python3 /home/$USER/.login/launch.py`

When installed, use of the config.py to change options. Here is an example of the current config.py:
```python
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
```

This generates an output(Color not shown):
```ASCII
[2J[36m       .__                      .__           .__       .___             
______ |  | _____    ____  ____ |  |__   ____ |  |    __| _/___________  
\____ \|  | \__  \ _/ ___\/ __ \|  |  \ /  _ \|  |   / __ |/ __ \_  __ \ 
|  |_> >  |__/ __ \  \__\  ___/|   Y  (  <_> )  |__/ /_/ \  ___/|  | \/ 
|   __/|____(____  /\___  >___  >___|  /\____/|____/\____ |\___  >__|    
|__|             \/     \/    \/     \/                  \/    \/       
[0m[0m[37mConnected to: [0m[0m[35mlocalhost [0m[0m[37m through [0m[0m[35m 127.0.0.1
[0m[0m[37mSystem: [0m[0m[35m22.2.0 arm64
[0m[0m[37mCurrent time: [0m[0m[35mWed, 29 Mar 2023 22:59:08
[0m[0m[31m*IMPORTANT*
[0m[0m[35mAccess to this system is for authorized persons only. 
Unauthorized use or access is regarded as a criminal act is subject to civil and criminal prosecution.
[0m[0m
```

## Current roadmap:
Check the TODO.md to see the current progress on development.
