#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# fritzbox_reboot
# created 23.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import os

NO_USER = ""
LOCATION = "/upnp/control/deviceconfig"
URI = "urn:dslforum-org:service:DeviceConfig:1"
ACTION = 'Reboot'


# noinspection HttpUrlsUsage
def execute_curl(ip, user, pw):
    curl = f"curl -k -m 5 --anyauth -u \"{user}:{pw}\" http://{ip}:49000{LOCATION} -H 'Content-Type: text/xml; charset=\"utf-8\"' -H \"SoapAction:{URI}#{ACTION}\" -d \"<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:{ACTION} xmlns:u='{URI}'></u:{ACTION}></s:Body></s:Envelope>\" -s > /dev/null"
    os.system(curl)


if __name__ == '__main__':
    pass
