import csv
import sqlite3


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            car_number, timestamp = row
            c.execute("""
                DELETE FROM table_fees
                WHERE truck_number = ? AND timestamp = ?
            """, (car_number, timestamp))

    print("Complete")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
        conn.commit()
