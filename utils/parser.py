
f = open('unparsed', 'r')


unique = []
lines = []
for line in f:
    lines.append(line)
    a = line.strip().split(' ')
    b = int(a[0]) - 1
    c = int(a[1]) - 1

    if b not in unique:
        unique.append(b)

    if c not in unique:
        unique.append(c)


f2 = open('parsed', 'w')


m = max(unique)
for i in range(m+1):
    f2.write(str(i) + ' ')

f2.write('\n') 

for line in lines:
    a = line.strip().split(' ')
    b = int(a[0]) - 1
    c = int(a[1]) - 1

    f2.write(str(b) + ' ' + str(c)  + '\n')
