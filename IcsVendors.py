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
            ICS(DeviceType="PLC", DeviceName="ECL Apex", VendorName="Danfoss", TcpPorts={5050}, UdpPorts={}, Dorks={"port:5050"}, Description="Danfoss ECL Apex: 5050"),
            ICS(DeviceType="Generic", DeviceName="QuickPanels", VendorName="GE", TcpPorts={}, UdpPorts={}, Dorks={"port:57176"}, Description="GE - QuickPanels on port 57176"),
            ICS(DeviceType="Generic", DeviceName="EHV Series", VendorName="HITACHI", TcpPorts={}, UdpPorts={}, Dorks={"port:3004"}, Description="HITACHI - EHV Series on port 3004"),
            ICS(DeviceType="Generic", DeviceName="KV-5000", VendorName="KEYENCE", TcpPorts={}, UdpPorts={}, Dorks={"port:8501"}, Description="KEYENCE - KV-5000 on port 8501"),
            ICS(DeviceType="Generic", DeviceName="Koyo Ethernet", VendorName="Koyo", TcpPorts={}, UdpPorts={}, Dorks={"port:28784"}, Description="Koyo - Koyo Ethernet on port 28784"),
            ICS(DeviceType="Generic", DeviceName="FEnet", VendorName="LS GLOFA", TcpPorts={}, UdpPorts={}, Dorks={"port:2004"}, Description="LS GLOFA - FEnet on port 2004"),
            ICS(DeviceType="Generic", DeviceName="Electric car charger", VendorName="kamstrup", TcpPorts={}, UdpPorts={}, Dorks={"port:1025"}, Description="Mitsubishi - FX on port 1025"),
            # ICS(DeviceType="Generic", DeviceName="FX3u Ethernet", VendorName="MITSUBISHI", TcpPorts={}, UdpPorts={}, Dorks={"port:5001"}, Description="MITSUBISHI - FX3u Ethernet on port 5001"),
            ICS(DeviceType="Generic", DeviceName="MR-MQ100 Ethernet", VendorName="MITSUBISHI", TcpPorts={}, UdpPorts={}, Dorks={"port:4999"}, Description="MITSUBISHI - MR-MQ100 Ethernet on port 4999"),
            ICS(DeviceType="Generic", DeviceName="QJ71E71 (Ethernet", VendorName="MITSUBISHI", TcpPorts={}, UdpPorts={}, Dorks={"port:5002"}, Description="MITSUBISHI - QJ71E71 (Ethernet on port 5002"),
            ICS(DeviceType="Generic", DeviceName="FP Ethernet", VendorName="Panasonic", TcpPorts={}, UdpPorts={}, Dorks={"port:9094"}, Description="Panasonic - FP Ethernet on port 9094"),
            ICS(DeviceType="Generic", DeviceName="FP2 Ethernet", VendorName="Panasonic", TcpPorts={}, UdpPorts={}, Dorks={"port:8500"}, Description="Panasonic - FP2 Ethernet on port 8500"),
            ICS(DeviceType="Generic", DeviceName="HMI", VendorName="Red Lion", TcpPorts={}, UdpPorts={}, Dorks={"port:789"}, Description="Red Lion - HMI on port 789"),
            ICS(DeviceType="Generic", DeviceName="S-BUS Ethernet", VendorName="SAIA", TcpPorts={}, UdpPorts={}, Dorks={"port:5050"}, Description="SAIA - S-BUS Ethernet on port 5050"),
            ICS(DeviceType="Generic", DeviceName="XCX 300", VendorName="Schleicher", TcpPorts={}, UdpPorts={}, Dorks={"port:20547"}, Description="Schleicher - XCX 300 on port 20547"),
            ICS(DeviceType="Generic", DeviceName="S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"port:102"}, Description="Siemens - S7 on port 102"),
            ICS(DeviceType="Generic", DeviceName="TCP slave", VendorName="Unitronics", TcpPorts={}, UdpPorts={}, Dorks={"port:20256"}, Description="Unitronics - TCP slave on port 20256"),
            ICS(DeviceType="Generic", DeviceName="Socket3 – TCP slave", VendorName="Unitronicsw", TcpPorts={}, UdpPorts={}, Dorks={"port:20257"}, Description="Unitronicsw - Socket3 – TCP slave on port 20257"),
            ICS(DeviceType="Generic", DeviceName="CODESYS – TCP", VendorName="Wago", TcpPorts={}, UdpPorts={}, Dorks={"port:2455"}, Description="Wago - CODESYS – TCP on port 2455"),
            # ICS(DeviceType="Generic", DeviceName="MP Series Ethernet", VendorName="YASKAWA", TcpPorts={}, UdpPorts={}, Dorks={"port:10000"}, Description="YASKAWA - MP Series Ethernet on port 10000"),
            ICS(DeviceType="Generic", DeviceName="FA-M3 (Ethernet)", VendorName="Yokogawa", TcpPorts={}, UdpPorts={}, Dorks={"port:12289"}, Description="Yokogawa - FA-M3 (Ethernet) on port 12289"),
            #
            # Protocols
            #
            ICS(DeviceType="Protocol", DeviceName="BACnet/IP", VendorName="", TcpPorts={}, UdpPorts={47808}, Dorks={"port:47808"}, Description="BACnet/IP - 47808"),
            ICS(DeviceType="Protocol", DeviceName="DNP3", VendorName="", TcpPorts={20000}, UdpPorts={20000}, Dorks={"port:20000"}, Description="DNP3 - 20000"),
            ICS(DeviceType="Protocol", DeviceName="EtherCAT", VendorName="", TcpPorts={}, UdpPorts={34980}, Dorks={"port:34980"}, Description="EtherCAT - 34980"),
            ICS(DeviceType="Protocol", DeviceName="Ethernet/IP", VendorName="", TcpPorts={44818}, UdpPorts={2222}, Dorks={"port:44818"}, Description="Ethernet/IP"),
            ICS(DeviceType="Protocol", DeviceName="FL-net", VendorName="", TcpPorts={}, UdpPorts={55000, 55001, 55002, 55003}, Dorks={"port:55000,55001,55002,55003"}, Description="FL-net"),
            ICS(DeviceType="Protocol", DeviceName="Foundation Fieldbus HSE", VendorName="", TcpPorts={1089, 1090, 1091}, UdpPorts={1089, 1090, 1091}, Dorks={"port:1089,1090,1091"}, Description="Foundation Fieldbus HSE"),
            ICS(DeviceType="Protocol", DeviceName="ICCP", VendorName="", TcpPorts={}, UdpPorts={102}, Dorks={"port:102"}, Description="ICCP"),
            ICS(DeviceType="Protocol", DeviceName="Modbus TCP", VendorName="", TcpPorts={502}, UdpPorts={}, Dorks={"port:502"}, Description="Modbus TCP"),
            ICS(DeviceType="Protocol", DeviceName="OPC UA Discovery Server", VendorName="OPC UA", TcpPorts={4840}, UdpPorts={}, Dorks={"port:4840"}, Description="OPC UA Discovery Server - 4840"),
            ICS(DeviceType="Protocol", DeviceName="PROFINET", VendorName="", TcpPorts={34962, 34963, 34964}, UdpPorts={34962, 34963, 34964}, Dorks={"port:34962,34963,34964"}, Description="PROFINET"),
            ICS(DeviceType="Protocol", DeviceName="ROC PLus", VendorName="", TcpPorts={4000}, UdpPorts={}, Dorks={"port:4000"}, Description="ROC PLus - 4000"),
            ICS(DeviceType="Protocol", DeviceName="FINS", VendorName="OMRON", TcpPorts={9600}, UdpPorts={9600}, Dorks={"port:9600"}, Description="FINS (Factory Interface Network Service)"),
            ICS(DeviceType="Protocol", DeviceName="HART-IP", VendorName="", TcpPorts={5094}, UdpPorts={5094}, Dorks={"port:5094"}, Description="HART-IP (Highway Addressable Remote Transducer over IP)"),
            ICS(DeviceType="Protocol", DeviceName="Unknown", VendorName="Mitsubitshi", TcpPorts={5006}, UdpPorts={5007}, Dorks={"port:5006,5007"}, Description="MELSEC-Q (Mitsubishi electric)"),
            ICS(DeviceType="Protocol", DeviceName="Tridium Fox", VendorName="", TcpPorts={1911, 4911}, UdpPorts={}, Dorks={"port:1911,4911"}, Description="Tridium Fox Protocol by Niagara AX"),
            ICS(DeviceType="Protocol", DeviceName="PCWORX", VendorName="Phoenix Contact", TcpPorts={1962}, UdpPorts={}, Dorks={"port:1962"}, Description="PCWorx is a protocol and program by Phoenix Contact used by a wide range of industries."),

            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Ranger 2003", VendorName="ABB", TcpPorts={10307, 10311, 10364, 10365, 10407, 10409, 10410, 10412, 10414, 10415, 10428, 10431, 10432, 10447, 10449, 10450, 13722, 13724, 13782, 13783, 38589, 38593, 38600, 38971, 39129, 39278}, UdpPorts={}, Dorks={"port:10307", "port:39278"}, Description=""),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Foxboro DCS FoxApi", VendorName="Foxboro/Invensys", TcpPorts={55555}, UdpPorts={55555}, Dorks={"port:55555"}, Description="Foxboro DCS FoxApi - 55555"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Foxboro DCS AIMAPI", VendorName="Foxboro/Invensys", TcpPorts={45678}, UdpPorts={45678}, Dorks={"port:45678"}, Description="Foxboro DCS AIMAPI"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Foxboro/Invensys", VendorName="Foxboro DCS Informix", TcpPorts={1541}, UdpPorts={1541}, Dorks={"port:1541"}, Description="Foxboro DCS Informix - 1541"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Genesis32 GenBroker (TCP)", VendorName="Iconics", TcpPorts={18000}, UdpPorts={}, Dorks={"port:18000"}, Description="Genesis32 GenBroker (TCP) - 18000"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Metasys N1", VendorName="Johnson Controls", TcpPorts={11001}, UdpPorts={11001}, Dorks={"port:11001"}, Description="Metasys N1"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="PI Server", VendorName="OSIsoft", TcpPorts={5450}, UdpPorts={}, Dorks={"port:5450"}, Description="PI Server"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="Spectrum Power TG", VendorName="Siemens", TcpPorts={500001,50018,50020,50021,50025,50028,50110,50111}, UdpPorts={}, Dorks={"port:50001", "port:50110"}, Description="Spectrum Power TG"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="GENe", VendorName="SNC", TcpPorts={38000, 38001, 38011, 38012, 38014, 38015, 38200, 38210, 38301, 38400, 38700, 62900, 62911, 62924, 62930, 62938, 62956, 62957, 62963, 62981, 62982, 62985, 62992, 63012, 63027, 63036, 63041, 63075, 63079, 63082, 63088, 63094, 65443}, UdpPorts={}, Dorks={"port:38000", "port:65443", "port:62900"}, Description="SNC - GENe"),
            ICS(DeviceType="Vendor Specific Protocol", DeviceName="OASyS DNA", VendorName="Telvent", TcpPorts={5050, 5051, 5052, 5065, 12135, 12137, 56001, 56099}, UdpPorts={}, Dorks={"port:5050", "port:12135", "port:56001"}, Description="Telvent - OASyS DNA"),

            ICS(DeviceType="PLC", DeviceName="FBs-PLC", VendorName="FATEK", TcpPorts={500}, UdpPorts={}, Dorks={"fatek"}, Description="FATEK FB Series: 500"),
            ICS(DeviceType="ICS", DeviceName="A850 Telemetry Gateway", VendorName="Adcon Telemetry", TcpPorts={}, UdpPorts={}, Dorks={"A850 Telemetry Gateway"}, Description="Adcon Telemetry - A850 Telemetry Gateway"),
            ICS(DeviceType="ICS", DeviceName="RTU500", VendorName="ABB", TcpPorts={}, UdpPorts={}, Dorks={"ABB RTU560"}, Description="ABB - ABB RTU560"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="ABB", TcpPorts={}, UdpPorts={}, Dorks={"ABB Webmodule"}, Description="ABB - ABB Webmodule"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="ACKP", TcpPorts={}, UdpPorts={}, Dorks={"AKCP Embedded Web Server"}, Description="ACKP - AKCP Embedded Web Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Allen-Bradley", TcpPorts={}, UdpPorts={}, Dorks={"Allen-Bradley"}, Description="Allen-Bradley - Allen-Bradley"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="BroadWeb", TcpPorts={}, UdpPorts={}, Dorks={"BroadWeb"}, Description="BroadWeb - BroadWeb"),
            ICS(DeviceType="ICS", DeviceName="Cimplicity", VendorName="General Electric", TcpPorts={}, UdpPorts={}, Dorks={"CIMPLICITY-HttpSvr"}, Description="General Electric - CIMPLICITY-HttpSvr"),
            ICS(DeviceType="ICS", DeviceName="Eplus – B/IP to B/WS Gateway Firewall", VendorName="Cimetrics", TcpPorts={}, UdpPorts={}, Dorks={"Cimetrics Eplus Web Server"}, Description="Cimetrics - Cimetrics Eplus Web Server"),
            ICS(DeviceType="ICS", DeviceName="CitectSCADA", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"CitectSCADA"}, Description="Schneider Electric - CitectSCADA"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"ClearSCADA"}, Description="Schneider Electric - ClearSCADA"),
            ICS(DeviceType="ICS", DeviceName="enteliTOUCH", VendorName="Delta Controls", TcpPorts={}, UdpPorts={}, Dorks={"DELTA enteliTOUCH"}, Description="Delta Controls - DELTA enteliTOUCH"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Electro Industries GaugeTech", TcpPorts={}, UdpPorts={}, Dorks={"EIG Embedded Web Server"}, Description="Electro Industries GaugeTech - EIG Embedded Web Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Elster EnergyICT", TcpPorts={}, UdpPorts={}, Dorks={"EnergyICT"}, Description="Elster EnergyICT - EnergyICT"),
            ICS(DeviceType="ICS", DeviceName="RTU", VendorName="Elster EnergyICT", TcpPorts={}, UdpPorts={}, Dorks={"EnergyICT RTU"}, Description="Elster EnergyICT - EnergyICT RTU"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"GoAhead-Webs InitialPage.asp"}, Description="Generic - GoAhead-Webs InitialPage.asp"),
            ICS(DeviceType="ICS", DeviceName="Simatic HMI", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"HMI, XP277"}, Description="Siemens - HMI, XP277"),
            ICS(DeviceType="ICS", DeviceName="EtherNet/IP /Modbus-TCP Interface", VendorName="HMS", TcpPorts={}, UdpPorts={}, Dorks={"HMS AnyBus-S WebServer"}, Description="HMS - HMS AnyBus-S WebServer"),
            ICS(DeviceType="ICS", DeviceName="IPC@CHIP", VendorName="Beck IPC", TcpPorts={}, UdpPorts={}, Dorks={"IPC@CHIP"}, Description="Beck IPC - IPC@CHIP"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Clorius Controls", TcpPorts={}, UdpPorts={}, Dorks={"ISC SCADA Service HTTPserv:00001"}, Description="Clorius Controls - ISC SCADA Service HTTPserv:00001"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"Jetty 3.1.8 (Windows 2000 5.0 x86)"}, Description="Generic - Jetty 3.1.8 (Windows 2000 5.0 x86)"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"Modbus Bridge"}, Description="Generic - Modbus Bridge"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"ModbusGW"}, Description="Generic - ModbusGW"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"“Server: VTS” -IIS -Apache -nginx 401 -500 -Boa -Sitewatch -Apple -httpd -cpsrvd -Ubicom -DCS-6620"},
                Description="Generic - “Server: VTS” -IIS -Apache -nginx 401 -500 -Boa -Sitewatch -Apple -httpd -cpsrvd -Ubicom -DCS-6620"),
            ICS(DeviceType="ICS", DeviceName="Micrologix", VendorName="Rockwell Automation", TcpPorts={}, UdpPorts={}, Dorks={"Micrologix"}, Description="Rockwell Automation - Micrologix"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"NET ARM Web Server/1.00"}, Description="Generic - NET ARM Web Server/1.00"),
            ICS(DeviceType="ICS", DeviceName="Modicon", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Modicon M340"}, Description="Schneider Electric - Modicon M340"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Moxa", TcpPorts={}, UdpPorts={}, Dorks={"MoxaHttp"}, Description="Moxa - MoxaHttp"),
            ICS(DeviceType="ICS", DeviceName="Modicon", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Modicon M340 CPU"}, Description="Schneider Electric - Modicon M340 CPU"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Tridium", TcpPorts={}, UdpPorts={}, Dorks={"Niagara Web Server"}, Description="Tridium - Niagara Web Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"PLC"}, Description="Generic - PLC"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Portal0000.htm"}, Description="Siemens - Portal0000.htm"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Portal0000"}, Description="Siemens - Portal0000"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Tridium", TcpPorts={}, UdpPorts={}, Dorks={"Niagara Web Server"}, Description="Tridium - Niagara Web Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Novatech", TcpPorts={}, UdpPorts={}, Dorks={"NovaTech HTTPD"}, Description="Novatech - NovaTech HTTPD"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic ION", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Power Measurement Ltd ION8650"}, Description="Schneider Electric - Power Measurement Ltd ION8650"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Power Measurement Ltd"}, Description="Schneider Electric - Power Measurement Ltd"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic PM", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"PowerLogic PM800"}, Description="Schneider Electric - PowerLogic PM800"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"Powerlink"}, Description="Generic - Powerlink"),
            ICS(DeviceType="ICS", DeviceName="Proficy", VendorName="General Electric", TcpPorts={}, UdpPorts={}, Dorks={"ProficyPortal"}, Description="General Electric - ProficyPortal"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="RTS Services", TcpPorts={}, UdpPorts={}, Dorks={"RTS SCADA Server"}, Description="RTS Services - RTS SCADA Server"),
            ICS(DeviceType="ICS", DeviceName="Reliance 4", VendorName="Reliance", TcpPorts={}, UdpPorts={}, Dorks={"Reliance 4 Control Server"}, Description="Reliance - Reliance 4 Control Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Rockwell Automation", TcpPorts={}, UdpPorts={}, Dorks={"Rockwell Automation"}, Description="Rockwell Automation - Rockwell Automation"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"S7-200"}, Description="Siemens - S7-200"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"S7-300"}, Description="Siemens - S7-300"),
            ICS(DeviceType="ICS", DeviceName="NetWeaver Application Server", VendorName="SAP", TcpPorts={}, UdpPorts={}, Dorks={"SAP NetWeaver Application Server"}, Description="SAP - SAP NetWeaver Application Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"SCADA"}, Description="Generic - SCADA"),
            ICS(DeviceType="ICS", DeviceName="Simatic HMI", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"SIMATIC HMI"}, Description="Siemens - SIMATIC HMI"),
            ICS(DeviceType="ICS", DeviceName="Simatic NET", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"SIMATIC NET"}, Description="Siemens - SIMATIC NET"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"SLC5"}, Description="Generic - SLC5"),
            ICS(DeviceType="ICS", DeviceName="Scalance S", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Scalance S"}, Description="Siemens - Scalance S"),
            ICS(DeviceType="ICS", DeviceName="Scalance W", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Scalance W"}, Description="Siemens - Scalance W"),
            ICS(DeviceType="ICS", DeviceName="Scalance X", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Scalance X"}, Description="Siemens - Scalance X"),
            ICS(DeviceType="ICS", DeviceName="SPbus gateway", VendorName="Schleifenbauer", TcpPorts={}, UdpPorts={}, Dorks={"Schleifenbauer SPbus gateway"}, Description="Schleifenbauer - Schleifenbauer SPbus gateway"),
            ICS(DeviceType="ICS", DeviceName="Scalance X", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Scalance X"}, Description="Siemens - Scalance X"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic ECC", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Schneider Electric ECC21"}, Description="Schneider Electric - Schneider Electric ECC21"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic EGX", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Schneider Electric EGX100MG"}, Description="Schneider Electric - Schneider Electric EGX100MG"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic PM", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Schneider Electric PM820SD"}, Description="Schneider Electric - Schneider Electric PM820SD"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic PM1", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Schneider Electric PM870SD"}, Description="Schneider Electric - Schneider Electric PM870SD"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Schneider-WEB"}, Description="Schneider Electric - Schneider-WEB"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Allen-Bradley", TcpPorts={}, UdpPorts={}, Dorks={"Series C Revision"}, Description="Allen-Bradley - Series C Revision"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Siemens"}, Description="Siemens - Siemens"),
            ICS(DeviceType="ICS", DeviceName="Simatic HMI", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Simatic"}, Description="Siemens - Simatic"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Simatic -S7 HMI"}, Description="Siemens - Simatic -S7 HMI"),
            ICS(DeviceType="ICS", DeviceName="Simatic S7", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Simatic S7"}, Description="Siemens - Simatic S7"),
            ICS(DeviceType="ICS", DeviceName="Simatic NET", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Simatic net"}, Description="Siemens - Simatic net"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="SoftPLC", TcpPorts={}, UdpPorts={}, Dorks={"SoftPLC"}, Description="SoftPLC - SoftPLC"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="SpiderControl", TcpPorts={}, UdpPorts={}, Dorks={"SpiderControl"}, Description="SpiderControl - SpiderControl"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Stulz", TcpPorts={}, UdpPorts={}, Dorks={"Stulz GmbH Klimatechnik"}, Description="Stulz - Stulz GmbH Klimatechnik"),
            ICS(DeviceType="ICS", DeviceName="Tac XENTA 913", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"TAC/Xenta"}, Description="Schneider Electric - TAC/Xenta"),
            ICS(DeviceType="ICS", DeviceName="Modicon", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"TELEMECANIQUE BMX"}, Description="Schneider Electric - TELEMECANIQUE BMX"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="THUS", TcpPorts={}, UdpPorts={}, Dorks={"THUS plc FTP server"}, Description="THUS - THUS plc FTP server"),
            ICS(DeviceType="ICS", DeviceName="Tac XENTA 913", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Tac XENTA 913"}, Description="Schneider Electric - Tac XENTA 913"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wind River", TcpPorts={}, UdpPorts={}, Dorks={"VxWorks"}, Description="Wind River - VxWorks"),
            ICS(DeviceType="ICS", DeviceName="Tac XENTA 913", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"Tac XENTA 913"}, Description="Schneider Electric - Tac XENTA 913"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wind River", TcpPorts={}, UdpPorts={}, Dorks={"VxWorks"}, Description="Wind River - VxWorks"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wago", TcpPorts={}, UdpPorts={}, Dorks={"WAGO"}, Description="Wago - WAGO"),
            ICS(DeviceType="ICS", DeviceName="WebVisu", VendorName="Codesys", TcpPorts={}, UdpPorts={}, Dorks={"Webvisu"}, Description="Codesys - Webvisu"),
            ICS(DeviceType="ICS", DeviceName="Simatic HMI", VendorName="Siemens", TcpPorts={}, UdpPorts={}, Dorks={"Welcome to the Windows CE Telnet Service on HMI_Panel"}, Description="Siemens - Welcome to the Windows CE Telnet Service on HMI_Panel"),
            ICS(DeviceType="ICS", DeviceName="WindCube", VendorName="NRG Systems", TcpPorts={}, UdpPorts={}, Dorks={"WindWeb"}, Description="NRG Systems - WindWeb"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Wind River", TcpPorts={}, UdpPorts={}, Dorks={"WindRiver-WebServer"}, Description="Wind River - WindRiver-WebServer"),
            ICS(DeviceType="ICS", DeviceName="addUPI-OPC Server", VendorName="Adcon Telemetry", TcpPorts={}, UdpPorts={}, Dorks={"addUPI Server"}, Description="Adcon Telemetry - addUPI Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Rabbit", TcpPorts={}, UdpPorts={}, Dorks={"Z-World Rabbit"}, Description="Rabbit - Z-World Rabbit"),
            ICS(DeviceType="ICS", DeviceName="eiPortal", VendorName="Elster EnergyICT", TcpPorts={}, UdpPorts={}, Dorks={"eiPortal"}, Description="Elster EnergyICT - eiPortal"),
            ICS(DeviceType="ICS", DeviceName="i.LON 600", VendorName="Echelon", TcpPorts={}, UdpPorts={}, Dorks={"i.LON"}, Description="Echelon - i.LON"),
            ICS(DeviceType="ICS", DeviceName="ioLogik", VendorName="Moxa", TcpPorts={}, UdpPorts={}, Dorks={"ioLogik Web Server"}, Description="Moxa - ioLogik Web Server"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Tridium", TcpPorts={}, UdpPorts={}, Dorks={"niagara_audit"}, Description="Tridium - niagara_audit"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Tridium", TcpPorts={}, UdpPorts={}, Dorks={"niagara_audit -login"}, Description="Tridium - niagara_audit -login"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"openerp server:CherryPy"}, Description="Generic - openerp server:CherryPy"),
            ICS(DeviceType="ICS", DeviceName="PowerLogic ION", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"port:23 “Meter ION”"}, Description="Schneider Electric - port:23 “Meter ION”"),
            ICS(DeviceType="ICS", DeviceName="IQ3xcite", VendorName="Trend", TcpPorts={}, UdpPorts={}, Dorks={"server:iq3"}, Description="Trend - server:iq3"),
            ICS(DeviceType="ICS", DeviceName="ServerView", VendorName="Fujitsu", TcpPorts={}, UdpPorts={}, Dorks={"serverview"}, Description="Fujitsu - serverview"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Schneider Electric", TcpPorts={}, UdpPorts={}, Dorks={"title:PowerLogic"}, Description="Schneider Electric - title:PowerLogic"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Somfy", TcpPorts={}, UdpPorts={}, Dorks={"title:Somfy"}, Description="Somfy - title:Somfy"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Adcon Telemetry", TcpPorts={}, UdpPorts={}, Dorks={"title:adcon"}, Description="Adcon Telemetry - title:adcon"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Rabbit", TcpPorts={}, UdpPorts={}, Dorks={"title:phasefale Z-World Rabbit"}, Description="Rabbit - title:phasefale Z-World Rabbit"),
            ICS(DeviceType="ICS", DeviceName="Generic", VendorName="Generic", TcpPorts={}, UdpPorts={}, Dorks={"webSCADA-Modbus"}, Description="Generic - webSCADA-Modbus"),
            ICS(DeviceType="Energy measurement and monitoring system", DeviceName="Electrical car charger", VendorName="DIRIS DIGIWARE", TcpPorts={1081, 1082}, UdpPorts={}, Dorks={"Server: servX"}, Description="DIRIS DIGIWARE: Energy measurement and monitoring system"),

            # ICS(DeviceType="", DeviceName="", VendorName="", TcpPorts={}, UdpPorts={}, Dorks={"port:"}, Description=""),
            ]


def PrintIcsList(ICS_List=None):
    ics = ICS()
    i = 0
    for tmpIcs in ICS_List:
        ics = tmpIcs
        i += 1
        print({"}. {"}.format(i, ics.Description))
