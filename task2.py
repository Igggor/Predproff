def quick_sort(alist, start, end):
    """
    Быстрая сортировка для массива
    :param alist: Изначльный список
    :param start: Позиция старта
    :param end: Позиция конца
    :return: Отсортированный массив
    """
    i = start
    j = end
    arr = alist[(start + end) // 2][1]
    while True:
        while alist[i][1] < arr:
            i += 1
        while alist[j][1] > arr:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
        else:
            break
    if start < j:
        quick_sort(alist, start, j)
    if i < end:
        quick_sort(alist, i, end)


def sort_potions() -> None:
    """
    Функция для получения списка зелий и сортировки их по возрастанию
    Выводит на экран первые пять зелий по количеству
    """
    with open("transfer.txt", 'r', encoding='utf-8') as file:
        alist = []
        for line in file:
            data = line.replace("\n", "").split("&")
            alist.append([data[0], int(data[1])])
        quick_sort(alist, 0, len(alist)-1)
        for i in range(5):
            print(f"Зелья {alist[i][0]} осталось {alist[i][1]}")
    with open("transfer.txt", 'w', encoding="utf-8") as transfer:
        for el in alist:
            transfer.write(f"{el[0]}&{el[1]}\n")


if __name__ == '__main__':
    sort_potions()
