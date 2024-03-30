with open("tasks/magical.csv", 'r', encoding="utf-8") as file:
    lines = []
    header = file.readline()
    for line in file:
        data = line.replace("\n", '').split(",")
        lines.append(data)
    print(lines)
    command = input()
    while command != "стоп":
        data = []
        out = None
        maxi = -(10**10)
        for i in range(len(lines)):
            if lines[i][-1] == command:
                count = int(lines[i][1])
                if count > maxi:
                    maxi = count
                out = lines[i][0]

        if out is None:
            print("Такую траву мы не используем")
        else:
            print(f"{command} используется в {out}, его количество составялет {maxi}")
        command = input()