#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# schedule
# created 23.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import datetime
import time


# TODO: dirty date check
def check_loop(day_check=3_600, time_check=600):
    rebooted = False
    while True:
        if today(REBOOT[0]) and not rebooted:
            now = datetime.datetime.now()
            if REBOOT[1] == now.hour and REBOOT[2] == now.minute:
                print("reboot router")
                reboot_box()
                time.sleep(REBOOT[3] * 60)
                print("reboot repeaters")
                reboot_repeaters()
                rebooted = True
            else:
                print("week day reached, wait for time")
                time.sleep(time_check)
                rebooted = False
            continue
        print("wrong week day!")
        time.sleep(day_check)


if __name__ == '__main__':
    check_loop(60, 10)
