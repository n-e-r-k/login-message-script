#!/bin/zsh

echo "Copying /login to /home/$USER/.login"

cp -r ./login /home/$USER/.login

echo "Adding `python3 /home/$USER/.login/launch.py` to zshrc"

echo "python3 /home/$USER/.login/launch.py" >> /home/$USER/.zshrc

echo "Finished install, edit /home/$USER/.login/config.py to change configuration for LMS."