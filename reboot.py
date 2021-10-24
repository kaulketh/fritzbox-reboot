#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# reboot
# created 24.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import sys
from subprocess import call


class RebootFritzDevice:
    def __init__(self, ip4, password, user=None):
        self.__device = ip4
        self.__usr = "" if user is None else user
        self.__pwd = password
        # noinspection SpellCheckingInspection
        self.__location = "/upnp/control/deviceconfig"
        # noinspection SpellCheckingInspection
        self.__uri = "urn:dslforum-org:service:DeviceConfig:1"
        self.__action = 'Reboot'
        # noinspection SpellCheckingInspection,HttpUrlsUsage
        self.__curl = f"curl -k -m 5 --anyauth " \
                      f"-u \"{self.__usr}:{self.__pwd}\" " \
                      f"http://{self.__device}:49000{self.__location} " \
                      f"-H 'Content-Type: text/xml; charset=\"utf-8\"' " \
                      f"-H \"SoapAction:{self.__uri}#{self.__action}\" " \
                      f"-d \"<?xml version='1.0' encoding='utf-8'?>" \
                      f"<s:Envelope s:encodingStyle=" \
                      f"'http://schemas.xmlsoap.org/soap/encoding/' " \
                      f"xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'>" \
                      f"<s:Body><u:{self.__action} xmlns:u='{self.__uri}'>" \
                      f"</u:{self.__action}></s:Body></s:Envelope>\" " \
                      f"-s > /dev/null"
        self.__return_value = None

        # noinspection PyBroadException
        try:
            self.__execute()
            sys.stdout.write(f"{self.__return_value}\n")
        # TODO: Exception handling
        except Exception:
            pass

    def __execute(self):
        self.__return_value = call(self.__curl, shell=True)


if __name__ == '__main__':
    # RebootFritzDevice(ip4=<IPv4 here>, password=<password>, user=<user name if required>)
    pass
