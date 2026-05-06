import sys
import os

def parse_log_line(line: str) -> dict:
    """Парсить рядок логу у словник."""
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return {}  # Повертаємо порожній словник для некоректних рядків
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу, обробляючи помилки доступу."""
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Відбулася помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує список логів за рівнем (без урахування регістру)."""
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    """Виводить таблицю зі статистикою рівнів."""
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    # Сортуємо для красивого виводу
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count:<10}")

def main():
    # Перевірка наявності хоча б одного аргументу (шлях до файлу)
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    # Виводимо загальну статистику
    display_log_counts(counts)

    # Якщо вказано другий аргумент (рівень логування)
    if len(sys.argv) > 2:
        specific_level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, specific_level)
        
        if filtered:
            print(f"\nДеталі логів для рівня '{specific_level}':")
            for entry in filtered:
                print(f"{entry['date']} {entry['time']} - {entry['message']}")
        else:
            print(f"\nЗаписів для рівня '{specific_level}' не знайдено.")

if __name__ == "__main__":
    main()