#
#   python -m unittest discover
#   python -m unittest sqlite_test.py
#

import unittest
import sqlite

class TestSQlite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        # self.db_conn = sqlite.SQLiteConnection('db', 'test.db')        
        # self.db_conn.connect()
        
        cls.db_conn = sqlite.SQLiteConnection()
        cls.db_conn.connectMemory()

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        cls.db_conn.close()
        
    def test_sqlite_version(self):
        db_conn = self.__class__.db_conn
        version = db_conn.getSqliteVersion()
        self.assertEqual(version, '3.42.0')
        
    def test_create_table(self):
        db_conn = self.__class__.db_conn
        db_conn.create_table('''
            CREATE TABLE IF NOT EXISTS tests(
                id     integer,
                name   varchar(50)
            )
        ''')
        count = db_conn.querySingleValue('SELECT count(*) from tests')
        self.assertEqual(count, 0)
        
    def test_insert(self):
        db_conn = self.__class__.db_conn
        for rowcount, lastrowid in db_conn.insert('''
            INSERT INTO tests(id, name)
            VALUES
                  (1, 'one')
                , (2, 'two')
                , (3, 'three')
                , (4, 'four')
                , (5, 'five')
                ;
        '''):
            self.assertEqual(rowcount, 5)
            self.assertEqual(lastrowid, 5)
    
    if __name__ == '__main__':
        unittest.main()