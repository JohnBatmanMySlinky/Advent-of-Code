with open('input.txt', 'r') as f:
	dat = f.read().split('\n\n')

# part 1
print(sum([len(set(list(x.replace('\n','')))) for x in dat]))


# part 2
dat = [x.split('\n') for x in dat]
dat[len(dat)-1].remove('')           ####  >>:|
answer2 = 0
for group in dat:
	common = set(map(chr, range(97, 123)))
	for member in group:
		common = common.intersection(member)
	answer2 += len(common)
print(answer2)
