#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

import os
import re
import subprocess


class ProxyBrokenList:
    """
    formats proxybroken output to readable form
    [{protocol}: // {ip address}: {port}]
    """

    def __init__(self):
        # path cwd
        self.brokenlist = "pr.txt"
        self.scrapylist = "proxy.txt"

    # start proxybroken
    def create_proxy(self):
        # change your env and command
        code = subprocess.call(
            ["/home/adls/anaconda3/envs/proxybroker/bin/proxybroker",\
             "find", "--types", "HTTP", "HTTPS", "--strict", "-l", "20",\
                 "--show-stats", "--format", "txt", "-o", self.brokenlist]
                                )
        return code

    def read_brokenlist(self):
        brlist = []
        with open(self.brokenlist, 'r') as brfile:
            [brlist.append(string) for string in brfile]
        return brlist

    # get protocol, ip, port
    def parser(self, brlist) -> list:
        ip_port = []
        for row in brlist:
            ip_port.append(re.findall(
          r"(\[(.*?)\]?)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:\:(\d{1,5}))?",
          row)
                                     )
        clearprotocol = self.clear_protocol(ip_port)
        clear80 = self.clear_80(clearprotocol)
        result = self.result_list(clear80)
        return result

    # deleted server on 80 port
    def clear_80(self, ipport):
        proxylist, protocol = [], []
        for port in range(0, len(ipport)):
            try:
                if not ipport[port][2] == '80':
                    protocol.append(ipport[port][0])
                    proxylist.append('%s:%s' % (ipport[port][1],
                                                ipport[port][2]))
            except IndexError:
                pass
        return (list(zip(protocol, proxylist)))

    # return valid string
    def result_list(self, proxylist):
        newlist = []
        for line in proxylist:
            base = line[0].split(' ')
            for n in range(0, len(base)):
                if base[n]:
                    newlist.append(('%s://%s' % (base[n], line[1])))
        return newlist

    def save(self, scrapylist):
        with open(self.scrapylist, 'w+') as sfile:
            print(*scrapylist, file=sfile, sep='\n')
        return True

    def clear_protocol(self, array) -> list:
        protocol, address, port = [], [], []
        for n in range(0, len(array)):
            protocol.append(self.clear_protocol_str(array[n][0][1]).rstrip())
            address.append(array[n][0][2].rstrip())
            port.append(array[n][0][3].rstrip())
        return (list(zip(protocol, address, port)))

    # deleted trush
    def clear_protocol_str(self, string):
        string = string.replace('Anonymous', '').replace('High','')
        string = string.replace('Transparent', '')
        string = string.replace(':', '').replace('  ', '').replace(',', '')
        return string.replace(']', '').lower()

    def deleted(self):
        os.remove(self.brokenlist)
        return (print("Proxy list is create!"))

    def run(self):
        if self.create_proxy() == 0:
            brokenlist = self.read_brokenlist()
        else: print("Error to run proxybroken")
        text = self.parser(brokenlist)
        self.save(text)
        self.deleted()
        return True

if __name__ == '__main__':
    ProxyBrokenList().run()

