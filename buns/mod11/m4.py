import logging
import random
import threading
import time
from queue import PriorityQueue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(priority={self.priority}). {self.description}"


class Producer(threading.Thread):
    def __init__(self, queue, tasks_cou, event):
        super().__init__()
        self.queue = queue
        self.tasks_cou = tasks_cou
        self.event = event

    def run(self):
        logger.info("Producer: Running")
        for _ in range(self.tasks_cou):
            priority = random.randint(0, 9)
            task = Task(priority, f"sleep({random.random()})")
            self.queue.put((priority, task))
            time.sleep(1)
        self.event.set()
        logger.info("Producer: Done")



class Consumer(threading.Thread):
    def __init__(self, queue, event):
        super().__init__()
        self.queue = queue
        self.event = event

    def run(self):
        logger.info("Consumer: Running")
        self.event.wait()
        while True:
            priority, task = self.queue.get()
            logger.info(f">running {task}")
            time.sleep(random.random())
            self.queue.task_done()
            if self.queue.empty():
                break
        logger.info("Consumer: Done")


def main():
    task_queue = PriorityQueue()
    tasks_cou = random.randint(5, 10)
    event = threading.Event()
    producer = Producer(task_queue, tasks_cou, event)
    consumer = Consumer(task_queue, event)

    producer.start()
    consumer.start()

    consumer.join()
    task_queue.join()
    producer.join()




if __name__ == "__main__":
    main()
