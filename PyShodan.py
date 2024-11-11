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
    if dbg_str[0].istitle() or dbg_str[0] == '[' or dbg_str[0] == '>':
        sys.stdout.write("[" + st + "] ")

    if alert == 1:
        sys.stdout.write("\033[1;31m")  # Set text to red
        sys.stdout.write(dbg_str)
        sys.stdout.write("\033[0;0m")  # Reset text
    else:
        sys.stdout.write(dbg_str)
    sys.stdout.flush()


# Print fancy debugging message followed by newline
def dbgln(dbg_str, alert=0):
    dbg(dbg_str + "\n", alert)


# Store shodan results
class ShodanResult:
    # Use python 3.6 to get atributes in the same preserved order
    def __init__(self):
        self.IpAddr = ""
        self.Port = ""
        self.Hostnames = []
        self.IpDecimal = ""
        self.Os = ""
        self.Timestamp = ""
        self.Isp = ""
        self.ASN = ""
        self.Domains = []
        self.Org = ""
        self.Data = ""
        self.Loc_City = ""
        self.Loc_RegionCode = ""
        self.Loc_AreaCode = ""
        self.Loc_Latitude = ""
        self.Loc_Longitude = ""
        self.Loc_CountryCode = ""
        self.Loc_CountryName = ""

    def GetCsvHeader(self):
        result_attributes = [attr for attr in self.__dict__.keys() if not attr.startswith('__')]
        csv_header = ""
        for attribute in result_attributes:
            csv_header += attribute + ","
        csv_header += "\n"
        return csv_header

    def GetCsvRow(self):
        csv_rows = ""
        result_values = [attr for attr in self.__dict__.values() ] # if not attr.startswith('__')
        for value in result_values:
            csv_rows += str(value) + ","
        return csv_rows + "\n"

# Shodan service handler
class ShodanService:
    __RESULTS_PER_PAGE=100
    _ShodanApi = None
    _LastResults = []

    def __init__(self, shodan_api):
        self._ShodanApi = shodan.Shodan(shodan_api)

    def PagesNo(self, dork):
        results_no = self.ResultsNo(dork)
        if results_no <= 0:
            return results_no
        return int(results_no / self.__RESULTS_PER_PAGE) + 1

    def ResultsNo(self, dork):
        # Get the amount of results for given dork
        total_pages = 0
        results_number = 0
        try:
            results_number = self._ShodanApi.count(dork)['total']
        except shodan.APIError as e:
            dbgln("Error in fetching results number for dork '{}': {}".format(dork, e), alert=1)
            return -1
        return results_number

    def Search(self, dork):  # type List[ShodanResult]
        # This is where results are stored
        Ret = []
        results_number = self.ResultsNo(dork)
        total_pages = int(results_number / self.__RESULTS_PER_PAGE) + 1
        if results_number <= 0:
            return Ret

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
                        match.ASN = result.get('asn') or ""
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
                        match.Loc_CountryCode = result['location']['country_code']
                        Ret.append(match)
                    except Exception as e:
                        dbgln("Error: failed to parse results for dork '{}': {}".format(dork, e), alert=1)

                # Shodan only allows one request per second
                if total_pages > 1 and (i+1) < total_pages:
                    ##dbgln("[PyShodan] Waiting 1 sec...")
                    time.sleep(1.1)

        except shodan.APIError as e:
            dbgln("Error when fetching results for dork '{}': {}".format(dork, e), alert=1)
        self._LastResults = Ret
        return Ret

    def SaveLastResultsAsCsv(self, filename=None):
        # Get all results as CSV rows
        csv_rows = ""
        for result in self._LastResults:
            csv_rows += result.GetCsvRow() + "\n"
        if filename is None:
            return csv_rows
        # Append header to file
        FileAppend(filename, ShodanResult().GetCsvHeader())
        # Append results to excel file
        FileAppend(filename, csv_rows)
