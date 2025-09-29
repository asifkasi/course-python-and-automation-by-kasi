def decreasing_letters(n):
    for i in range (n):
        for j in range (n,i,-1):
         print(chr(64 + j),end="")
        print()
        
decreasing_letters(3)