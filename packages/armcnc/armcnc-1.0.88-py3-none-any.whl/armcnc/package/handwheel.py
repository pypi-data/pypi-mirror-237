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
        self.connect = None
        self.status = False
        self.task = False
        self.write = "01 03 04 7D 00 07 95 20".encode("utf-8")
        self.read = ""
        self.read_count = 0
        self.joy_speed = {}

    def init_serial(self):
        if os.path.exists("/dev/ttyUSB0"):
            self.connect = serial.Serial()
            self.connect.port = "/dev/ttyUSB0"
            self.connect.baudrate = 19200
            self.connect.bytesize = 8
            self.connect.stopbits = serial.STOPBITS_ONE
            self.connect.parity = serial.PARITY_NONE
            try:
                self.connect.open()
                self.task = threading.Thread(name="package_handwheel_task", target=self.task_work)
                self.task.daemon = True
                self.task.start()
                self.status = True
            except Exception as e:
                self.status = False

    def task_work(self):
        print("-> task")
        config = configparser.ConfigParser()
        config.read(self.package.framework.machine.workspace + "/configs/" + self.package.framework.machine.machine_path + "/machine.user")
        items = config.items("HANDWHEEL")
        for key, val in items:
            key = "EXTINFO_" + key.upper()
            self.joy_speed[key] = float(val.strip())
        while True:
            if self.status:
                read_tmp = self.connect.readall()
                self.read = str(binascii.b2a_hex(read_tmp))[6:34]
                self.connect.write(self.write)
                print("-->", self.read)
            self.package.framework.utils.set_sleep(0.1)
