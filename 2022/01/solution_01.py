with open("input.txt") as f:
    dat = [x.strip() for x in f.readlines()]

def do_calorie(dat):
    cal_list = []
    calories = 0
    for each in dat:
        if each == '':
            cal_list.append(calories)
            calories = 0
            continue
        else:
            calories += int(each)
    return cal_list
    

print(f"solution 01: {max(do_calorie(dat))}")
print(f"solution 02: {sum(list(reversed(sorted(do_calorie(dat))))[:3])}")