def count_potions() -> None:
    """
    Функция для решения первой задачи. Выводит на экран количество Мощного зелья
    :return:
    """
    with open("tasks/magical.csv", 'r', encoding="utf-8") as file:
        alist = {}
        count = 0
        header = file.readline()
        for line in file:
            data = line.split(",")
            if data[1] == "-1":
                data[1] = "0"
            if data[0] == "Мощное Зелье":
                count += int(data[1])
            if not data[0] in alist.keys():
                alist[data[0]] = int(data[1])
            else:
                alist[data[0]] += int(data[1])

    with open("magicaPotions.txt", 'w', encoding="utf-8") as out:
        for key, value in alist.items():
            out.write(f"{key} в запасах еще есть - {value}\n")
    with open("transfer.txt", 'w', encoding="utf-8") as transfer:
        for key, value in alist.items():
            transfer.write(f"{key}&{value}\n")


    print(count)


if __name__ == '__main__':
    count_potions()
