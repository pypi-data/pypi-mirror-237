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
            try:
                self.connect = serial.Serial("/dev/ttyUSB0", 19200)
                self.task = threading.Thread(name="package_handwheel_task", target=self.task_work)
                self.task.daemon = True
                self.task.start()
                self.status = True
            except Exception as e:
                self.status = False

    def task_work(self):
        print("1-> task")
        config = configparser.ConfigParser()
        config.read(self.package.framework.machine.workspace + "/configs/" + self.package.framework.machine.machine_path + "/machine.user")
        items = config.items("HANDWHEEL")
        for key, val in items:
            key = "EXTINFO_" + key.upper()
            self.joy_speed[key] = float(val.strip())
        joy_count_time = 0
        while True:
            if self.status:
                self.read_count = self.connect.inWaiting()
                print("2-->", self.read_count)
                if self.read_count != 0:
                    read_tmp = self.connect.read(self.read_count)
                    self.read = str(binascii.b2a_hex(read_tmp))[6:34]
                self.connect.flushInput()
                joy_count_time = joy_count_time + 1
                self.connect.write(self.write)
                print("3--->", self.read)
            self.package.framework.utils.set_sleep(0.5)
