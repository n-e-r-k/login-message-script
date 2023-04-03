#!/bin/bash

echo "Copying /login to /home/$USER/.login"

cp -r ./login /home/$USER/.login

echo "Adding `python3 /home/$USER/.login/launch.py` to bash"

echo "python3 /home/$USER/.login/launch.py" >> /home/$USER/.bashrc

echo "Finished install, edit /home/$USER/.login/config.py to change configuration for LMS."