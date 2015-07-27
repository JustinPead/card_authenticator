import serial
import logging
import time

class CardReader:

    def __init__(self,logger=logging.getLogger(__name__)):
        self.logger = logger
        #Open COM port
        port = "/dev/ttyACM0" #hardcoded for linux
        self.ser = serial.Serial(port,baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)
        self.logger.info("{p} port established".format(p = port))		

    def get_tag_id(self):
        tag_length = 14
        self.ser.read(self.ser.inWaiting()) #flushing the system.
        time.sleep(0.1)
        while(self.ser.inWaiting()>0):
            self.ser.read(self.ser.inWaiting()) #flushing the system.
            self.logger.debug("Data still coming in - Flushing Loop")
            time.sleep(0.1)
        self.logger.debug("Waiting for Data")
        while(self.ser.inWaiting()<tag_length):
            pass
        value = self.ser.read(tag_length)
        value = value.decode("utf-8")
        value = int(value[1:-3],16)
        self.logger.debug("Value: {v}".format(v = value))
        return value