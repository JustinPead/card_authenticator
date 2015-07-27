#!/usr/bin/env python

import time
import logging
from card_reader import CardReader
from student import Student
from access_list import AccessList
from timeout import Timeout
from leds import LEDs

if __name__ == "__main__":
    logging.basicConfig(filename = "./log/file_{t}.log".format(t = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())),
                        level=logging.DEBUG, 
                        format="%(asctime)s:" + logging.BASIC_FORMAT)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s:" + logging.BASIC_FORMAT))
    logging.getLogger().addHandler(console)
    logger = logging.getLogger(__name__)
    logger.info("Student Logger has started")
    while(True):# Loop created for retry purposes
        try:    
            card_reader = CardReader();
            access_list = AccessList("allowed_students.txt",logger.getChild("access_list"));
            with LEDs() as leds:
                while(True):
                    tag_id = card_reader.get_tag_id();
                    with Timeout(seconds=20) as t:
                        leds.orange();
                        student = Student(tag_id, logger.getChild("student"))
                        access_status = access_list.check_allowed(student.info[0])
                        logger.info("Student Number: {name} Access Given: {status}".format(
                            name = student.info[0],
                            status = access_status))
                        if(True==access_status):
                            leds.green();
                        else:
                            leds.red();
        except Exception as e:
            logger.exception(e)