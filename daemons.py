#!/usr/bin/env python3
# *-* encoding: utf-8 *-*

import sys
import time
import logging

import pynput
from pynput.keyboard import Key, Listener
import alsaaudio


def backlight(op):
    # Get actual brightness
    with open(("/sys/class/backlight/"
               + "intel_backlight/brightness"), 'r') as actual_f:
        actual_b = int(actual_f.readline().rstrip())

    # Calculate new brightness
    if op == 'up':
        new_b = actual_b + step
        if new_b > max_b:
            new_b = max_b
    elif op == 'down':
        new_b = actual_b - step
        if new_b < 0:
            new_b = 0
    else:
        raise ValueError("op should be either 'up' or 'down'.")

    # Set new brightness
    with open(("/sys/class/backlight/"
               + "intel_backlight/brightness"), 'w') as actual_f:
        actual_f.write(str(new_b))

def sound(op):
    m = alsaaudio.Mixer()
    if op == 'toggle':
        if int(False) in m.getmute():
            m.setmute(int(True))
        else:
            m.setmute(int(False))
    else:
        for channel, volume in enumerate(m.getvolume()):
            current_v = int(volume)
            if op == 'up':
                m.setmute(int(False), channel)
                new_v = current_v + 5
            elif op == 'down':
                new_v = current_v - 5
            else:
                raise ValueError("op should be either 'up', 'down' or 'toggle'.")

            try:
                m.setvolume(new_v, channel)
            except alsaaudio.ALSAAudioError:
                if new_v < 0:
                    m.setvolume(0, channel)
                elif new_v > 100:
                    m.setvolume(100, channel)
                else:
                    raise ValueError("new_v is not a valid integer.")

def on_press(key):
    try:
        if key.vk == 269025041:
            sound('down')
        elif key.vk == 269025042:
            sound('toggle')
        elif key.vk == 269025043:
            sound('up')
        elif key.vk == 269025026:
            backlight('up')
        elif key.vk == 269025027:
            backlight('down')
    except AttributeError:
        pass
    except ValueError:
        pass

# Get maximum brightness
with open(("/sys/class/backlight/"
           + "intel_backlight/max_brightness"), 'r') as max_f:
    max_b = int(max_f.readline().rstrip())

# Calculate step
step = int(max_b / 100)

def run():
    logging.basicConfig(level=logging.DEBUG)

    # Create listener thread
    listener = Listener(on_press=on_press)

    # Start listener
    listener.start()

    # Wait for listener to stop
    listener.join()
