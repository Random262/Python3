import math
import logging


logger = logging.getLogger('utils')


def calculate(a: float, b: float, operation: str) -> float:
    logger.info(f'{operation} with {a} and {b}')
    match operation:
        case "+":
            return _addition(a, b)
        case "-":
            return _subtraction(a, b)
        case "*":
            return _multiplication(a, b)
        case "/":
            return _division(a, b)
        case "^":
            return _pow(a, b)


def _addition(a: float, b: float) -> float:    
    result: float = a + b
    logger.info(f'Addition: {result}')
    return result


def _subtraction(a: float, b: float) -> float:    
    result: float = a - b
    logger.info(f'Subtraction: {result}')
    return result


def _multiplication(a: float, b: float) -> float:    
    result: float = a * b
    logger.info(f'Multiplication: {result}')
    return result


def _division(a: float, b: float) -> float:    
    result: float = a / b
    logger.info(f'Division: {result}')
    return result


def _pow(a: float, b: float) -> float:    
    result: float = math.pow(a, b)
    logger.info(f'Pow: {result}')
    return result
