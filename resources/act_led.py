#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# act_led.py
# created 25.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import os


def led_on():
    """
    Turn on activity LED of Raspberry Pi
    :return:
    """
    on = """
    # exec >> /dev/null
    sudo su <<HERE
    echo default-on > /sys/class/leds/led1/trigger
    HERE
    """
    os.system(on)

def led_off():
    """
    Turn off activity LED of Raspberry Pi
    :return:
    """
    off = """
    # exec >> /dev/null
    sudo su <<HERE
    echo none > /sys/class/leds/led1/trigger
    HERE
    """
    os.system(off)


if __name__ == '__main__':
    pass