import os
import sys
import time
import nmap
import socket
import dns.resolver
import dns.reversename
from pythonping import ping
from contextlib import closing
from PyUtil.IcsVendors import *

# Util: https://pypi.org/project/python-nmap/


class IcsScanner:
    def __init__(self, IpOrHostname):
        self.__IP_Addrr = None
        self.__Hostname = None
        # Store ping
        self.__PingMeasured = False
        self.__Ping = {'response': False, 'latency': '-1ms'}
        # nMap handler
        self.__nm = nmap.PortScanner()
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
                raise ValueError("Invalid ip or host provided: '%s'" % IpOrHostname)

    def GetHostname(self):
        return self.__Hostname

    def GetIpAddress(self):
        return self.__IP_Addr

    def GetOpenTcpPorts(self):
        ports = GetAllIcsPortsList()['tcp']
        ports_str = (','.join([str(i) for i in ports]))
        self.__nm.scan(str(self.__IP_Addr), 'T:' + str(ports_str), arguments="")
        open_ports = []
        for port in ports:
            if (self.__nm.has_host(self.__IP_Addr)) and ("tcp" in self.__nm[self.__IP_Addr]) and (port in self.__nm[self.__IP_Addr]['tcp']) and (self.__nm[self.__IP_Addr]['tcp'][port]['state'] == "open"):
                open_ports.append(port)
        return open_ports

    def GetOpenUdpPorts(self):
        ports = GetAllIcsPortsList()['udp']
        ports_str = (','.join([str(i) for i in ports]))
        self.__nm.scan(str(self.__IP_Addr), 'U:' + str(ports_str))
        ports = []
        for port in ports:
            if (self.__nm.has_host(self.__IP_Addr)) and ("tcp" in self.__nm[self.__IP_Addr]) and (port in self.__nm[self.__IP_Addr]['tcp']) and (self.__nm[self.__IP_Addr]['tcp'][port]['state'] == "open"):
                ports.append(port)
        return ports

    def Ping(self, MesureAgain=False):
        # Do not measure ping again if not specifically requested
        if MesureAgain is False:
            if self.__PingMeasured:
                return self.__Ping
        # This requires root privileges
        try:
            ping_resp =  ping(self.__IP_Addr, timeout=3,  count=3, size=84)
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

    def IsPortOpen(self, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(2)
            if sock.connect_ex((self.__IP_Addr, port)) == 0:
                return True
            else:
                return False

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


