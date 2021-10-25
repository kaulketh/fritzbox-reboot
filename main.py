#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# main
# created 25.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import time

from resources import RebootFritzDevice, \
    BOX_IP, BOX_USER_PW, BOX_USER, \
    REP_IP_1, REP_IP_2, REP_PW, \
    every, DAY, MINUTE


def reboot_box():
    RebootFritzDevice(BOX_IP, BOX_USER_PW, BOX_USER)


def reboot_repeaters():
    RebootFritzDevice(REP_IP_1, REP_PW)
    RebootFritzDevice(REP_IP_2, REP_PW)


def restart_all():
    reboot_box()
    time.sleep(5 * MINUTE)
    reboot_repeaters()


if __name__ == '__main__':
    every(DAY, restart_all())
    pass
