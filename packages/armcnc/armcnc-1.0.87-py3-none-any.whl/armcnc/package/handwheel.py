"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import os
import serial
import binascii
import threading
import configparser

class HandWheel:

    def __init__(self, package):
        self.package = package
        self.serial = None
        self.serial_status = False
        self.serial_task = False
        self.write = "01 03 04 7D 00 07 95 20".encode("utf-8")
        self.read = ""
        self.read_count = 0
        self.joy_speed = {}

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
        print("-> task")
        config = configparser.ConfigParser()
        config.read(self.package.framework.machine.workspace + "/configs/" + self.package.framework.machine.machine_path + "/machine.user")
        items = config.items("HANDWHEEL")
        for key, val in items:
            key = "EXTINFO_" + key.upper()
            self.joy_speed[key] = float(val.strip())
        while True:
            if self.serial_status:
                read_tmp = self.serial.readall()
                self.read = str(binascii.b2a_hex(read_tmp))[6:34]
                self.serial.write(self.write)
                print("-->", self.read)
            self.package.framework.utils.set_sleep(0.1)
