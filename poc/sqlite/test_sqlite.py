#
#   python -m unittest discover
#   python -m unittest sqlite_test.py
#

import unittest
import sqlite


data = (
    {"id": 1, "name": "one"},
    {"id": 2, "name": "two"},
    {"id": 3, "name": "three"},
    {"id": 4, "name": "four"},
    {"id": 5, "name": "five"},
)


class TestSQlite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # self.db_conn = sqlite.SQLiteConnection('db', 'test.db')
        # self.db_conn.connect()

        cls.db_conn = sqlite.SQLiteConnection()
        cls.db_conn.connectMemory()

    @classmethod
    def tearDownClass(cls):
        cls.db_conn.close()

    def test_1_sqlite_version(self):
        db_conn = self.__class__.db_conn
        version = db_conn.getSqliteVersion()
        self.assertEqual(version, "3.42.0")

    def test_2_create_table(self):
        db_conn = self.__class__.db_conn
        db_conn.create_table(
            """
            CREATE TABLE IF NOT EXISTS tests(
                id     integer,
                name   varchar(50)
            )
        """
        )
        count = db_conn.querySingleValue("SELECT count(*) from tests")
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

    def test_3_insert_many(self):
        db_conn = self.__class__.db_conn
        for rowcount, lastrowid in db_conn.insert_many(
            "INSERT INTO tests(id, name) VALUES(:id, :name)", data
        ):
            self.assertEqual(rowcount, len(data))

    def test_4_query_all(self):
        db_conn = self.__class__.db_conn
        records = db_conn.queryAll("select * from tests")

        self.assertEqual(len(records), len(data))
        for index, record in enumerate(records):
            self.assertEqual(record.id, data[index]["id"])
            self.assertEqual(record.name, data[index]["name"])

    def test_5_update(self):
        db_conn = self.__class__.db_conn
        for rowcount, lastrowid in db_conn.update(
            "UPDATE tests set name = 'tom' where id = 5 "
        ):
            self.assertEqual(rowcount, 1)
            self.assertEqual(lastrowid, 5)

            name = db_conn.querySingleValue("select name from tests where id = 5")
            self.assertEqual(name, "tom")

    def test_6_delete(self):
        db_conn = self.__class__.db_conn
        for rowcount, lastrowid in db_conn.delete("DELETE FROM tests where id = 4"):
            self.assertEqual(rowcount, 1)
            # print(f'delete: rowcount = {rowcount}, lastrowid = {lastrowid}')
            count = db_conn.querySingleValue("SELECT count(id) FROM tests")
            self.assertEqual(count, 4)


if __name__ == "__main__":
    unittest.main()
