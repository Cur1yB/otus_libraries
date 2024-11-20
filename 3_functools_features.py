import time
from functools import partial, wraps, lru_cache, reduce, total_ordering
from termcolor import colored
import os
import logging

os.system('clear')

'''
Для работы с кодом необходимо установить все зависимости, указанные в файле requirements.txt

Пример команды:
pip install -r requirements.txt
'''

# Настройка логгера
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Стартовое время для измерения текущего времени
start_time = time.time()

# Функция для получения текущего времени
def current_time():
    return round(time.time() - start_time, 2)

# Функция для логирования сообщений с цветом
def log_message(message, color, level):
    formatted_message = colored(f"[{current_time()}s] {message}", color)
    if level == "info":
        logger.info(formatted_message)
    elif level == "warning":
        logger.warning(formatted_message)
    elif level == "error":
        logger.error(formatted_message)

# Создаем частичные функции для разных уровней логирования
log_info = partial(log_message, color='green', level='info')
log_warning = partial(log_message, color='yellow', level='warning')
log_error = partial(log_message, color='red', level='error')

# Примеры использования логирования
log_info("This is an info message.")
log_warning("This is a warning message.")
log_error("This is an error message.")

# Пример создания замыкания
def multiply_by(x):
    def multiplier(y):
        return x * y
    return multiplier

# Создаем функцию, которая всегда умножает на 3 с использованием замыкания
triple_with_closure = multiply_by(3)
log_info(f"Using closure: 3 * 5 = {triple_with_closure(5)}")
log_info(f"Using closure: 3 * 10 = {triple_with_closure(10)}")

# Пример использования partial
def multiply(x, y):
    return x * y

# Создаем функцию, которая всегда умножает на 3 с использованием partial
triple_with_partial = partial(multiply, 3)
log_info(f"Using partial: 3 * 5 = {triple_with_partial(5)}")
log_info(f"Using partial: 3 * 10 = {triple_with_partial(10)}")

# Пример использования wraps для создания декоратора
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        log_warning(f"Executed {func.__name__} in {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

# Пример вызова декорированной функции
log_info(slow_function())

# Пример использования lru_cache для мемоизации
@timing_decorator
@lru_cache(maxsize=2)
def multiply_thousand(n):
    n ** 1000000
    return n

log_info(f"multiply_thousand: {multiply_thousand(100)}")
log_info(f"multiply_thousand: {multiply_thousand(150)}")

log_info(f"multiply_thousand: {multiply_thousand(100)}")
log_info(f"multiply_thousand: {multiply_thousand(150)}")

log_info(f"multiply_thousand: {multiply_thousand(160)}")
log_info(f"multiply_thousand: {multiply_thousand(100)}")


# Пример использования reduce для суммирования
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
log_info(f"Sum of {numbers}: {sum_result}")

# Пример использования total_ordering для упрощения сравнения объектов
@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Создаем экземпляры класса
alice = Person("Alice", 30)
bob = Person("Bob", 25)

# Проверяем операции сравнения
log_info(f"Alice > Bob: {alice > bob}")
log_info(f"Alice <= Bob: {alice <= bob}")
log_info(f"Alice == Bob: {alice == bob}")
log_info(f"Alice != Bob: {alice != bob}")
