#!/bin/bash

sudo port install postgresql84-server
sudo port install py26-virtualenvwrapper

cp venv-work $HOME/.venv-work
cp git-completion.bash $HOME/.git-completion.bash

# Add workflow script to user's .bash_profile
echo -ne "\nsource ~/.venv-work" >> ~/.bash_profile
