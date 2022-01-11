# comparision of two strings
s1=input("enter the first string")
s2 = input("enter the second string")

if len(s2) == len(s1):
    flag=0
    for i in range(0,len(s1)):
        if s1[i]==s2[i]:
            pass
        else:
            flag=1
            print("both the strings are different")
            break
    if flag==0:
        print("both string are equal")
else:
    print("both strings are different")