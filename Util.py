#
#   Filename    : Util.py
#   Created on  : Jun, 2018
#   Author      : Alex C.
#   Description : Util functions
#

import sys
import time
import datetime

# Enable debug messages
DBG_ENB = True


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


def log(str_text):
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S.%f')[:-3]
    formated_str = ("[%s] %s\n" % (st, str_text))
    sys.stdout.write(str(formated_str))
    sys.stdout.flush()


def dbg(dbg_str, alert=0):
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S.%f')[:-3]
    # Print time stamp only if string does not start with '[' or str is capital
    if dbg_str[0].istitle() or dbg_str[0] is '[' or dbg_str[0] is '>':
        sys.stdout.write("[" + st + "] ")

    if alert == 1:
        sys.stdout.write("\033[1;31m")  # Set text to red
        sys.stdout.write(dbg_str)
        sys.stdout.write("\033[0;0m") # Reset text
        sys.stdout.flush()
    else:
        sys.stdout.write(dbg_str)
        sys.stdout.flush()


def dbgln(dbg_str, alert=0):
    dbg(dbg_str + "\n", alert)
