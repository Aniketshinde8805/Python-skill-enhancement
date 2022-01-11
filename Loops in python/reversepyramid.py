num=int(input("enter a number"))
for i in range(0,num+1):
    
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,num+1-i):
        print("* ",end="")
    print("")