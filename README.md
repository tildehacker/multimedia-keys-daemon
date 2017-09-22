# multimedia-keys-daemon
A gnome-settings-daemon alternative for handling multimedia keys events for standalone window managers.

## Motivation
This is the solution for multimedia keys in i3wm: https://faq.i3wm.org/question/3747/enabling-multimedia-keys.1.html. A new process is spawning everytime you press a multimedia keys. This solution aims to have only one daemon process to handle all multimedia keys events.

## Installation
This script is still a work in progress. This is a quick guide on how to get this script working on your machine. This should work on any Debian based Linux distro.

First install python3, python3-pip and libasound2-dev using apt:
```bash
sudo apt install python3 python3-pip libasound2-dev
```

Then install the three required python packages:
```bash
sudo pip3 install python-daemon pynput pyalsaaudio
```

## Start the daemon
```bash
sudo ./__main__.py
```

## Kill the daemon
Use `ps aux | grep __main__` and `sudo kill` to kill the daemon.
