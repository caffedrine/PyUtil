#
# Industrial devices vendors ports
#

import sys


class ICS:
    def __init__(self, DeviceType="", DeviceName="", VendorName="", Description="", TcpPorts=None, UdpPorts=None, Dorks=None):
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
    # ICS(DeviceType="PLC", DeviceName="Older Rockwell PLC's", VendorName="Allen Bradley", TcpPorts={2222}, UdpPorts={}, Dorks={"port:2222"}, Description="Allen Bradley –  Older Rockwell AB PLC5E and SLC5/05"),
    ICS(DeviceType="Embedded PC", DeviceName="AB PLC5E or SLC5/05", VendorName="BECKHOFF", TcpPorts={48898}, UdpPorts={}, Dorks={"port:48898"}, Description="BECKHOFF Embedded PC: 48898"),
    ICS(DeviceType="PLC",     DeviceName="ECL Apex", VendorName="Danfoss", TcpPorts={5050}, UdpPorts={}, Dorks={"port:5050"}, Description="Danfoss ECL Apex: 5050"),
    ICS(DeviceType="Generic", DeviceName="QuickPanels", VendorName="GE", TcpPorts={}, UdpPorts={}, Dorks={"port:57176"}, Description="GE - QuickPanels on port 57176"),
    ICS(DeviceType="Generic", DeviceName="EHV Series", VendorName="HITACHI", TcpPorts={}, UdpPorts={}, Dorks={"port:3004"}, Description="HITACHI - EHV Series on port 3004"),
    ICS(DeviceType="Generic", DeviceName="KV-5000", VendorName="KEYENCE", TcpPorts={}, UdpPorts={}, Dorks={"port:8501"}, Description="KEYENCE - KV-5000 on port 8501"),
    ICS(DeviceType="Generic", DeviceName="Koyo Ethernet", VendorName="Koyo", TcpPorts={}, UdpPorts={}, Dorks={"port:28784"}, Description="Koyo - Koyo Ethernet on port 28784"),
    ICS(DeviceType="Generic", DeviceName="FEnet", VendorName="LS GLOFA", TcpPorts={}, UdpPorts={}, Dorks={"port:2004"}, Description="LS GLOFA - FEnet on port 2004"),
    ICS(DeviceType="Generic", DeviceName="Electric car charger", VendorName="kamstrup", TcpPorts={}, UdpPorts={}, Dorks={"port:1025"}, Description="Mitsubishi - FX on port 1025"),
    # ICS(DeviceType="Generic", DeviceName="FX3u Ethernet", VendorName="MITSUBISHI", TcpPorts={}, UdpPorts={}, Dorks={"port:5001"}, Description="MITSUBISHI - FX3u Ethernet on port 5001"),
    ICS(DeviceType="Generic", DeviceName="MR-MQ100 Ethernet", VendorName="MITSUBISHI", TcpPorts={4999, 5002}, UdpPorts={}, Dorks={"port:4999,5002"}, Description="MITSUBISHI - MR-MQ100 Ethernet on port 4999"),
    ICS(DeviceType="Generic", DeviceName="FP Ethernet", VendorName="Panasonic", TcpPorts={8500, 9094}, UdpPorts={}, Dorks={"port:8500,9094"}, Description="Panasonic - FP Ethernet on port 9094"),
    ICS(DeviceType="Generic", DeviceName="HMI", VendorName="Red Lion", TcpPorts={789}, UdpPorts={}, Dorks={"port:789"}, Description="Red Lion - HMI on port 789"),
    ICS(DeviceType="Generic", DeviceName="S-BUS Ethernet", VendorName="SAIA", TcpPorts={}, UdpPorts={}, Dorks={"port:5050"}, Description="SAIA - S-BUS Ethernet on port 5050"),
    ICS(DeviceType="Generic", DeviceName="XCX 300", VendorName="Schleicher", TcpPorts={}, UdpPorts={}, Dorks={"port:20547"}, Description="Schleicher - XCX 300 on port 20547"),
    ICS(DeviceType="Generic", DeviceName="S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"port:102"}, Description="Siemens - S7 on port 102"),
    ICS(DeviceType="Generic", DeviceName="TCP slave", VendorName="Unitronics", TcpPorts={20256, 20257}, UdpPorts={}, Dorks={"port:20256,20257"}, Description="Unitronics - TCP slave on port 20256"),
    ICS(DeviceType="Generic", DeviceName="CODESYS – TCP", VendorName="Wago", TcpPorts={}, UdpPorts={}, Dorks={"port:2455"}, Description="Wago - CODESYS – TCP on port 2455"),
    # ICS(DeviceType="Generic", DeviceName="MP Series Ethernet", VendorName="YASKAWA", TcpPorts={}, UdpPorts={}, Dorks={"port:10000"}, Description="YASKAWA - MP Series Ethernet on port 10000"),
    ICS(DeviceType="Generic", DeviceName="FA-M3 (Ethernet)", VendorName="Yokogawa", TcpPorts={}, UdpPorts={}, Dorks={"port:12289"}, Description="Yokogawa - FA-M3 (Ethernet) on port 12289"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="Ranger 2003", VendorName="ABB", TcpPorts={10307, 10311, 10364, 10365, 10407, 10409, 10410, 10412, 10414, 10415, 10428, 10431, 10432, 10447, 10449, 10450, 13722, 13724, 13782, 13783, 38589, 38593, 38600, 38971, 39129, 39278}, UdpPorts={}, Dorks={"port:10307,10311,10364,10365,10407,10409,10410,10412,10414,10415,10428,10431,10432,10447,10449,10450,13722,13724,13782,13783,38589,38593,38600,38971,39129,39278"}, Description=""),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="Foxboro DCS FoxApi", VendorName="Foxboro/Invensys", TcpPorts={1541, 45678, 55555}, UdpPorts={45678, 55555}, Dorks={"port:1541,55555,45678"}, Description="Foxboro DCS FoxApi - 55555"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="Genesis32 GenBroker (TCP)", VendorName="Iconics", TcpPorts={18000}, UdpPorts={}, Dorks={"port:18000"}, Description="Genesis32 GenBroker (TCP) - 18000"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="Metasys N1", VendorName="Johnson Controls", TcpPorts={11001}, UdpPorts={11001}, Dorks={"port:11001"}, Description="Metasys N1"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="PI Server", VendorName="OSIsoft", TcpPorts={5450}, UdpPorts={}, Dorks={"port:5450"}, Description="PI Server"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="Spectrum Power TG", VendorName="Siemens", TcpPorts={50001, 50018, 50020, 50021, 50025, 50028, 50110, 50111}, UdpPorts={}, Dorks={"port:500001,50018,50020,50021,50025,50028,50110,50111"}, Description="Spectrum Power TG"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="GENe", VendorName="SNC", TcpPorts={38000, 38001, 38011, 38012, 38014, 38015, 38200, 38210, 38301, 38400, 38700, 62900, 62911, 62924, 62930, 62938, 62956, 62957, 62963, 62981, 62982, 62985, 62992, 63012, 63027, 63036, 63041, 63075, 63079, 63082, 63088, 63094, 65443}, UdpPorts={}, Dorks={"port:38000,38001,38011,38012,38014,38015,38200,38210,38301,38400,38700,62900,62911,62924,62930,62938,62956,62957,62963,62981,62982,62985,62992,63012,63027,63036,63041,63075,63079,63082,63088,63094,65443"}, Description="SNC - GENe"),
    ICS(DeviceType="Vendor Specific Protocol", DeviceName="OASyS DNA", VendorName="Telvent", TcpPorts={5050, 5051, 5052, 5065, 12135, 12137, 56001, 56099}, UdpPorts={}, Dorks={"port:5050,5051,5052,5065,12135,12137,56001,56099"}, Description="Telvent - OASyS DNA"),

    # # #
    # # # Protocols
    # # #
    ICS(DeviceType="Protocol", DeviceName="BACnet/IP", VendorName="", TcpPorts={}, UdpPorts={47808}, Dorks={"port:47808"}, Description="BACnet/IP - 47808"),
    ICS(DeviceType="Protocol", DeviceName="DNP3", VendorName="", TcpPorts={20000}, UdpPorts={20000}, Dorks={"port:20000"}, Description="DNP3 - 20000"),
    ICS(DeviceType="Protocol", DeviceName="EtherCAT", VendorName="", TcpPorts={}, UdpPorts={34980}, Dorks={"port:34980"}, Description="EtherCAT - 34980"),
    ICS(DeviceType="Protocol", DeviceName="Ethernet/IP", VendorName="", TcpPorts={44818}, UdpPorts={2222}, Dorks={"port:44818"}, Description="Ethernet/IP"),
    ICS(DeviceType="Protocol", DeviceName="FL-net", VendorName="", TcpPorts={}, UdpPorts={55000, 55001, 55002, 55003}, Dorks={"port:55000,55001,55002,55003"}, Description="FL-net"),
    ICS(DeviceType="Protocol", DeviceName="Foundation Fieldbus HSE", VendorName="", TcpPorts={1089, 1090, 1091}, UdpPorts={1089, 1090, 1091}, Dorks={"port:1089,1090,1091"}, Description="Foundation Fieldbus HSE"),
    ICS(DeviceType="Protocol", DeviceName="ICCP", VendorName="", TcpPorts={}, UdpPorts={102}, Dorks={"port:102"}, Description="ICCP"), ICS(DeviceType="Protocol", DeviceName="Modbus TCP", VendorName="", TcpPorts={502}, UdpPorts={}, Dorks={"port:502"}, Description="Modbus TCP"),
    ICS(DeviceType="Protocol", DeviceName="OPC UA Discovery Server", VendorName="OPC UA", TcpPorts={4840}, UdpPorts={}, Dorks={"port:4840"}, Description="OPC UA Discovery Server - 4840"),
    ICS(DeviceType="Protocol", DeviceName="PROFINET", VendorName="", TcpPorts={34962, 34963, 34964}, UdpPorts={34962, 34963, 34964}, Dorks={"port:34962,34963,34964"}, Description="PROFINET"),
    ICS(DeviceType="Protocol", DeviceName="ROC PLus", VendorName="", TcpPorts={4000}, UdpPorts={}, Dorks={"port:4000"}, Description="ROC PLus - 4000"),
    ICS(DeviceType="Protocol", DeviceName="FINS", VendorName="OMRON", TcpPorts={9600}, UdpPorts={9600}, Dorks={"port:9600"}, Description="FINS (Factory Interface Network Service)"),
    ICS(DeviceType="Protocol", DeviceName="HART-IP", VendorName="", TcpPorts={5094}, UdpPorts={5094}, Dorks={"port:5094"}, Description="HART-IP (Highway Addressable Remote Transducer over IP)"),
    ICS(DeviceType="Protocol", DeviceName="Unknown", VendorName="Mitsubitshi", TcpPorts={5006}, UdpPorts={5007}, Dorks={"port:5006,5007"}, Description="MELSEC-Q (Mitsubishi electric)"),
    ICS(DeviceType="Protocol", DeviceName="Tridium Fox", VendorName="", TcpPorts={1911, 4911}, UdpPorts={}, Dorks={"port:1911,4911"}, Description="Tridium Fox Protocol by Niagara AX"),
    ICS(DeviceType="Protocol", DeviceName="PCWORX", VendorName="Phoenix Contact", TcpPorts={1962}, UdpPorts={}, Dorks={"port:1962"}, Description="PCWorx by Phoenix Contact"),

    # # #
    # # # ICS by Header's fingerprint
    # # #
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"all:scada"}, Description=""),
    ICS(DeviceType="PLC", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:"Logic controller"'}, Description=""),
    ICS(DeviceType="PLC", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:PLC'}, Description=""),
    ICS(DeviceType="PLC", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:"wind farm"'}, Description=""),
    ICS(DeviceType="PLC", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:"modbus"'}, Description=""),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"all:Siemens"}, Description="Siemens - Siemens"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="FATEK", TcpPorts={}, UdpPorts={}, Dorks={"all:fatek"}, Description="FATEK PLCs"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Adcon", TcpPorts={}, UdpPorts={}, Dorks={"all:adcon"}, Description="Adcon PLCs"),
    # ICS(DeviceType="ICS", DeviceName="Generic", VendorName="ABB", TcpPorts={}, UdpPorts={}, Dorks={"abb"}, Description="ABB PLCs"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="ACKP", TcpPorts={}, UdpPorts={}, Dorks={"all:AKCP"}, Description="ACKP - AKCP Embedded Web Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Allen-Bradley", TcpPorts={}, UdpPorts={}, Dorks={"all:Bradley"}, Description="Rockwell Automation/Allen-Bradley ICSs"),
    # ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Rockwell Automation", TcpPorts={}, UdpPorts={}, Dorks={"Rockwell Automation"}, Description="Rockwell Automation - Rockwell Automation"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:Schneider"}, Description="Schneider Electric - ICS systems"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:Modicon"}, Description="Schneider Electric - Modicon"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:ClearSCADA"}, Description="Schneider Electric - ClearSCADA"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={'all:"Power Measurement"'}, Description="Schneider Electric - Power Measurement"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:PowerLogic"}, Description="Schneider Electric - PowerLogic"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:XENTA"}, Description="Schneider Electric - Tac XENTA"),
    ICS(DeviceType="ICS", DeviceName="Modicon", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"all:TELEMECANIQUE"}, Description="Schneider Electric - TELEMECANIQUE"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="BroadWeb", TcpPorts={}, UdpPorts={}, Dorks={"all:BroadWeb"}, Description="BroadWeb - BroadWeb"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="General Electric", TcpPorts={}, UdpPorts={}, Dorks={'all:"general electric"'}, Description="General Electric Devices"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Cimetrics", TcpPorts={}, UdpPorts={}, Dorks={"all:cinemetrics"}, Description="Cimetrics - Cimetrics Web Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Delta Controls", TcpPorts={}, UdpPorts={}, Dorks={"all:enteliTOUCH"}, Description="Delta Controls - DELTA enteliTOUCH"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Electro Industries GaugeTech", TcpPorts={}, UdpPorts={}, Dorks={'all:"EIG Embedded"'}, Description="Electro Industries GaugeTech - EIG Embedded Web Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Elster EnergyICT", TcpPorts={}, UdpPorts={}, Dorks={"all:EnergyICT"}, Description="Elster EnergyICT - EnergyICT"),
    ICS(DeviceType="ICS", DeviceName="EtherNet/IP /Modbus-TCP Interface", VendorName="HMS", TcpPorts={}, UdpPorts={}, Dorks={"HMS AnyBus"}, Description="HMS - HMS AnyBus WebServer"),
    ICS(DeviceType="ICS", DeviceName="IPC@CHIP", VendorName="Beck IPC", TcpPorts={}, UdpPorts={}, Dorks={'all:"Beck IPC"'}, Description="Beck IPC - IPC@CHIP"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Moxa", TcpPorts={}, UdpPorts={}, Dorks={"all:MoxaHttp"}, Description="Moxa - MoxaHttp"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Tridium", TcpPorts={}, UdpPorts={}, Dorks={"all:Tridium"}, Description="Tridium - Niagara Web Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Novatech", TcpPorts={}, UdpPorts={}, Dorks={'all:"NovaTech HTTPD"'}, Description="Novatech - NovaTech HTTPD"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"all:Powerlink"}, Description="Generic - Powerlink"),
    ICS(DeviceType="ICS", DeviceName="Reliance", VendorName="Reliance", TcpPorts={}, UdpPorts={}, Dorks={"all:Reliance"}, Description="Reliance - Reliance 4 Control Server"),
    ICS(DeviceType="ICS", DeviceName="NetWeaver Application Server", VendorName="SAP", TcpPorts={}, UdpPorts={}, Dorks={"all:NetWeaver"}, Description="SAP - SAP NetWeaver Application Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"all:SLC5"}, Description="Generic - SLC5"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="SoftPLC", TcpPorts={}, UdpPorts={}, Dorks={"all:SoftPLC"}, Description="SoftPLC - SoftPLC"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="SpiderControl", TcpPorts={}, UdpPorts={}, Dorks={"all:SpiderControl"}, Description="SpiderControl - SpiderControl"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Stulz", TcpPorts={}, UdpPorts={}, Dorks={"all:Stulz"}, Description="Stulz - Stulz GmbH Klimatechnik"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wind River", TcpPorts={}, UdpPorts={}, Dorks={"all:VxWorks"}, Description="Wind River - VxWorks"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wago", TcpPorts={}, UdpPorts={}, Dorks={"all:WAGO"}, Description="Wago - WAGO"),
    ICS(DeviceType="ICS", DeviceName="WebVisu", VendorName="Codesys", TcpPorts={}, UdpPorts={}, Dorks={"all:Webvisu"}, Description="Codesys - Webvisu"),
    ICS(DeviceType="ICS", DeviceName="WindCube", VendorName="NRG Systems", TcpPorts={}, UdpPorts={}, Dorks={"all:WindWeb"}, Description="NRG Systems - WindWeb"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Rabbit", TcpPorts={}, UdpPorts={}, Dorks={'all:"Z-World Rabbit"'}, Description="Rabbit - Z-World Rabbit"),
    ICS(DeviceType="ICS", DeviceName="eiPortal", VendorName="Elster EnergyICT", TcpPorts={}, UdpPorts={}, Dorks={"all:eiPortal"}, Description="Elster EnergyICT - eiPortal"),
    ICS(DeviceType="ICS", DeviceName="i.LON 600", VendorName="Echelon", TcpPorts={}, UdpPorts={}, Dorks={'all:'"i.LON"''}, Description="Echelon - i.LON"),
    ICS(DeviceType="ICS", DeviceName="ioLogik", VendorName="Moxa", TcpPorts={}, UdpPorts={}, Dorks={"all:ioLogik"}, Description="Moxa - ioLogik Web Server"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"all:CherryPy"}, Description="Generic - openerp server:CherryPy"),
    ICS(DeviceType="ICS", DeviceName="IQ3xcite", VendorName="Trend", TcpPorts={}, UdpPorts={}, Dorks={"all:iq3"}, Description="Trend - server:iq3"),
    ICS(DeviceType="IvCS",DeviceName="ServerView", VendorName="Fujitsu", TcpPorts={}, UdpPorts={}, Dorks={"all:serverview"}, Description="Fujitsu - serverview"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Somfy", TcpPorts={}, UdpPorts={}, Dorks={"all:Somfy"}, Description="Somfy - title:Somfy"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Adcon Telemetry", TcpPorts={}, UdpPorts={}, Dorks={"all:adcon"}, Description="Adcon Telemetry - title:adcon"),
    ICS(DeviceType="ICS", DeviceName="Electrical car charger", VendorName="DIRIS DIGIWARE", TcpPorts={1081, 1082}, UdpPorts={}, Dorks={"Server: servX"}, Description="DIRIS DIGIWARE: Energy measurement and monitoring system"),

    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:"Jetty 3.1.8 (Windows 2000 5.0 x86)"'}, Description="Generic - Jetty 3.1.8 (Windows 2000 5.0 x86)"),
    ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={'all:"NET ARM Web Server/1.00"'}, Description="Generic - NET ARM Web Server/1.00"),

]


def GetAllIcsPortsList():
    global ICS_List
    result = {'tcp': None, 'udp': None}
    tcp_ports = []
    udp_ports = []

    for ics in ICS_List:
        for tcp_port in ics.TcpPorts:
            tcp_ports.append(tcp_port)
        for udp_port in ics.UdpPorts:
            udp_ports.append(udp_port)

    # Sort ports
    tcp_ports.sort()
    udp_ports.sort()

    result['tcp'] = tcp_ports
    result['udp'] = udp_ports
    return result


def PortToVendorDescription(protocol, port):
    global ICS_List
    for ics in ICS_List:
        if protocol is 'tcp':
            if int(port) in ics.TcpPorts:
                return ics.Description
        else:
            if int(port) in ics.UdpPorts:
                return ics.Description
    return None


def PrintIcsList(ICS_List=None):
    ics = ICS()
    i = 0
    for tmpIcs in ICS_List:
        ics = tmpIcs
        i += 1
        print("[%d] - %s"%(i, ics.Description))
