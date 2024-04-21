import requests
from threading import Thread
import time
import datetime
import logging


def get_timestamp():
    response = requests.get("http://127.0.0.1:8080/timestamp/" + str(int(time.time())))
    return response.text.strip()


def worker(logs):
    for _ in range(20):
        timestamp = get_timestamp()
        date = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        logs.append((timestamp, date))
        time.sleep(1)


def write_logs(logs):
    logs.sort(key=lambda x: x[0])
    with open("logs.txt", "a") as f:
        for log in logs:
            f.write(f"{log[0]} {log[1]}\n")


def main():
    logs = []
    threads = []
    for _ in range(10):
        t = Thread(target=worker, args=(logs,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    write_logs(logs)

    print("Complete")


if __name__ == "__main__":
    logging.basicConfig(filename='logs.txt', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    main()
