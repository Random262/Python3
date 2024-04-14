import sqlite3
with sqlite3.connect("hw_4_database.db") as conn:
    cursor = conn.cursor()
    print('----')
    cursor.execute("SELECT COUNT(*) FROM 'salaries' WHERE salary < 5000")
    result = cursor.fetchone()
    print(result[0])
    # 27 человек
    print('----')
    cursor.execute("SELECT AVG(salary) FROM 'salaries'")
    result = cursor.fetchone()
    print(result[0])
    # 9483.36
    print('----')
    cursor.execute("SELECT salary "
                   "FROM ( SELECT salary, "
                   "ROW_NUMBER() OVER (ORDER BY salary) AS id, "
                   "COUNT(*) OVER () AS count FROM salaries ) "
                   "WHERE id IN ((count + 1) / 2, "
                   "(count + 2) / 2)")
    result = cursor.fetchall()
    print(result[0][0], result[1][0])
    # 9983 10085
    print('----')
    cursor.execute("SELECT SUM(salary) FROM (SELECT salary FROM salaries "                    
                   "ORDER BY salary DESC "
                   "LIMIT (SELECT 0.1 * COUNT(salary) FROM salaries))")
    top_10_salary = int(cursor.fetchone()[0])
    cursor.execute("SELECT SUM(salary) FROM salaries")
    total_salary = int(cursor.fetchone()[0])
    result = round(top_10_salary / (total_salary - top_10_salary) * 100, 2)
    print(f'{result}%')
    # 21.87%