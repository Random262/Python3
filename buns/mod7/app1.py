import logging

from task1 import utils


logger = logging.getLogger('app')


def show_list_of_commands() -> None:
    logger.debug('Commands list')
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
    result: float = utils.calculate(number_1, number_2, operation)    
    return str(result)


def give_result_to_user(result: str) -> None:
    logger.debug('Giving result to user')
    print(result)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    show_list_of_commands()
    while True:        
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)
        
