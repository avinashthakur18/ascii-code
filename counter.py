file = open("ascii-art.txt", "r")

line_no = 1

for line in file:
    line = line.rstrip("\n")

    if len(line) == 0:
        continue

    result = []

    current_char = line[0]
    count = 1

    for ch in line[1:]:
        if ch == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = ch
            count = 1

    result.append((count, current_char))

    print("ROW", line_no, "=", result)
    line_no += 1

file.close()