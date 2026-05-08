def caching_fibonacci():
    # 1. Створюємо кеш із базовими значеннями
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        # 2. Захист від від’ємних чисел
        if n < 0:
            return 0
        
        # 3. Перевірка кешу через .get()
        result = cache.get(n)
        if result is not None:
            return result

        # 4. Якщо в кеші немає — обчислюємо і записуємо
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    # 5. Повертаємо функцію як об'єкт
    return fibonacci

# Використання:
fib = caching_fibonacci()
print(fib(10))   # 55
print(fib(15))   # 610
print(fib(-5))   # 0