freqs = set([0])
with open('inputs/day_1.txt') as f:
    x = f.readlines()
    x = [int(xx.strip()) for xx in x]
tot = 0
found = False
while not found:
    for ii in x:
        tot += ii
        if tot in freqs:
            print(tot)
            found = True
            break
        else:
            freqs.add(tot)
