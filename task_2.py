import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:

    # Регулярний вираз для пошуку дійсних чисел, оточених пробілами.
    # \d+\.\d+ — знаходить числа з крапкою
    # \d+ — знаходить цілі числа
    pattern = r'\b\d+(?:\.\d+)?\b'
    
    for match in re.finditer(pattern, text):
        # yield повертає значення і зберігає стан функції
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    
    total_sum = 0
    # Ітеруємося по генератору, який повертає функція generator_numbers
    for number in func(text):
        total_sum += number
    return total_sum

# Приклад використання:
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")