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
        self.status = False
        self.task = False
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
                self.task = threading.Thread(name="package_handwheel_task", target=self.task_work)
                self.task.daemon = True
                self.task.start()
                self.status = True
            except serial.SerialException as e:
                self.status = False

    def task_work(self):
        config = configparser.ConfigParser()
        config.read(self.package.framework.machine.workspace + "/configs/" + self.package.framework.machine.machine_path + "/machine.user")
        items = config.items("HANDWHEEL")
        for key, val in items:
            key = "EXTINFO_" + key.upper()
            self.joy_speed[key] = float(val.strip())
        joy_count_time = 0
        info_count_time = 0
        while True:
            if self.status:
                if joy_count_time > 1:
                    joy_count_time = 0
                if info_count_time > 60:
                    info_count_time = 0
                info_count_time = info_count_time + 1
                self.read = ""
                self.read_count = self.serial.inWaiting()
                if self.read_count != 0:
                    read_tmp = self.serial.read(self.read_count)
                    self.read = str(binascii.b2a_hex(read_tmp))[6:34]
                self.serial.flushInput()
                joy_count_time = joy_count_time + 1
                self.serial.write(self.write)
                print("->", self.read)
                if self.read_count == 0:
                    continue
            self.package.framework.utils.set_sleep(0.1)
