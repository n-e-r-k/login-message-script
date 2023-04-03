# login-message-script
A customizable python script used to display login information.

## Current features:
- Configured to display ASCII logo
- Customizable login message
- Assignable foreground and background colors for both key and value
- Informs the user the $SSH_CLIENT if applicable
- Customizable display() function to enable/disable different modules and change their location.
- Eeasily expandable using python.

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

This generates an output (localhost/127.0.0.1 does not show as ssh connection, used as example):
<img width="730" alt="Screenshot 2023-03-29 at 6 07 32 PM" src="https://user-images.githubusercontent.com/101080594/228687737-b4652162-736e-41ce-b3b2-5bdb92e4c965.png">

## Current roadmap:
Check the TODO.md to see the current progress on development.
