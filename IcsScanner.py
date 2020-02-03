import os
import sys
import time
import nmap
from pythonping import ping
import socket
import dns.resolver
import dns.reversename
from PyUtil.IcsVendors import *
from PyUtil.Util import *


class IcsScanner:
    def __init__(self, IpOrHostname):
        self.__IP_Addr = None
        self.__Hostname = None
        # Store ping
        self.__PingMeasured = False
        self.__Ping = {'response': False, 'latency': '-1ms'}
        try:
            socket.inet_aton(IpOrHostname)
            # Provided data is a valid IPv4
            self.__IP_Addr = IpOrHostname
            # Resolve IP address to hostname
            self.__Hostname = self.__Ip2Hostname(self.__IP_Addr)
        except socket.error:
            ip = self.__Hostname2Ip(IpOrHostname)
            if ip is not None:
                self.__IP_Addr = ip
            else:
                raise ValueError("Invalid username or host provided: '%s'" % IpOrHostname)

    def GetHostname(self):
        return self.__Hostname

    def GetIpAddress(self):
        return self.__IP_Addr

    def Ping(self, MesureAgain=False):
        # Do not measure ping again if not specifically requested
        if MesureAgain is False:
            if self.__PingMeasured:
                return self.__Ping
        # This requires root privileges
        try:
            ping_resp =  ping(self.__IP_Addr, timeout=3,  count=1)
            if  ping_resp.success():
                self.__Ping['response'] = True
                self.__Ping['latency'] =  str(ping_resp.rtt_avg_ms) + "ms"
            else:
                self.__Ping['response'] = False
                self.__Ping['latency'] = "Not responding"
        except:
            self.__Ping['response'] = False
            self.__Ping['latency'] = 'Unreachable/Error'
        # Set a flag indicating that ping was already measured
        self.__PingMeasured = True
        return self.__Ping

    def __Ip2Hostname(self, ip):
        try:
            # Validate ip address
            socket.inet_aton(ip)
            # DNS Handler
            n = dns.reversename.from_address(ip)
            return str(dns.resolver.query(n, "PTR")[0])
        except:
            return None

    def __Hostname2Ip(self, hostname):
        try:
            # DNS Handler
            res = dns.resolver.Resolver(configure=False)
            # res.nameservers = ['8.8.8.8', '2001:4860:4860::8888', '8.8.4.4', '2001:4860:4860::8844']
            res.timeout = 5
            return res.query(hostname)
        except:
            return None
