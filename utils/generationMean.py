

f = open('genfile', 'r')

l = 0
c = 0
for line in f:
    if 'run' not in line:
        l += int(line)
        c += 1

print(l/c)



