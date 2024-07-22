# Імпортуємо необхідні модулі
import sys
from collections import Counter

# Функція для парсингу логів з рядка
def parse_log_line(line: str) -> dict:
    parts = line.split(" ")
    try:
        # Спроба створити словник з частин рядка
        return {
            "date": parts[0],  # Дата
            "time": parts[1],  # Час
            "level": parts[2],  # Рівень логування
            "message": " ".join(parts[3:]).strip()  # Повідомлення
        }
    except ValueError:
        # Якщо рядок не вдалося розібрати, повертаємо помилку
        return print(f"Неможливо розібрати рядок: {line}")

# Функція для завантаження логів з файлу і додавання їх у список
def load_logs(file_path: str) -> list:
    logs_list = []  
    with open(file_path, "r") as file:  
        for line in file:  
            log = parse_log_line(line)  # Розбираємо кожен рядок
            if log:  
                logs_list.append(log)  # Додаємо лог до списку
    return logs_list

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    # Використовуємо list comprehension для фільтрації
    return [log for log in logs if log["level"] == level.upper()]

# Функція для підрахунку кількості логів за рівнем
def count_logs_by_level(logs: list) -> dict:
    # Використовуємо Counter для підрахунку і повертаємо результат
    return Counter(log["level"] for log in logs)

# Функція для відображення кількості логів за рівнем
def display_logs_count(logs_count: dict):
    # Виводимо заголовок і розділювач
    header = "Рівень логування | Кількість"
    separator = "-" * len(header)
    print(header)
    print(separator)
    # Виводимо кількість логів за кожним рівнем, сортуючи за рівнем
    for level, count in sorted(logs_count.items()):
        print(f"{level:^16} | {count:^9}")
    print(separator)

# Функція для форматування і виводу одного логу
def format_and_print_log(log):
    print(f"{log['date']} {log['time']} {log['level']} - {log['message']}")


if __name__ == "__main__":
    try:
        # Отримуємо шлях до файлу з логами з аргументів командного рядка
        file_path = sys.argv[1]
        # Завантажуємо логи з файлу
        logs = load_logs(file_path)
        # Підраховуємо кількість логів за рівнем
        logs_count = count_logs_by_level(logs)
        # Відображаємо кількість логів за рівнем
        display_logs_count(logs_count)

        # Перевіряємо, чи був переданий другий аргумент (рівень логування)
        if len(sys.argv) > 2:
            # Отримуємо рівень логування з аргументів командного рядка
            level = sys.argv[2]
            # Фільтруємо логи за вказаним рівнем
            filtered_logs = filter_logs_by_level(logs, level)
            # Виводимо інформацію про фільтрацію
            print(f"Деталі логів для рівня {level}:")
            # Виводимо деталі логів певного рівня
            for log in filtered_logs:
                format_and_print_log(log)
    except FileNotFoundError:
        # Обробка випадку, коли файл не знайдено
        print("Файл не знайдено")
        sys.exit(1)
    except IndexError:
        # Обробка випадку, коли не було передано аргументів
        print("Будь ласка, вкажіть шлях до файлу логів як аргумент.")
        sys.exit(1)
    