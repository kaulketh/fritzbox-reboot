#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# fritz_reboot
# created 23.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import os

from python.secret import BOX_IP, BOX_USER, BOX_USER_PW, REP_IP_1, \
    REP_PW, REP_IP_2

LOCATION = "/upnp/control/deviceconfig"
URI = "urn:dslforum-org:service:DeviceConfig:1"
ACTION = 'Reboot'


# noinspection HttpUrlsUsage
def __execute_curl(ip, user, pw):
    curl = f"curl -k -m 5 --anyauth -u \"{user}:{pw}\" http://{ip}:49000{LOCATION} -H 'Content-Type: text/xml; charset=\"utf-8\"' -H \"SoapAction:{URI}#{ACTION}\" -d \"<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:{ACTION} xmlns:u='{URI}'></u:{ACTION}></s:Body></s:Envelope>\" -s > /dev/null"
    os.system(curl)


def __reboot(ip, pwd, user=None):
    usr = "" if user is None else user
    __execute_curl(ip, usr, pwd)


def reboot_box():
    __reboot(BOX_IP, BOX_USER_PW, BOX_USER)


def reboot_repeaters():
    __reboot(REP_IP_1, REP_PW)
    __reboot(REP_IP_2, REP_PW)


if __name__ == '__main__':
    reboot_box()
