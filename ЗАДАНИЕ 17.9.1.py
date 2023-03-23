array = [int(i) for i in input("Введите числа от 0 до 99: ").split()]


def vst_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


array = vst_sort(array)
print(f'Сортированный по возрастанию список: {array}')
element = int(input('Введите число из списка: '))

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

indx = binary_search(array, element, 0, len(array))
print(f'Индекс введенного элемента: {indx}')

r_ind = indx + 1
l_ind = indx - 1
if element in array:
    if array[l_ind] < array[indx] and array[l_ind] >= 0:
        print(f'Позиция элемента меньше введенного пользователем числа: {l_ind} ')
    else:
        print('Введённое число пользователем наименьшее - начало списка')

    try:
        if array[r_ind] >= array[indx] and array[r_ind] <= array[-1]:
            print(f'Позиция элемента следующего за введёным пользователем числа: {r_ind}')
    except IndexError as error:
        print('Введённое число пользователем наибольшее - конец списка.')
else:
    print(f'В списке нет введенного числа: {element}')






