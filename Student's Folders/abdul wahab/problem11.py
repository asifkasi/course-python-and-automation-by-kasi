n=3
for i in range (1,n+ 1):
    line=""
    for j in range(i):
        line+= chr(ord('A')+j)
    print(line)