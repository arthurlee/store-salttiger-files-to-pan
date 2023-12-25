import sqlite3
import os
import record


class SQLiteConnection:
    def __init__(self, folder=None, database=None):
        self.db_folder = folder
        self.database_file = database
        self.connection = None

    def mkdbFolderIfNotExist(self):
        if self.db_folder and not os.path.exists(self.db_folder):
            print(f"create folder {self.db_folder}")
            os.mkdir(self.db_folder)

    def getFullDatabaseFile(self):
        return os.path.abspath(os.path.join(self.db_folder, self.database_file))

    # connect to the database
    def connect(self, timeout=20):
        self.mkdbFolderIfNotExist()

        full_dbname = self.getFullDatabaseFile()
        print(f"full database name = {full_dbname}")

        self.connection = sqlite3.connect(full_dbname, timeout=timeout)
        
    def connectMemory(self):
        self.connection = sqlite3.connect(':memory:')

    # close the connection
    def close(self):
        self.connection.close()
        self.connection = None
        
    def db_execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        yield cursor
        self.connection.commit()

    def convertToRecords(self, rows, names):
        records = []
        for row in rows:
            r = record.Record()
            for index,name in enumerate(names):
                r[name] = row[index]
            records.append(r)
            
        print(records)
        return records

    def queryAll(self, sql):
        for cursor in self.db_execute(sql):
          rows = cursor.fetchall()
          names = list(map(lambda x: x[0], cursor.description))
          return self.convertToRecords(rows, names)
      
    # query the single record
    def querySingle(self, sql):
        for cursor in self.db_execute(sql):
          record = cursor.fetchone()
          return record
    
    # query the single value
    def querySingleValue(self, sql):
        return self.querySingle(sql)[0]
    
      
    def getSqliteVersion(self):
        version = self.querySingleValue("select sqlite_version();")
        print(f"SQLite Database Version is: {version}")
        return version
    
    def execute(self, sql):
        for cursor in self.db_execute(sql):
          print(f'execute: rowcount {cursor.rowcount}, lastrowid {cursor.lastrowid}')        
          yield cursor.rowcount, cursor.lastrowid
          
    def create_table(self, sql):
        for rowcount,lastrowid in self.execute(sql):
            print(f'create table: rowcount {rowcount}, lastrowid {lastrowid}')        
        
    def insert(self, sql):
        yield from self.execute(sql)
        
    def update(self, sql):
        yield from self.execute(sql)
        
    def delete(self, sql):
        yield from self.execute(sql)


def main():
    try:
        sqlite = SQLiteConnection('db', 'test.db')
        sqlite.connect()
        sqlite.getSqliteVersion()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqlite:
            sqlite.close()
            print("The sqlite connection is closed")


if __name__ == "__main__":
    main()
