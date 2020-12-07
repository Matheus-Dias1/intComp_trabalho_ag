

f = open('genfile', 'r')

l = 0
c = 0
r = 0
for line in f:
    if 'run' not in line:
        l += int(line)
        c += 1
    else:
        r += 1

print('generation mean', l/c)
print('sucess rate', 1-r/c)


