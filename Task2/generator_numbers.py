# Імпортуємо необхідні модулі
from decimal import Decimal
import re
from typing import Callable

# Функція-генератор для пошуку чисел у тексті
def generator_numbers(text: str):
    # Визначаємо регулярний вираз для пошуку чисел
    pattern = r"\b-?\d+(\.\d+)?\b"
    # Шукаємо всі відповідності у тексті
    for match in re.finditer(pattern, text):
        # Повертаємо знайдені числа, перетворені на Decimal як генератор
        yield Decimal(match.group())

# Функція для підрахунку суми чисел, знайдених у тексті
def sum_profit(text: str, func: Callable[[str], Decimal]) -> Decimal:
    return sum(func(text))