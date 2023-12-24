import sqlite3
import os

DB_FOLDER = os.path.abspath('database')
DATABASE_NAME = f'{DB_FOLDER}/salttiger.db'
TABLE_SALTTIGER_BOOKS = 'salttiger_books'
TABLE_SALTTIGER_BOOKS_DDL = f'''CREATE TABLE IF NOt EXISTS {TABLE_SALTTIGER_BOOKS}(
    id                integer,
    name                varchar(50),
    isbn                nchar(13),
    publish_date        DATE,
    press               varchar(50),
    salttiger_url       varchar(50),
    official_url        varchar(50),
    coverpage_url       varchar(50),
    salttiger_pan_url   varchar(50),
    summary             varchar(250),
    keywords            varchar(50),
    mine_pan_url        varchar(50),
    store_time          DATETIME,
    status              varchar(20)

)'''

TABLE_SALTTIGER_BOOKS_DML_INSERT = f'''
INSERT INTO {TABLE_SALTTIGER_BOOKS}(id, name, press, status) 
values
      (1, '111', '111', 'new')
    , (2, '222', '222', 'new')
    , (3, '333', '333', 'new')
    ;
'''

TABLE_SALTTIGER_BOOKS_DML_SELECT = f'''
select id, name, press, status from {TABLE_SALTTIGER_BOOKS}
'''

def show_sqlite_version(conn):
    cursor = conn.cursor()
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print('SQLite Database Version is: ', record)
    cursor.close


def create_tables(conn):
    cursor = conn.cursor()
    ret = cursor.execute(TABLE_SALTTIGER_BOOKS_DDL)
    print(f'return {ret}')
    conn.commit()
    cursor.close

    print(f'table {TABLE_SALTTIGER_BOOKS} is created')


def insert_records(conn):
    cursor = conn.cursor()
    ret = cursor.execute(TABLE_SALTTIGER_BOOKS_DML_INSERT)
    print(f'return {ret}')
    conn.commit()
    print(f'Record insert successfully into {TABLE_SALTTIGER_BOOKS}')


def read_records(conn):
    cursor = conn.cursor()
    ret = cursor.execute(TABLE_SALTTIGER_BOOKS_DML_SELECT)
    print(f'return {ret}')
    records = cursor.fetchall()
    print('id | name | press | status');
    for r in records:
        print(f'{r[0]}|{r[1]}|{r[2]}|{r[3]}')

    cursor.close


def update_records(conn):
    pass


def delete_records(conn):
    pass

def main():
    if not os.path.exists(DB_FOLDER):
        print(f'create folder {DB_FOLDER}')
        os.mkdir(DB_FOLDER)

    try:
        sqliteConnection = sqlite3.connect(DATABASE_NAME, timeout=20)    
        print('Database created and Successfully Connected to SQLite')

        create_tables(sqliteConnection)
        insert_records(sqliteConnection)
        read_records(sqliteConnection)

        show_sqlite_version(sqliteConnection)

    except sqlite3.Error as error:
        print('Error while connecting to sqlite', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('The sqlite connection is closed')


if __name__ == "__main__":
    main()