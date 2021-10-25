#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# reboot
# created 24.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import traceback
from subprocess import call


class RebootFritzDevice:
    def __init__(self, ip4, password, user=None):
        self.__ip4 = ip4
        self.__usr = "" if user is None else user
        self.__pwd = password

        self.__return_value = None

        # noinspection SpellCheckingInspection,HttpUrlsUsage
        self.__curl = f"curl -k -m 5 --anyauth " \
                      f"-u \"{self.__usr}:{self.__pwd}\" " \
                      f"http://{self.__ip4}:49000/upnp/control/deviceconfig " \
                      f"-H 'Content-Type: text/xml; charset=\"utf-8\"' " \
                      f"-H \"SoapAction:" \
                      f"urn:dslforum-org:service:DeviceConfig:1#Reboot\" " \
                      f"-d \"<?xml version='1.0' encoding='utf-8'?>" \
                      f"<s:Envelope s:encodingStyle=" \
                      f"'http://schemas.xmlsoap.org/soap/encoding/' " \
                      f"xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'>" \
                      f"<s:Body><u:Reboot xmlns:" \
                      f"u='urn:dslforum-org:service:DeviceConfig:1'>" \
                      f"</u:Reboot></s:Body></s:Envelope>\" " \
                      f"-s > /dev/null"

        # noinspection PyBroadException
        # TODO: Exception handling properly
        try:
            self.__return_value = call(self.__curl, shell=True)
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    pass
