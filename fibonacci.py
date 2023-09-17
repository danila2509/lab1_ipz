def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Задаємо кількість чисел Фібоначчі, які хочемо обчислити
n = int(input("Введіть кількість чисел Фібоначчі: "))

# Обчислюємо та виводимо числа Фібоначчі
for i in range(n):
    print(fibonacci_recursive(i))
