import logging
import pymssql
import _mssql
import os

class Student:
    def __init__ (self, tag_id, logger = logging.getLogger(__name__)):
        self.logger = logger;
        self.tag_id = tag_id
        self.establish_connection()
        self.get_student_info()

    def establish_connection(self):
        self.conn = pymssql.connect(os.environ["ENDPOINT"],os.environ["USERNAME"],os.environ["PASSWORD"], 'DB400_reports')#These are private environment variables
        self.cursor = self.conn.cursor()
        
    def get_student_info(self):
        sqlquery = "EXEC DB400_reports.dbo.GET_TAG_DETAILS @TAG_CODE = {t}".format(t = self.tag_id)
        print(sqlquery)
        self.cursor.execute(sqlquery)
        info = self.cursor.fetchone()
        self.logger.debug(info)
        self.info = info
