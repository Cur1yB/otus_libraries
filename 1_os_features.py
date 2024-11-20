import os
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


# Очистка терминала
def clear_terminal():
    os.system("clear")


# Функция для создания директории проекта
def create_project_directory(project_name):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        logger.info(f"Директория '{project_name}' создана.")
    else:
        logger.info(f"Директория '{project_name}' уже существует.")
    return project_name


# Функция для создания файлов в проектной директории
def create_files(project_dir):
    files = ["index.html", "main.css", "app.js"]
    for file in files:
        file_path = os.path.join(project_dir, file)
        with open(file_path, "w") as f:
            f.write(f"// {file}")
        logger.info(f"Файл '{file}' создан в '{project_dir}'.")
    return files


# Функция для переименования файлов
def rename_files(project_dir, files):
    for file in files:
        old_file_path = os.path.join(project_dir, file)
        new_file_path = os.path.join(project_dir, f"new_{file}")
        os.rename(old_file_path, new_file_path)
        logger.info(f"Файл '{file}' переименован в 'new_{file}'.")


# Функция для проверки существования файлов и директории
def check_existence(project_dir, files):
    for file in files:
        new_file_path = os.path.join(project_dir, f"new_{file}")
        if os.path.exists(new_file_path):
            logger.info(f"Файл '{new_file_path}' существует.")
        else:
            logger.warning(f"Файл '{new_file_path}' не найден.")

    if os.path.exists(project_dir):
        logger.info(f"Директория '{project_dir}' существует.")
    else:
        logger.warning(f"Директория '{project_dir}' не найдена.")


# Функция для получения и изменения текущей рабочей директории
def get_and_change_directory(project_dir):
    current_dir = os.getcwd()
    logger.info(f"Текущая рабочая директория: {current_dir}")
    os.chdir(project_dir)
    logger.info(f"Рабочая директория изменена на: {os.getcwd()}")


# Функция для удаления файла
def delete_file(file_to_delete):
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        logger.info(f"Файл '{file_to_delete}' удален.")
    else:
        logger.warning(f"Файл '{file_to_delete}' не найден.")


# Функция для удаления пустой директории
def delete_empty_directory(dir_to_delete):
    if os.path.exists(dir_to_delete):
        os.rmdir(dir_to_delete)
        logger.info(f"Директория '{dir_to_delete}' удалена.")
    else:
        logger.warning(f"Директория '{dir_to_delete}' не найдена.")


# Функция для обхода дерева директорий
def walk_directory():
    for root, dirs, files in os.walk("my_new_project"):
        logger.info(f"Текущая директория: {root}")
        logger.info(f"Подкаталоги: {dirs}")
        logger.info(f"Файлы: {files}")


# Функция для получения размера файла
def get_file_size(project_dir):
    file_path = os.path.join(project_dir, "new_index.html")
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        logger.info(f"Размер файла '{file_path}': {file_size} байт")
    else:
        logger.warning(f"Файл '{file_path}' не найден.")


# Функция для получения абсолютного пути
def get_absolute_path():
    relative_path = "new_main.css"
    absolute_path = os.path.abspath(relative_path)
    logger.info(f"Абсолютный путь: {absolute_path}")


# Функция для создания лог-файла
def create_log_file(project_dir):
    log_dir = os.path.join(project_dir, "logs")
    logger.info(log_dir)
    os.makedirs(log_dir, exist_ok=True)  # Создание всех промежуточных директорий
    log_file = os.path.join(log_dir, "setup.log")
    os.system(f'echo "Setup log created on $(date)" > {log_file}')
    logger.info(f"Файл логов '{log_file}' создан.")
    return log_file


# Функция для вывода содержимого директории
def list_directory_contents():
    result = os.popen("ls").read()
    logger.info("Список файлов и директорий в текущем каталоге:")
    logger.info(result)


# Функция для чтения лог-файла
def read_log_file(log_file):
    log_content = os.popen(f"cat {log_file}").read()
    logger.info(f"Содержимое лог-файла '{log_file}':")
    logger.info(log_content)


# Основной блок программы
DIR_NAME = "new_directory"

if __name__ == "__main__":
    # Очищаем терминал
    clear_terminal()

    # Создаем директорию проекта
    project_dir = create_project_directory(DIR_NAME)
'''
    # Создаем файлы в директории проекта
    files = create_files(project_dir)

    # Переименовываем созданные файлы
    rename_files(project_dir, files)

    # Проверяем существование файлов и директории
    check_existence(project_dir, files)

    # Получаем текущую рабочую директорию и меняем ее на директорию проекта
    get_and_change_directory(project_dir)

    # Удаляем ненужный файл, если он существует
    delete_file("unwanted_file.txt")

    # Удаляем пустую директорию, если она существует
    delete_empty_directory("empty_directory")

    # Обходим дерево директорий и выводим его содержимое
    walk_directory()

    # Получаем размер файла и выводим его
    get_file_size(project_dir)

    # Получаем и выводим абсолютный путь к файлу
    get_absolute_path()

    # Создаем лог-файл и записываем в него информацию
    log_file = create_log_file(project_dir)

    # Выводим содержимое текущей директории
    list_directory_contents()

    # Читаем и выводим содержимое лог-файла
    read_log_file(log_file)'''
