from PyUtil.Util import *
from PyUtil.IcsScanner import *
from PyUtil.PortsScanner import *
from PyUtil.ThreadPool import *


class IcsScanResult:
    def __init__(self):
        self.IpAddress = ""
        self.Time = ""
        self.Hostname = ""
        self.Organization = ""
        self.ASN = ""
        self.Ping = None
        self.OpenTcpPorts = []
        self.OpenUdpPorts = []
        self.IcsDetected = False
        self.VendorsListIds = []
        self.VendorsDetails = []
        self.ScanSucceed = True


class ScanEngine:
    def __init__(self, threads_no=10):
        self.__pool = ThreadPool(threads_no)
        self.__export_filename = ""
        self.__ip_addresses_list = {}
        self.__print_idx = 0

    def Event_IcsScanFinished(self, result_scan: IcsScanResult):
        # Store result into dict, and display it if it is next to be shown
        self.__ip_addresses_list[result_scan.IpAddress] = result_scan

        # Display and print next IP addresses in the queue
        while (True):
            first_element_key = list(self.__ip_addresses_list)[0]
            if self.__ip_addresses_list[first_element_key]:
                scan_res = self.__ip_addresses_list[first_element_key]
                csv_data = "%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (self.__print_idx,
                                                                         scan_res.Time,
                                                                         scan_res.IpAddress,
                                                                         scan_res.Hostname,
                                                                         scan_res.Organization,
                                                                         scan_res.ASN,
                                                                         scan_res.Ping['latency'],
                                                                         "succeed" if scan_res.ScanSucceed else "failed",
                                                                         scan_res.IcsDetected,
                                                                         ','.join([str(x) for x in scan_res.OpenTcpPorts]),
                                                                         ','.join([str(x) for x in scan_res.OpenUdpPorts]),
                                                                         '|'.join([str(x) for x in scan_res.VendorsDetails]),
                                                                         "")
                # remove vendors details from printing, only keep them in files
                dbg_data = csv_data.rsplit(";", 2)[0]
                dbg_data = dbg_data.split(";")
                dbg_data[0] = "\033[1;31m" + str(self.__print_idx) + "\033[0;0m"
                dbg_data = ';'.join([str(x) for x in dbg_data])
                dbg_timestamp(dbg_data + "\n", 0, True)

                # Append data to file
                FileAppend(self.__export_filename, csv_data)
                self.__print_idx += 1

                # Remove first element from list as it was already added to fine and it was printed
                del(self.__ip_addresses_list[first_element_key])

            else:
                break

    def Ics_ScanSingleIp(self, ip_addr, print_info=False, trigger_finish_callback=False) -> Union[IcsScanResult, None]:
        if not IsValidIPv4(ip_addr):
            return

        if print_info:
            dbgln("Scanning ip '%s' for industrial control systems..." % str(ip_addr), 1)

        scan_result = IcsScanResult()
        ics = IcsScanner(ip_addr)
        scan_result.IpAddress = ics.GetIpAddress()
        scan_result.Time = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S'))

        scan_result.Hostname = ics.GetHostname()
        if print_info:
            dbgln("Hostname: %s" % str(scan_result.Hostname))

        ip_info = GetIpInfo(ip_addr)
        scan_result.Organization = ip_info['org'].replace(";", "")
        scan_result.ASN = ip_info['asn'].replace(";", "")
        if print_info:
            dbgln("ISP: %s" % scan_result.Organization)
            dbgln("ASN: %s" % scan_result.ASN)

        scan_result.Ping = ics.Ping()
        if print_info:
            dbgln("Ping: %s" % str(scan_result.Ping['latency']))

        try:
            scan_result.OpenUdpPorts = ics.GetOpenUdpPorts()
            scan_result.OpenTcpPorts = ics.GetOpenTcpPorts()
            if print_info:
                dbgln("Ports open: tcp:%s, udp:%s" % ((','.join([str(x) for x in scan_result.OpenTcpPorts]) if len(scan_result.OpenTcpPorts) else "none"),
                      (','.join([str(x) for x in scan_result.OpenUdpPorts]) if len(scan_result.OpenUdpPorts) else "none")))

            scan_result.IcsDetected = True if (len(scan_result.OpenTcpPorts) > 0) else False
            if print_info:
                dbgln("ICS detected: %s" % str(scan_result.IcsDetected))

            if scan_result.OpenTcpPorts or scan_result.OpenUdpPorts:
                if print_info:
                    dbgln("Potential vendors:")

                scan_result.VendorsListIds = []
                # Read all possible vendors by discovered open TCP ports
                for port in scan_result.OpenTcpPorts:
                    tmp = PortToVendorId('tcp', int(port))
                    if tmp is not None:
                        scan_result.VendorsListIds.append(tmp)
                # Read all possible vendors by discovered open UDP ports
                for port in scan_result.OpenUdpPorts:
                    tmp = PortToVendorId('udp', int(port))
                    if tmp is not None:
                        scan_result.VendorsListIds.append(tmp)

                # Remove duplicate vendors (multiple ports can point to same vendor)
                scan_result.VendorsListIds = set(scan_result.VendorsListIds)

                # Print each possible vendor
                for vendor_idx in scan_result.VendorsListIds:
                    ics = GetVendorById(vendor_idx)
                    vendor_desc_str = ""
                    vendor_desc_str += ics.DeviceName

                    if ics.VendorName:
                        vendor_desc_str += ", " + ics.VendorName
                    if ics.DeviceType:
                        vendor_desc_str += ", " + ics.DeviceType

                    # Add detected TCP ports open
                    vendor_desc_str += ", (tcp:"
                    for vendor_port in ics.TcpPorts:
                        if vendor_port in scan_result.OpenTcpPorts:
                            vendor_desc_str += str(vendor_port) + ","
                    vendor_desc_str = vendor_desc_str[:-1]
                    vendor_desc_str += ")"

                    # Add detected UDP ports open
                    vendor_desc_str += ", (udp:"
                    for vendor_port in ics.UdpPorts:
                        if vendor_port in scan_result.OpenUdpPorts:
                            vendor_desc_str += str(vendor_port) + ","
                    vendor_desc_str = vendor_desc_str[:-1]
                    vendor_desc_str += ")"

                    scan_result.VendorsDetails.append(vendor_desc_str)
                    if print_info:
                        dbg_timestamp("\t-> " + vendor_desc_str + "\n", 0, 1)

        except Exception as e:
            scan_result.ScanSucceed = False
            dbgln("EXCEPTION (%s): %s" % (str(ip_addr), str(e)))

        if trigger_finish_callback:
            self.Event_IcsScanFinished(scan_result)

        return scan_result

    def Ics_ScanMultipleIPs(self, input_file):
        # Write CSV header
        input_path = os.path.dirname(input_file)
        input_filename = os.path.basename(input_file)

        self.__export_filename = input_path + "/" + input_filename + "_results_from_{}.csv".format(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')))
        csv_data = "Index;Time;IP;Hostname;Organization;ASN;Ping;Scan status;ICS Detected;ICS TCP ports open;ICS UDP Ports open;ICS Vendors;Raw scan\n"
        FileWrite(self.__export_filename, csv_data)
        dbgln("writing results to " + self.__export_filename)
        dbgln(csv_data)

        # ICS Scanner
        idx = 0

        # Read all the IPv4 addresses
        for line in FileGetLines(input_file):
            ip = ExtractIPv4(line)
            if not ip:
                continue
            # Add to IPs list
            self.__ip_addresses_list[ip] = None
            # Trigger the job
            self.__pool.add_task(self.Ics_ScanSingleIp, ip, False, True)

        # Wait for jobs to finish
        self.__pool.wait_completion()

    def Ports_ScanMultiplePorts(self):
        # CSV format to be saved
        csv_data = "Index;Time;IP;Hostname;Ping;Scan status;Ports open;Raw scan\n\n"
        dbgln(csv_data)
        # Ports scanner
        idx = 0
        for ip in FileGetLines("ips.txt"):
            if not IsValidIPv4(ip):
                continue
            ics = PortsScanner(ip)
            hostname = ics.GetHostname()
            ping = ics.Ping()['latency']
            try:
                open_ports = (','.join([str(i) for i in ics.GetDefaultOpenTcpPorts()]))
                csv_data += "%d;%s;%s;%s;%s;%s;%s;%s\n" % (idx, Datetime(), ip, hostname, ping, "succeed", open_ports, "")
                dbgln(csv_data)
                idx += 1
            except Exception as e:
                csv_data += "%d;%s;%s;%s;%s;%s\n" % (idx, Datetime(), ip, hostname, ping, "failed")
                dbgln(csv_data)
                dbgln(e)

        # Export data to a CSV file
        FileWrite("scan_ports_results.csv", (csv_data))
