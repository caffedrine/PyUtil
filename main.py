#
#   Filename    : main.py
#   Created on  : Jun, 2018
#   Author      : Alex C
#   Description : RPI Testbench
#

# Standard modules
import SerialService
from threading import Thread
from time import sleep
import sys
import os

# Owned modules
from SerialService import *
from NetworkService import *
from Sockets import *
from Util import *


def tcp_recv_callback(client, data):
    dbg("[" + str(client.get_address()) + ":" + str(client.get_port()) + "] " + str(data) + "\n")


def serial_recv_callback(port, data):
    dbg("[" + str(port.get_port_name()) + " RECV] " + str(data) + "\n")
    if port.write(data) == -1:
        print("Error: " + port.get_last_error())


# Main function
def main():
    # Start TCP networking on port 1337
    start_networking_task_background(1337, tcp_recv_callback)

    # Start serial port service
    # serial = SerialPort("/dev/ttyS0", 9600)
    # serial.start_listener_background(serial_recv_callback)

    while True:
        time.sleep(5)
        # if serial.write("fff!") != -1:
        #     dbg("[" + str(serial.get_port_name()) + " SEND] !\n")
        # else:
        #     dbg("Failed: " + serial.get_last_error())


# Execute main function
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print >> sys.stderr, 'Keyboard interrupt detected! Program will end now... '
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
