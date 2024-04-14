import logging
import random
import threading
import time

TOTAL_TICKETS = 10
SOLD_TICKETS = 0
FILL = 7
SEATINGS = 50
MORE = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        global SOLD_TICKETS
        global MORE
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                if TOTAL_TICKETS > FILL or not MORE:
                    self.tickets_sold += 1
                    SOLD_TICKETS += 1
                    TOTAL_TICKETS -= 1
                    logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')
        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore

    def run(self):
        global TOTAL_TICKETS
        global SOLD_TICKETS
        global MORE
        while True:
            with (self.sem):
                if TOTAL_TICKETS <= FILL:
                    if SOLD_TICKETS + FILL * 3 < SEATINGS:
                        self.refill(2 * FILL)
                    elif MORE:
                        self.refill(SEATINGS - SOLD_TICKETS - FILL)
                        MORE = False

            time.sleep(1)

    def refill(self, COU):
        global TOTAL_TICKETS
        logger.info("Director is refilling tickets")
        TOTAL_TICKETS += COU
        logger.info(f"Tickets refilled to {TOTAL_TICKETS}")

def main():
    global SOLD_TICKETS
    semaphore = threading.Semaphore()
    sellers = []
    director = Director(semaphore)

    for _ in range(4):
        seller = Seller(semaphore)
        sellers.append(seller)

    director.start()
    for seller in sellers:
        seller.start()

    director.join()
    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()
