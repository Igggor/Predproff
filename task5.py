def count_herbs() -> None:
    """
    Функция для создания хеш-таблицы на основе подсчета количества трав
    Результат выполнения выводится в консоль
    """
    herbs = {}
    with open("tasks/magical.csv", 'r', encoding="utf-8") as file:
        lines = []
        header = file.readline()
        for line in file:
            data = line.replace("\n", '').split(",")
            for i in range(2, len(data)):
                if data[i] not in herbs.keys():
                    herbs[data[i]] = 1
                else:
                    herbs[data[i]] += 1
        arr = [[key, value] for key, value in herbs.items()]
        arr.sort(key=lambda x: x[1], reverse=True)
        for i in range(5):
            print(f"{arr[i][0]} - {arr[i][1]}")


if __name__ == '__main__':
    count_herbs()
