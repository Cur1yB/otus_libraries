import itertools
import time
import os
import logging

os.system("clear")

# Настройка стандартного логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


# Генерация последовательных идентификаторов с использованием itertools.count
def generate_ids():
    logger.info("Генерация последовательных идентификаторов:")
    id_generator = itertools.count(start=1, step=1)
    for _ in range(5):
        logger.info(f"ID: {next(id_generator)}")


# Циклическое выполнение задач с использованием itertools.cycle
def cycle_tasks():
    def task_1():
        logger.info('task1')

    def task_2():
        logger.info('task2')
    
    def task_3():
        logger.info('task3')
    
    logger.info("Циклическое выполнение задач:")
    tasks = itertools.cycle([task_1, task_2, task_3])
    for _ in range(6):
        next(tasks)()


# Создание повторяющихся сообщений с использованием itertools.repeat
def repeat_messages(iterations):
    logger.info("Повторяющиеся сообщения:")
    repeater = itertools.repeat("Повторяйте это сообщение", iterations)
    for item in repeater:
        logger.info(f"Сообщение: {item}")


# Генерация тестовых случаев с комбинациями полей с использованием itertools.combinations
def generate_test_cases():
    logger.info("Тестовые случаи с комбинациями полей:")
    fields = ["username", "password", "email"]
    required_fields = itertools.combinations(fields, 2)
    for combination in required_fields:
        logger.info(f"Комбинация: {combination}")


# Фильтрация данных с использованием itertools.dropwhile и itertools.takewhile
def filter_data():
    logger.info("Фильтрация данных с использованием dropwhile и takewhile:")
    data = [1, 2, 3, 4, 5, 6]

    logger.info("Данные после dropwhile (x < 4):")
    dropped_data = itertools.dropwhile(lambda x: x < 4, data)
    for item in dropped_data:
        logger.info(f"Элемент: {item}")

    logger.info("Данные после takewhile (x < 4):")
    taken_data = itertools.takewhile(lambda x: x < 4, data)
    for item in taken_data:
        logger.info(f"Элемент: {item}")


# Объединение нескольких итераторов с использованием itertools.chain
def combine_iterators():
    logger.info("Объединение нескольких итераторов:")
    iter1 = [1, 2, 3]
    iter2 = ["A", "B", "C"]
    iter3 = 'string'
    combined = itertools.chain(iter1, iter2, iter3)
    logger.info(combined)
    logger.info(list(combined))


# Картезианское произведение итераторов с использованием itertools.product
def demonstrate_product():
    logger.info("Картезианское произведение итераторов:")
    iter1 = [1, 2]
    iter2 = ["A", "B"]
    product_result = itertools.product(iter1, iter2)
    for item in product_result:
        logger.info(f"Комбинация: {item}")


# Генерация перестановок элементов с использованием itertools.permutations
def demonstrate_permutations():
    logger.info("Перестановки элементов:")
    elements = ["A", "B", "C"]
    permutation_result = itertools.permutations(elements, 2)
    logger.info(f"Перестановки: {list(permutation_result)}")


# Накопление значений с использованием itertools.accumulate
def demonstrate_accumulate():
    logger.info("Пример accumulate (накопительная сумма):")
    numbers = [1, 2, 3, 4, 5]
    accumulate_result = itertools.accumulate(numbers)
    for item in accumulate_result:
        logger.info(f"Накопленная сумма: {item}")

    logger.info("Пример accumulate (накопительное произведение):")
    accumulate_result = itertools.accumulate(numbers, lambda x, y: x * y)
    for item in accumulate_result:
        logger.info(f"Накопленное произведение: {item}")


# Объединение итераторов разной длины с использованием itertools.zip_longest
def demonstrate_zip_longest():
    logger.info("Пример zip_longest:")
    iter1 = [1, 2, 3]
    iter2 = ["A", "B"]
    zip_longest_result = itertools.zip_longest(iter1, iter2, fillvalue="?")
    logger.info(f"Комбинации: {list(zip_longest_result)}")


# Группировка данных с использованием itertools.groupby
def demonstrate_groupby():
    logger.info("Пример groupby:")
    group_data = sorted(
        [
            ("fruit", "apple"),
            ("fruit", "banana"),
            ("vegetable", "carrot"),
            ("fruit", "orange"),
        ]
    )
    for key, group in itertools.groupby(group_data, lambda x: x[0]):
        group_items = [item[1] for item in group]
        logger.info(f"{key}: {group_items}")


# Создание срезов итератора с использованием itertools.islice
def demonstrate_islice():
    logger.info("Пример islice:")
    count_numbers = itertools.count(1)
    islice_result = itertools.islice(
        count_numbers, 5, 15, 2
    )  # Срез от 5 до 15 с шагом 2
    for item in islice_result:
        logger.info(f"Элемент: {item}")


# Дублирование итераторов с использованием itertools.tee
def demonstrate_tee():
    logger.info("Пример tee:")
    numbers = [1, 2, 3, 4]
    iter1, iter2 = itertools.tee(numbers, 2)

    logger.info("Первый итератор:")
    for item in iter1:
        logger.info(f"Элемент: {item}")

    logger.info("Второй итератор:")
    for item in iter2:
        logger.info(f"Элемент: {item}")


# Генерация комбинаций с повторением с использованием itertools.combinations_with_replacement
def demonstrate_combinations_with_replacement():
    logger.info("Комбинации с повторением:")
    elements = ["A", "B"]
    combinations_with_replacement_result = itertools.combinations_with_replacement(
        elements, 2
    )
    for item in combinations_with_replacement_result:
        logger.info(f"Комбинация: {item}")


if __name__ == "__main__":
    # Генерация последовательных идентификаторов
    generate_ids()

    ## Циклическое выполнение задач
    #cycle_tasks()

    ## Повторение сообщений определенное количество раз
    #repeat_messages(5)

    ## Генерация тестовых случаев с комбинациями полей
    #generate_test_cases()

    ## Фильтрация данных с использованием dropwhile и takewhile
    #filter_data()

    ## Объединение нескольких итераторов в один
    #combine_iterators()

    ## Картезианское произведение итераторов
    #demonstrate_product()

    ## Генерация перестановок элементов
    #demonstrate_permutations()

    ## Накопление значений (сумма и произведение)
    #demonstrate_accumulate()

    ## Объединение итераторов разной длины
    #demonstrate_zip_longest()

    ## Группировка данных
    #demonstrate_groupby()

    ## Создание срезов итератора
    #demonstrate_islice()

    ## Дублирование итераторов
    #demonstrate_tee()

    ## Генерация комбинаций с повторением
    #demonstrate_combinations_with_replacement()