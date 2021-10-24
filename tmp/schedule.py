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

from python.fritz_reboot import reboot_repeaters, reboot_box

# reboot day and time:
# weekday, hour, minute, minutes later to reboot repeaters
REBOOT = ("Sunday", 0, 1, 5)

ISO_WEEK_EN = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# noinspection SpellCheckingInspection
ISO_WEEK_DE = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag",
    6: "Samstag",
    7: "Sonntag"
}


def today(day: str, weekday_dic=None):
    if weekday_dic is None:
        weekday_dic = ISO_WEEK_EN
    outcome = False
    try:
        import datetime
        if day in weekday_dic.values():
            outcome = day == weekday_dic.get(
                datetime.datetime.now().isoweekday())
    except (ImportError, TypeError, ValueError):
        outcome = False
    finally:
        return outcome


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
