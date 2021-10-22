#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# fritzbox_reboot
# created 23.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import os

from secret import BOX_IP, REP_IP_1, REP_IP_2, BOX_USER, BOX_USER_PW, REP_PW

NO_USER = ""
LOCATION = "/upnp/control/deviceconfig"
URI = "urn:dslforum-org:service:DeviceConfig:1"
ACTION = 'Reboot'


# noinspection HttpUrlsUsage
def _execute_curl(ip, user, pw):
    curl = f"curl -k -m 5 --anyauth -u \"{user}:{pw}\" http://{ip}:49000{LOCATION} -H 'Content-Type: text/xml; charset=\"utf-8\"' -H \"SoapAction:{URI}#{ACTION}\" -d \"<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:{ACTION} xmlns:u='{URI}'></u:{ACTION}></s:Body></s:Envelope>\" -s > /dev/null"
    os.system(curl)


if __name__ == '__main__':
    #_execute_curl(BOX_IP, BOX_USER, BOX_USER_PW)
    #_execute_curl(REP_IP_1, NO_USER, REP_PW)
    _execute_curl(REP_IP_2, NO_USER, REP_PW)
