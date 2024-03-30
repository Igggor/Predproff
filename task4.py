def count_classes() -> None:
    """
    Функция для подсчета количества зелий классов.
    Результат выполнения функции выводится в консоль
    """
    classes = {}
    with open("tasks/magical.csv", 'r', encoding="utf-8") as file:
        lines = []
        header = file.readline()
        for line in file:
            data = line.replace("\n", '').split(",")
            lines.append(data)
            name = data[0].split()
            tip = ' '.join([name[x] for x in range(1, len(name))])
            if tip in classes.keys():
                classes[tip].append(int(data[1]))
            else:
                classes[tip] = []
                classes[tip].append(int(data[1]))
        for key, value in classes.items():
            print(f"{len(value)} зелий класса {key}, общее количество зелий {sum(value)}")


if __name__ == '__main__':
    count_classes()
