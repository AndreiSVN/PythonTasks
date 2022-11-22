import random
while True:
    nums = input('Введите только числа через пробел:\n')
    check = nums.replace(' ', '')                                   # преобразовываем введенные данные
    if check.isdigit():                                             # и проверяем, что там только цифры
        print('Условие выполнено!')
        break

array = list(map(int, nums.split()))                                    # преобразовываем в список
print(f'Преобразованная в список последовательность чисел: {array}')


def quicksort(seq):                                              # сортировка с помощью рандома
    if len(seq) <= 1:
        return seq
    else:
        q = random.choice(seq)
    l_nums = [n for n in seq if n < q]
    e_nums = [q] * seq.count(q)
    b_nums = [n for n in seq if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


print(f'Отсортированный список:\t{quicksort(array)}')


def binary_search(array, element):                              # двоичный поиск элемента
    left = -1
    right = len(array)
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] >= element:
            right = middle
        else:
            left = middle
    return right


element = int(input('Введите цифру для поиска:\n'))

if element == min(array):                                                   # исключительные случаи
    print(f'Индекс элемента: {min(array) - 1}')
elif element > max(array):
    print('Число больше максимального и не входит в диапазон массива')
elif element < min(array):
    print('Число меньше минимального и не входит в диапазон массива')
else:
    print(f'Индекс элемента меньше введённого: {binary_search(array, element)-1}')
