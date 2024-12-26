# Ввод списка из целых элементов.
A = list(map(int, input("Введите целые числа через пробел: ").split()))

# 1. Произведение элементов списка с четными номерами.
product_even_indices = 1
for i in range(0, len(A), 2):  # Индексы: 0, 2, 4, ...
    product_even_indices *= A[i]

# 2. Сумма элементов между первым и последним нулевыми элементами.
first_zero_index = -1
last_zero_index = -1

# Поиск индексов первого и последнего нулевого элемента.
for i in range(len(A)):
    if A[i] == 0:
        if first_zero_index == -1:
            first_zero_index = i
        last_zero_index = i

# Проверяем, есть ли хотя бы два нуля для вычисления суммы.
if first_zero_index != -1 and last_zero_index != -1 and first_zero_index < last_zero_index:
    sum_between_zeros = sum(A[first_zero_index + 1:last_zero_index])
else:
    sum_between_zeros = 0  # Если нулей недостаточно, сумма равна 0.

# Вывод результатов.
print("Произведение элементов с четными номерами:", product_even_indices)
print("Сумма элементов между первым и последним нулевыми элементами:", sum_between_zeros)






