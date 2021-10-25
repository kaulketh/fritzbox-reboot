#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# schedule.py
# created 25.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# ----------------------------------------------------------

import datetime
import time
import traceback
from threading import Event, Thread

# duration constants in seconds
SECOND = 1
MINUTE = 60
HOUR = 3_600
DAY = 216_000
WEEK = 1_512_000

# week days
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
        if day in weekday_dic.values():
            outcome = day == weekday_dic.get(
                datetime.datetime.now().isoweekday())
    except (ImportError, TypeError, ValueError):
        outcome = False
    finally:
        return outcome


def call_repeatedly(interval, func, *args):
    """
    https://stackoverflow.com/questions/22498038/improve-current-implementation-of-a-setinterval/22498708#22498708
    """
    stopped = Event()

    def loop():
        while not stopped.wait(
                interval):  # the first call is in `interval` secs
            func(*args)

    Thread(target=loop).start()
    return stopped.set


def every(interval, func, *args):
    """
    https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds/25251804#25251804
    """

    next_time = time.time() + interval

    while True:
        time.sleep(max(0, next_time - time.time()))
        # noinspection PyBroadException
        # TODO: Exception handling properly
        try:
            func(*args)
        except Exception:
            traceback.print_exc()
            # in production code you might want to have this instead of course:
            # logger.exception("Problem while executing repetitive task.")
        # skip tasks if we are behind schedule:
        next_time += (time.time() - next_time) \
                     // interval * interval + interval


def set_interval(interval):
    """
    Interval decorator
    https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            stopped = Event()

            def loop():  # executed in another thread
                while not stopped.wait(interval):  # until stopped
                    func(*args, **kwargs)

            t = Thread(target=loop)
            t.daemon = True  # stop if the program exits
            t.start()
            return stopped

        return wrapper

    return decorator


if __name__ == '__main__':
    pass
