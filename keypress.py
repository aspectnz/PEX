#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pygame
from pygame.locals import *
import pip
try:
    from evdev import InputDevice, categorize, ecodes, list_devices
except:
    pip.main(['install','evdev'])
    from evdev import InputDevice, categorize, ecodes, list_devices


pygame.init()
pygame.mixer.init()


def toggle_sound():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load("/home/pi/Desktop/song.mp3")
        pygame.mixer.music.play()


def get_button():
    devices = [InputDevice(fn) for fn in list_devices()]
    buttons = filter(lambda d: d.name == 'Cleware GmbH USB-Keys', devices)
    if buttons:
        button = buttons[0]
        return button
    else:
        return None


dev = get_button()

while True:
    time.sleep(0.25)
    if not dev:
        dev = get_button()
    if dev:
        try:
            event = dev.read_one()
            while event:
                if event.type == ecodes.EV_KEY:
                    c = categorize(event)
                    # print c.keycode, c.keystate, c.scancode
                    if c.keycode == "KEY_1" and c.keystate > 0:
                        toggle_sound()
                event = dev.read_one()
        except IOError:
            dev = None