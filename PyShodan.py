# Shodan API documentation:
# https://shodan.readthedocs.io/en/latest/tutorial.html

import shodan
import sys
import time
import datetime

# Util function to append data t a file
def FileAppend(filename, content):
    with open(filename, 'a') as filehandle:
        filehandle.write(content)


# Return current time
def Timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# Print fancy debugging message
def dbg(dbg_str, alert=0):
    st = Timestamp()
    # Print time stamp only if string does not start with '[' or str is capital
    if dbg_str[0].istitle() or dbg_str[0] is '[' or dbg_str[0] is '>':
        sys.stdout.write("[" + st + "] ")

    if alert == 1:
        sys.stdout.write("\033[1;31m")  # Set text to red
        sys.stdout.write(dbg_str)
        sys.stdout.write("\033[0;0m")   # Reset text
    else:
        sys.stdout.write(dbg_str)
    sys.stdout.flush()


# Print fancy debugging message followed by newline
def dbgln(dbg_str, alert=0):
    dbg(dbg_str + "\n", alert)


# Store shodan results
class ShodanResult:
    # Use python 3.6 to get atributes in the same preserved order
    IpAddr = ""
    Port = ""
    Hostnames = []
    IpDecimal = ""
    Os = "",
    Timestamp = ""
    Isp = ""
    ASN = ""
    Domains = []
    Org = ""
    Data = ""
    Loc_City = ""
    Loc_RegionCode = ""
    Loc_AreaCode = ""
    Loc_Latitude = ""
    Loc_Longitude = ""
    Loc_CountryCode3 = ""
    Loc_CountryName = ""
    Loc_PostalCode = ""
    Loc_DmaCode = ""


# Shodan service handler
class ShodanService:
    _ShodanApi = None
    _LastResults = []

    def __init__(self, shodan_api):
        self._ShodanApi = shodan.Shodan(shodan_api)

    def Search(self, dork):  # type List[ShodanResult]

        Ret = []

        # Get the amount of results for given dork
        total_pages = 0
        results_number = 0
        try:
            results_number = self._ShodanApi.count(dork)['total']
            total_pages = int(results_number / 100) + 1
        except shodan.APIError as e:
            dbgln('Error: {}'.format(e), alert=1)

        dbgln("Results available: {}".format(results_number))

        # Wrap the request in a try/ except block to catch errors
        try:
            for i in range(0, total_pages):
                # Search Shodan
                results = self._ShodanApi.search(query=dork, page=i + 1)

                # Show the results
                # print('Results found: {}'.format(results['total']))
                for result in results['matches']:
                    # Protect against parsing errors
                    try:
                        match = ShodanResult()
                        match.IpAddr = result['ip_str']
                        match.Timestamp = result['timestamp']
                        match.Isp = result['isp']
                        match.Os = result['os']
                        match.ASN = result['asn']
                        match.IpDecimal = result['ip']
                        match.Org = result['org']
                        match.Port = result['port']
                        match.Domains = result['domains']
                        match.Hostnames = result['hostnames']
                        match.Loc_City = result['location']['city']
                        match.Loc_RegionCode = result['location']['region_code']
                        match.Loc_CountryName = result['location']['country_name']
                        match.Loc_Longitude = result['location']['longitude']
                        match.Loc_Longitude = result['location']['longitude']
                        match.Loc_CountryCode3 = result['location']['country_code3']
                        match.Loc_PostalCode = result['location']['postal_code']
                        match.Loc_DmaCode = result['location']['dma_code']
                        Ret.append(match)
                    except Exception as e:
                        dbgln("Error: failed to parse: {}".format(e.message), alert=1)
            # Shodan only allows one request per second
            time.sleep(1)

        except shodan.APIError as e:
            dbgln('Error: {}'.format(e), alert=1)
        self._LastResults = Ret
        return Ret

    def SaveLastResultsAsCsv(self, filename):
        result_atributes = [attr for attr in ShodanResult.__dict__.keys() if not attr.startswith('__')]

        # Append header to file
        csv_header = ""
        for atribute in result_atributes:
            csv_header += atribute + ","
        FileAppend(filename, csv_header)

        # Append data to the file
        csv_row = ""
        for result in self._LastResults:
            result_values = [attr for attr in result.__dict__.values() if not attr.startswith('__')]
            for value in result_values:
                csv_row += value + ","
