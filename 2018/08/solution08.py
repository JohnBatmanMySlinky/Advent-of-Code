with open("input.txt", "r") as f:
    data = [int(x) for x in f.readlines()[0].split(" ")]

def p1(data):
    children = data[0]
    meta_data_number = data[1]
    data = data[2:]
    meta_data_total = 0
    values = []

    for i in range(children):
        meta_data_total_tmp, data, values_tmp = p1(data)
        meta_data_total += meta_data_total_tmp
        values += [values_tmp]

    meta_data_total += sum(data[:meta_data_number])

    if children == 0:
        return meta_data_total, data[meta_data_number:], sum(data[:meta_data_number])
    else:
        return meta_data_total, data[meta_data_number:], sum(values[k-1] for k in data[:meta_data_number] if k <= len(values))

answer1, data, answer2 = p1(data)

print(f"part 1: {answer1}")
print(f"part 2: {answer2}")
