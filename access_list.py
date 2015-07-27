import logging

class AccessList:
    def __init__(self,file_name,logger = logging.getLogger(__name__)):
        self.logger = logger;
        with open(file_name) as f:
            self.students = f.readlines()
        self.students = [student.strip() for student in self.students]
        self.students = [student.upper() for student in self.students]	
        self.logger.info("Read {l} students".format(l = len(self.students)))
        
    def check_allowed(self, student_number):
        student_number = student_number.upper()
        student_number = student_number.strip()
        if(student_number in self.students):
            return True
        else:
            return False