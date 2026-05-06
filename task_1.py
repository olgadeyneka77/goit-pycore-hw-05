def caching_fibonacci():
    # 1. Створюємо кеш (у зовнішній функції)
    cache = {}

    def fibonacci(n):
        # 2. Всі ці рядки МАЮТЬ мати додатковий відступ (4 пробіли)
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # 3. Повертаємо функцію 
    return fibonacci

# Використання:
fib = caching_fibonacci()
print(fib(10))