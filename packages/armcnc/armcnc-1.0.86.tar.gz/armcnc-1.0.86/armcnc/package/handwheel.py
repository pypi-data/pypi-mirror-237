"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import os
import serial
import binascii
import threading

class HandWheel:

    def __init__(self, package):
        self.package = package
        self.serial = None
        self.serial_status = False
        self.serial_task = False
        self.write = "01 03 04 7D 00 07 95 20".encode("utf-8")
        self.read = ""
        self.read_count = 0

    def init_serial(self):
        if os.path.exists("/dev/ttyUSB0"):
            self.serial = serial.Serial()
            self.serial.port = "/dev/ttyUSB0"
            self.serial.baudrate = 19200
            self.serial.bytesize = 8
            self.serial.stopbits = serial.STOPBITS_ONE
            self.serial.parity = serial.PARITY_NONE
            try:
                self.serial.open()
                self.serial_task = threading.Thread(name="package_handwheel_task", target=self.task)
                self.serial_task.daemon = True
                self.serial_task.start()
                self.serial_status = True
            except Exception as e:
                self.serial_status = False

    def task(self):
        while True:
            if self.serial_status:
                self.read_count = self.serial.inWaiting()
                if self.read_count != 0:
                    read_tmp = self.serial.read(self.read_count)
                    self.read = str(binascii.b2a_hex(read_tmp))[6:34]
                self.serial.flushInput()
                self.serial.write(self.write)
                print("-->", self.read)
            self.package.framework.utils.set_sleep(0.1)
