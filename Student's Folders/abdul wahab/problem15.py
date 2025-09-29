#abdul wahab
num=1
alp= num +64

for i in range(1,5,1):
    for j in range(i):
        print(f"{chr(alp)}{num}" ,end=" ")
        num=num + 1
        alp= alp +1
    print()