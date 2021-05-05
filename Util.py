#
#   Filename    : Util.py
#   Created on  : Jun, 2018
#   Author      : Alex C.
#   Description : Util functions
#
import json
import re
import sys
import time
import datetime
import socket

# Enable debug messages
DBG_ENB = True

# ANSI colors for fancy printing
class AnsiColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ByteToHex(byteStr):
    hex = []
    for aChar in byteStr:
        hex.append("%02X " % ord(aChar))
    return ''.join(hex).strip()


def HexToByte(hexStr):
    bytes = []
    hexStr = ''.join(hexStr.split(" "))
    for i in range(0, len(hexStr), 2):
        bytes.append(chr(int(hexStr[i:i + 2], 16)))
    return ''.join(bytes)


def FileGetContent(filename):
    with open(filename, 'r') as filehandle:
        data = filehandle.read()
        return data


def FileGetLines(filename):
    return [line.strip() for line in open(filename)]


def FileWrite(filename, content):
    with open(filename, 'w') as filehandle:
        filehandle.write(content)


def FileAppend(filename, content):
    with open(filename, 'a') as filehandle:
        filehandle.write(content)


def FileExists(filename):
    import os
    exists = os.path.exists(filename)
    if exists:
        return True
    else:
        return False


def Timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def Datetime():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


def ExtractIPv4(input_str):
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    result = pattern.search(input_str)
    if result:
        return result[0]
    else:
        return None


def ContainIPv4(input_str):
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    if pattern.search(input_str):
        return True
    else:
        return False


def IsValidIPv4(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def IsValidIPv6(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def log(str_text):
    st = Timestamp()
    formatted_str = ("[%s] %s\n" % (st, str_text))
    sys.stdout.write(str(formatted_str))
    sys.stdout.flush()


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


def dbgln(dbg_str, alert=0):
    dbg(dbg_str + "\n", alert)


def dbg_timestamp(dbg_str, alert=0, timestamp = 0):
    st = Timestamp()
    # Print time stamp only if string does not start with '[' or str is capital
    if timestamp:
        sys.stdout.write("[" + st + "] ")

    if alert == 1:
        sys.stdout.write("\033[1;31m")  # Set text to red
        sys.stdout.write(dbg_str)
        sys.stdout.write("\033[0;0m")   # Reset text
    else:
        sys.stdout.write(dbg_str)
    sys.stdout.flush()


def RemoveHtmlTags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def DownloadWebPage(page_url, timeout=10):
    import requests
    import html

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(page_url, headers=headers, timeout=timeout)
        return response.text
    except:
        return "error_exception"


def GetIpInfo(addr):
    ip_info_link = "https://rest.db.ripe.net/search.json?query-string=%s&flags=no-referenced&flags=no-irt&source=RIPE" % str(addr)
    html = DownloadWebPage(ip_info_link)

    result = {}
    result['org'] = "unknown"
    result['org_key'] = "unknown"
    result['role_key'] = "unknown"
    result['asn'] = "unknown"
    result['country'] = "unknown"
    result['ripe_link'] = ip_info_link
    #result['full_json_info'] = html

    # Parse ASN
    jsn = json.loads(html)
    if 'objects' not in jsn:
        return ""

    base_objects = jsn['objects']['object']
    for obj in base_objects:
        attributes = obj['attributes']['attribute']
        # Loop through each attribute until all fields are found
        for atr in attributes:
            atr_name = str(atr['name'])
            atr_val = str(atr['value'])
            # Check if current attribute is the one we are looking for
            if (atr_name == "descr"):
                if result['org'] == "unknown":
                    result['org'] = atr_val
                # else:
                #     result['org'] += ", " + atr_val
            if (atr_name == "origin") and (result['asn'] == "unknown"):
                result['asn'] = atr_val
            if (atr_name == "country") and (result['country'] == "unknown"):
                result['country'] = atr_val

            # Read organization role key
            if (('referenced-type' in atr) and (atr['referenced-type'] == "organisation")) and (result['org_key'] == "unknown"):
                result['org_key'] = atr_val

            if ('link' in atr)  and ('type' in atr['link']) and (atr['link']['type'] == "locator") and (result['role_key'] == "unknown"):
                result['role_key'] = atr_val

    # Read original organization name directly if key already read
    if result['org_key'] != "unknown":
        org_res = GetRipeIpOrganizationName(result['org_key'])
        if org_res:
            result['org'] = org_res
    elif result['role_key'] != "unknown":
        res = GetRipeOrganizationId(result['role_key'])
        if res:
            result['org_key'] = res
            org_res = GetRipeIpOrganizationName(result['org_key'])
            if org_res:
                result['org'] = org_res

    return result


def GetRipeOrganizationId(ripe_role_key):
    request_link = "https://rest.db.ripe.net/ripe/role/%s.json" % ripe_role_key
    html = DownloadWebPage(request_link)

    # Parse response
    jsn = json.loads(html)

    if 'objects' not in jsn:
        return ""

    base_objects = jsn['objects']['object']
    for obj in base_objects:
        attributes = obj['attributes']['attribute']
        # Loop through each attribute until all fields are found
        for atr in attributes:
            atr_name = str(atr['name'])
            atr_val = str(atr['value'])
            if ('referenced-type' in atr) and (atr['referenced-type'] == "organisation") or ("admin-c" in atr_name):
                return atr_val


def GetRipeIpOrganizationName(ripe_org_key):
    request_link = "https://rest.db.ripe.net/ripe/organisation/%s.json" % ripe_org_key
    html = DownloadWebPage(request_link)

    # Parse response
    jsn = json.loads(html)

    if 'objects' not in jsn:
        return ""

    base_objects = jsn['objects']['object']
    for obj in base_objects:
        attributes = obj['attributes']['attribute']
        # Loop through each attribute until all fields are found
        for atr in attributes:
            atr_name = str(atr['name'])
            atr_val = str(atr['value'])
            if atr_name == "org-name":
                return atr_val

