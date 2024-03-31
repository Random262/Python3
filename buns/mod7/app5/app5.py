import logging
import logging.config

import logging_tree

from logging_config5 import LOGGING_CONFIG
import sys

import utils5


logger = logging.getLogger('app')
logging.config.dictConfig(LOGGING_CONFIG)


# class LevelBased(logging.Handler):
#     def __init__(self, debug_file, info_file, error_file):
#         super().__init__()
#         self.debug_file = debug_file
#         self.info_file = info_file
#         self.error_file = error_file
#
#     def emit(self, record):
#         if record.levelno == logging.DEBUG:
#             with open(self.debug_file, 'a') as f:
#                 f.write(self.format(record) + '\n')
#         elif record.levelno == logging.INFO:
#             with open(self.info_file, 'a') as f:
#                 f.write(self.format(record) + '\n')
#         elif record.levelno == logging.ERROR:
#             with open(self.error_file, 'a') as f:
#                 f.write(self.format(record) + '\n')
#
#
# def configure_logger():
#     logging.basicConfig(
#         level=logging.DEBUG,
#         handlers=[logging.StreamHandler(sys.stdout)])
#     formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
#     for handler in logging.root.handlers:
#         handler.setFormatter(formatter)
#
#     file_handler = LevelBased('calc_debug.log', 'calc_info.log', 'calc_error.log')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)


def show_list_of_commands() -> None:
    logger.info('Commands list')
    logger.info("Доступные команды:\n"
                "\"+\" - сложение\n"
                "\"-\" - вычитание\n"
                "\"*\" - умножение\n"
                "\"/\" - деление\n"
                "\"^\" - возведение в степень\n")


def get_command_from_user() -> str:
    logger.debug('Getting command from user')
    command: str = input("Введите выражение с пробелами: \n")
    return command


def process_command(command: str) -> tuple[float, float, str] | None:
    logger.debug('Processing command')
    command_split: [str] = command.split()
    if len(command_split) != 3:        
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]    
    return number_1, number_2, operation


def get_result(command: tuple[float, float, str] | None) -> str:
    logger.debug('Getting result')
    if command is None:
        logger.error('Incorrect input')
        return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command    
    result: float = utils5.calculate(number_1, number_2, operation)
    return str(result)


def give_result_to_user(result: str) -> None:
    logger.debug('Giving result to user')
    print(result)


if __name__ == '__main__':
    # configure_logger()
    show_list_of_commands()
    first = sys.stdout
    with open('logging_tree.txt', 'w') as f:
        sys.stdout = f
        logging_tree.printout()
    sys.stdout = first
    while True:        
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)
        
