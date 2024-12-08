
import psycopg2
import time
import syslog
from psycopg2 import sql
import psycopg2.extras


class millPostDB:
    def __init__(self, database, host, user, password, port, sysLogF=True):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.post_cursor = None
        self.syslogF = sysLogF

    def connectToPostDB(self):
        try:
            self.conn = psycopg2.connect(database=self.database,
                                    host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port)
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: connecting to postgres db => {e}")
            else:
                print(f"Exception: connecting to postgres db => {e}")

    def getCursor(self):
        try:
            self.post_cursor = self.conn.cursor()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: getting cursor => {e}")
            else:
                print(f"Exception: getting cursor => {e}")
        return self.post_cursor

    def delTableData(self, del_sql):
        try:
            self.post_cursor.execute(del_sql)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: delete table data => {e}")
            else:
                print(f"Exception: delete table data => {e}")
        time.sleep(1)
        return True

    def storeTableData(self, store_sql):
        try:
            self.post_cursor.execute(store_sql)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: store table data => {e}")
            else:
                print(f"Exception: store table data => {e}")
        time.sleep(1)
        return True

    def insertRowData(self, insert_sql, row):
        try:
            self.post_cursor.execute(insert_sql, row)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: insert row data => {e}")
            else:
                print(f"Exception: insert row data => {e}")    
                return False
        time.sleep(1)
        return True
    
    def bulkInsertData(self, bulk_sql, bulkData):
        stmt = sql.SQL(bulk_sql)
        try:
            psycopg2.extras.execute_values(self.post_cursor, stmt, bulkData)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:           
                syslog.syslog(syslog.LOG_ERR, f"Exception: bulk insert data => {e}")
            else:
                print(f"Exception: bulk insert data => {e}")
        time.sleep(1)
        return True

    def queryData(self, query_sql):
        try:
            self.post_cursor.execute(query_sql)
            query_row = self.post_cursor.fetchall()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: insert row data => {e}")
            else:
                print(f"Exception: insert row data => {e}")
        time.sleep(1)
        return query_row

    def updateRowData(self, update_sql):
        try:
            self.post_cursor.execute(update_sql)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: update row data => {e}")
            else:
                print(f"Exception: update row data => {e}")    
        time.sleep(1)
        return True

    def updateRowData2(self, update_sql, row):
        try:
            self.post_cursor.execute(update_sql, row)
            self.conn.commit()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: update row data => {e}")
            else:
                print(f"Exception: update row data => {e}")    
        time.sleep(1)
        return True




    def __del__(self):
        try:
            self.post_cursor.close()
            self.conn.close()
        except Exception as e:
            if self.syslogF:
                syslog.syslog(syslog.LOG_ERR, f"Exception: post DB destructor => {e}")
            else:
                print(f"Exception: post DB destructor => {e}")
