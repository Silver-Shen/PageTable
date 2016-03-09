import os
fd = open('mem.txt')
memory = fd.readlines()
mainMem = []
for i in range(0, len(memory)):
    line = memory[i].split(' ')
    #print line
    page = []
    for j in range(2, len(line)):
        if line[j] != '\n':
            page.append(int(line[j],16))
    mainMem.append(page)
    print page

