#
# Industrial devices vendors ports
#

import sys


class ICS:
    def __init__(self, DeviceType="", DeviceName="", VendorName="", Description ="", TcpPorts=None, UdpPorts=None, Dorks=None):
        self.DeviceType = DeviceType
        self.DeviceName = DeviceName
        self.VendorName = VendorName
        self.Description = Description
        self.TcpPorts = TcpPorts
        self.UdpPorts = UdpPorts
        self.Dorks = Dorks
        if Dorks is None:
            Dorks = []
        if UdpPorts is None:
            UdpPorts = []
        if TcpPorts is None:
            TcpPorts = []


ICS_List = [
    ICS(DeviceType="PLC", DeviceName="All New Rockwell PLC’s", VendorName="Allen Bradley", TcpPorts={44818}, UdpPorts={}, Dorks={"port:44818"}, Description="Allen Bradley – All newer Rockwell PLC’s : 44818"),
    ICS(DeviceType="PLC", DeviceName="AB PLC5E or SLC5/05", VendorName="Allen Bradley", TcpPorts={2222}, UdpPorts={}, Dorks={"port:2222"}, Description="Allen Bradley –  Older Rockwell AB PLC5E and SLC5/05"),
    ICS(DeviceType="Embedded PC", DeviceName="AB PLC5E or SLC5/05", VendorName="BECKHOFF", TcpPorts={48898}, UdpPorts={}, Dorks={"port:48898"}, Description="BECKHOFF Embedded PC: 48898"),
    ICS(DeviceType="PLC", DeviceName="ECL Apex", VendorName="Danfoss", TcpPorts={5050}, UdpPorts={}, Dorks={"port:5050"}, Description="Danfoss ECL Apex: 5050"),
    ICS(DeviceType="PLC", DeviceName="FBs-PLC", VendorName="FATEK", TcpPorts={500}, UdpPorts={}, Dorks={"port:500"}, Description="FATEK FB Series: 500"),

    ICS(DeviceType="", DeviceName="", VendorName="", TcpPorts={}, UdpPorts={}, Dorks={"port:"}, Description=""),
]


def PrintIcsList(ICS_List = None):
    ics = ICS()
    i = 0
    for tmpIcs in ICS_List:
        ics = tmpIcs
        i += 1
        print("{}. {}".format(i, ics.Description))
