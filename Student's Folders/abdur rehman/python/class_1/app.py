# 32. Write a program to show a number can be expressed as the sum of two 
# number. 
# Input: 5 
def sum_of_two(num): # defniing a funtion for patting a pattern
    for i in range(1, num): # looping from 1 to less than num 
        print(f"{num} = {i} + {num - i}") # printing `num = i` and `num -i` (to print  expected number)
    # function end hair       


# for i in range(65):
#     for j in range(69):
#         print(i, end=" ")
#     print(chr)   

# for i in range(65,69):
#     for j in range(64,i):
#         print(chr(i) ,end=" ")
#     print()    


# for i in range(chr(65,1)):
#     for j in range(chr(69,1)):
#         print(chr,end=" ")
#     print()    
 
# n=4
# odd_num=1+n*2
# for i in range(n+1,0,-1):

#     for j in range(n-i,-1,-1):
#         print(" ",end="")
#     for k in range(odd_num): 
#         print("*",end="") 
#     print()
#     odd_num = odd_num-2

# n=4
# odd_num=1
# for i in range(1,n+1,1):
    
#     for j in range(n-i,0,-1):
#         print(" ",end="")
#     for k in range(odd_num): 
#         print("*",end="") 
#     print()
#     odd_num = odd_num+2
n = 5  # takeing and input to expressed the pattern
sum_of_two(n) # calling user deifine  function to expressed the patterns, passing `n` has parameter to replace the num 
