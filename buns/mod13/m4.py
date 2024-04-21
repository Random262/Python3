import sqlite3


def get_ivan_sovin_salary(cur: sqlite3.Cursor) -> int:
    cur.execute("""
    SELECT salary FROM table_effective_manager WHERE name = ?;
    """, ('Иван Совин',))
    res = cur.fetchone()[0]
    return res


def ivan_sovin_the_most_effective(cur: sqlite3.Cursor, name: str, sovin_salary: int) -> None:
    if name != 'Иван Совин':
        cur.execute("""
        SELECT salary FROM table_effective_manager WHERE name = ?;
        """, (name,))
        row = cur.fetchone()

        if row:
            employee_salary = row[0]
            if employee_salary *  1.1 > sovin_salary:
                cur.execute("""
                DELETE FROM table_effective_manager WHERE name = ?;
                """, (name,))
                print(f"Employee {name} has been terminated")
            else:
                new_salary = int(employee_salary * 1.1)
                cur.execute("""
                UPDATE table_effective_manager SET salary = ? WHERE name = ?;
                """, (new_salary, name))
                print(f"Employee {name} salary has been increased to {new_salary}")
        else:
            print(f"Employee {name} is not found in the database")
    else:
        print("Ivan, you can't give yourself a raise")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        sovin_salary = get_ivan_sovin_salary(cursor)
        try:
            while True:
                name = input("Enter the employee's name: ")
                ivan_sovin_the_most_effective(cursor, name, sovin_salary)
                connection.commit()
        except KeyboardInterrupt:
            print('\nYou close the program')



