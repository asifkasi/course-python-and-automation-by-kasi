n=4
odd_num= n*2-1

for i in  range (n,0,-1):
    for  j in range (n-i,0,-1):
        print(" ",end='')
    for k in range (odd_num):
        print("*",end="")
    print()
    odd_num-=2
