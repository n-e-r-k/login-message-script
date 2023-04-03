#!/bin/zsh

echo "Copying /login to /Users/$USER/.login"

cp -r ./login /Users/$USER/.login

echo "Adding `python3 /Users/$USER/.login/launch.py` to zshrc"

echo "python3 /Users/$USER/.login/launch.py" >> /Users/$USER/.zshrc

echo "Finished install, edit /Users/$USER/.login/config.py to change configuration for LMS."