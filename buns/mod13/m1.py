import sqlite3


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    c.execute("""
            SELECT COUNT(*) 
            FROM table_truck_with_vaccine 
            WHERE truck_number = ? 
            AND (temperature_in_celsius < -20 OR temperature_in_celsius > -16)
            """, (truck_number,))
    hours_outside_range = c.fetchone()[0]
    return hours_outside_range >= 3


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cur = conn.cursor()
        print(check_if_vaccine_has_spoiled(cur, "а000ех147"))
