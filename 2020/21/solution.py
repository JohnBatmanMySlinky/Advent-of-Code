import sys

dat = [x.strip('\n').replace(')','').replace(',','').split('(contains') for x in sys.stdin]

food = []
for each in dat:
    food.append([set(x.strip().split(' ')) for x in each])
del dat

# seperating out allergens and ingredients
all_allergen = []
all_ingredient = []
for ingredient, allergen in food:
    # add unique allergens
    for each in allergen:
        if each not in all_allergen:
            all_allergen.append(each)

    # add ALL ingredients
    for each in ingredient:
        all_ingredient.append(each)

# finding all ingredients that can br allergens
known_allergens = set()
for a in all_allergen:
    [known_allergens.add(x) for x in set.intersection(*[x[0] for x in food if a in x[1]])]

# part 1 final
part1 = 0
for i in all_ingredient:
    if i not in known_allergens:
        part1 += 1
print('part1: ' + str(part1))

# this is super lazy, I could adjust my code above but mehhhhh
ingredient_allergen_dict = {}
while all_allergen:
    for a in all_allergen:
        candidates = list(set.intersection(*[x[0] for x in food if a in x[1]]))
        if len(candidates) == 1:
            ingredient_allergen_dict[candidates[0]] = a
            all_allergen.remove(a)
            for x in range(len(food)):
                if candidates[0] in food[x][0]:
                    food[x][0].remove(candidates[0])
                if a in food[x][1]:
                    food[x][1].remove(a)

# sort dictionary alphabetically via values
sorted_dict = {k: v for k, v in sorted(ingredient_allergen_dict.items(), key=lambda item: item[1])}
print(','.join(sorted_dict.keys()))

