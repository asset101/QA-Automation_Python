def check_number(number):
    if number > 7:
        print("Привет")

def check_name(name):
    if name == "Вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")

def filter_multiples_of_three(array):
    result = [x for x in array if x % 3 == 0]
    print(result)

# Примеры использования:
number = int(input("Введите число: "))  # Например, 10
check_number(number)

name = input("Введите имя: ")  # Например, Вячеслав
check_name(name)

array = list(map(int, input("Введите числовой массив через пробел: ").split()))  # Например, 1 2 3 4 5 6 7 8 9
filter_multiples_of_three(array)
