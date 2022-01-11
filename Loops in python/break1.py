# print prime number using continue statements
start=int(input("enter the starting no of range"))
end=int(input("enter the end of range"))

for i in range(start,end):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i)

    
        