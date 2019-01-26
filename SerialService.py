#
#   Filename    : main.py
#   Created on  : Jun, 2018
#   Author      : Alex C.
#   Description : Serial port wrapper
#

from threading import Thread
from Util import *

import time
from serial import *

# After how many seconds should attempt to reconnect
RECONNECT_ATTEMPT_S = 10


class SerialPort:
    def __init__(self, serial_port, baud_rate):
        # User defined config
        self.__port_name = serial_port  # type: str
        self.__baud_rate = baud_rate    # type: int

        # Serial port handler
        self.__hSerial = None   # type: Serial

        # Store last error
        self.__last_error = ""  # type: str

        # Also try to connect
        self.connect()

    def read(self, buff_len):
        if not self.is_alive():
            self.__set_last_error("Port is not open!")
            return -1
        if buff_len <= 0:
            self.__set_last_error("Can't read this length")
            return -1
        try:
            return self.__hSerial.read(buff_len)
        except Exception as e:
            self.__set_last_error("Port is not open!")
            self.__hSerial.close()
            return -1

    def write(self, data):
        if not self.is_alive():
            self.__set_last_error("Port is not open!")
            return -1
        if len(data) == 0:
            self.__set_last_error("Can't read this length")
            return -1
        try:
            return self.__hSerial.write(data)
        except Exception as e:
            self.__set_last_error("Port is not open!")
            self.__hSerial.close()
            return -1

    def is_alive(self):
        if self.__hSerial is None:
            return False
        if self.__hSerial.isOpen() is False:
            return False
        return True

    def connect(self):
        try:
            self.__hSerial = Serial(port=self.__port_name, baudrate=self.__baud_rate, timeout=0)
            return True
        except Exception as e:
            self.__set_last_error(str(e))
            return False

    def close(self):
        try:
            self.__hSerial.close()
            return True
        except Exception as e:
            self.__set_last_error(str(e))
            return False

    def is_data_available(self):
        try:
            return self.__hSerial.in_waiting
        except Exception as e:
            self.__set_last_error(str(e))
            return -1

    def get_last_error(self):
        return self.__last_error

    def __set_last_error(self, err_str):
        self.__last_error = str(err_str)

    def get_port_name(self):
        return self.__port_name

    def get_baud_rate(self):
        return self.__baud_rate

    # This will also keep the connection alive or reconnect in case of lost/broken connection
    def start_listener(self, callback_recv):
        while True:
            if self.__hSerial is not None and self.is_alive() is True:
                # if some data is available
                # if self.is_data_available() > 0:
                    # Read data and pass it via callback function if available
                try:
                    if self.is_data_available() > 0:
                        recv_data = self.read(64)
                        if recv_data == -1:
                            continue
                        else:
                            callback_recv(self, recv_data)

                except Exception as e:
                    self.close()
                    self.__set_last_error(str(e))

                # Reset loop to prevent reconnect
                continue

            # This code is reached if connection to given port failed
            dbg("[SerialService] Attempting to connect to %s with baud %s..." % (str(self.__port_name), str(self.__baud_rate)))
            if self.connect() is False:
                dbg("failed\n", alert=1)
                dbg("[SerialService] ERROR: " + self.get_last_error() + "\n", alert=1)
                dbg("[SerialService] I will try again in " + str(RECONNECT_ATTEMPT_S) + " seconds...\n", alert=1)
                time.sleep(RECONNECT_ATTEMPT_S)
                continue
            dbg("done\n")

    def start_listener_background(self, recv_callback):
        serial_thread = Thread(target=self.start_listener, args=[recv_callback])
        serial_thread.daemon = True
        serial_thread.start()