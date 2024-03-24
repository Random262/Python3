import getpass
import logging
import re

logger = logging.getLogger("password_checker")


def console_handler():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)


def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль")
        return False

    try:
        if re.match(r'^[a-zA-Z0-9]+$', password):
            logger.info("Вы вошли в skillbox")
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)
    logger.info("Неверный пароль")
    return False


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="stderr.txt",
        format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
    console_handler()
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error("Пользователь трижды ввел неправильный пароль!")
    exit(1)