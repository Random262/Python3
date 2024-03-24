import getpass
import logging
import re

logger = logging.getLogger("password_checker")

library = set()


def make_lib():
    global library
    with open('words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) > 4:
                library.add(word)


def is_strong_password(password):
    global library
    password_words = re.findall(r'\w{5,}', password.lower())
    for w in password_words:
        if w in library:
            return False
    return True


def console_handler():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)


def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password = input()

    if not password:
        logger.warning("Вы ввели пустой пароль")
        return False

    try:
        if is_strong_password(password):
            logger.info("Вы создали пароль")
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)
    logger.info(f"Ваш пароль {password} слабый")
    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="stderr.txt",
        format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
    console_handler()
    logger.info("Вы пытаетесь создать пароль для Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")
    make_lib()
    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error("Пользователь трижды ввел неправильный пароль!")
    exit(1)