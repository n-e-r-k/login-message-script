# login-message-script
A customizable python script used to display login information.

## Usage:
Enabled by adding a command to the end of your .bashrc, .zshrc, etc...
`python3 /home/$USER/.login/login.py`

When installed, use of the config.py to change options. Here is an example of the current config.py:
```python
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
```

This generates an output(Color not shown):
```bash

       .__                      .__           .__       .___             
______ |  | _____    ____  ____ |  |__   ____ |  |    __| _/___________  
\____ \|  | \__  \ _/ ___\/ __ \|  |  \ /  _ \|  |   / __ |/ __ \_  __ \ 
|  |_> >  |__/ __ \  \__\  ___/|   Y  (  <_> )  |__/ /_/ \  ___/|  | \/ 
|   __/|____(____  /\___  >___  >___|  /\____/|____/\____ |\___  >__|    
|__|             \/     \/    \/     \/                  \/    \/       
Connected to: hostname
System: 22.2.0 arm64
Current time: Tue, 28 Mar 2023 05:01:00
*IMPORTANT*
Access to this system is for authorized persons only. 
Unauthorized use or access is regarded as a criminal act is subject to civil and criminal prosecution.
```

Check the TODO.md to see the current progress on development.
