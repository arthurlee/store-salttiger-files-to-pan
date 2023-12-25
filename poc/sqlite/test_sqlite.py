#
#   python -m unittest discover
#   python -m unittest sqlite_test.py
#

import unittest
import sqlite

data = (
    {'id': 1, 'name': 'one'},
    {'id': 2, 'name': 'two'},
    {'id': 3, 'name': 'three'},
    {'id': 4, 'name': 'four'},
    {'id': 5, 'name': 'five'}
)


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
        
    # def test_insert(self):
    #     db_conn = self.__class__.db_conn
    #     for rowcount, lastrowid in db_conn.insert('''
    #         INSERT INTO tests(id, name)
    #         VALUES
    #               (1, 'one')
    #             , (2, 'two')
    #             , (3, 'three')
    #             , (4, 'four')
    #             , (5, 'five')
    #             ;
    #     '''):
    #         self.assertEqual(rowcount, 5)
    #         self.assertEqual(lastrowid, 5)
            
    def test_insert_many(self):
        db_conn = self.__class__.db_conn
        for rowcount, lastrowid in db_conn.insert_many('INSERT INTO tests(id, name) VALUES(:id, :name)', data):
            self.assertEqual(rowcount, len(data))
        
            
    def test_query_all(self):
        db_conn = self.__class__.db_conn
        records = db_conn.queryAll('select * from tests')
        
        self.assertEqual(len(records), len(data))
        for index, record in enumerate(records):        
            self.assertEqual(record.id, data[index]['id'])
            self.assertEqual(record.name, data[index]['name'])
        
    
    if __name__ == '__main__':
        unittest.main()