import sqlite3
with sqlite3.connect("hw_3_database.db") as conn:
    cursor = conn.cursor()
    print('----')
    tables = ['table_1', 'table_2', 'table_3']
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        result = cursor.fetchone()
        print(result[0])
    # table_1 : 50; table_2 : 50; table_3 : 50;
    print('----')
    cursor.execute("SELECT COUNT(DISTINCT value) FROM 'table_1'")
    result = cursor.fetchone()
    print(result[0])
    # 25 уникальных записей
    print('----')
    cursor.execute("SELECT COUNT (*) "
                   "FROM (SELECT value FROM table_1 "
                   "INTERSECT "
                   "SELECT value FROM table_2)")
    result = cursor.fetchone()
    print(result[0])
    # 18 записей
    print('----')
    cursor.execute("SELECT COUNT (*) "
                   "FROM (SELECT value FROM table_1 "
                   "INTERSECT "
                   "SELECT value FROM table_2 "
                   "INTERSECT "
                   "SELECT value FROM table_3)")
    result = cursor.fetchone()
    print(result[0])
    # 12 записей
