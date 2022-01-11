print("Enter the marks")
maths=int(input("enter the marks of Mathematics"))
sci=int(input("enter the marks of Science"))
soci=int(input("enter the marks of Social Science"))

if maths<35 or sci<35 or soci< 35:
    percent=(sci+maths+soci)/300*100
    print("Your Percentage is ",percent)
    print("You have failed")
else:
    percent=(sci+maths+soci)/300*100
    print("Your Percentage is ",percent)
    if percent>35 and percent<60:
        print("You have got second class")
    elif percent>=60 and percent<75:
        print("You have got First Class")
    elif percent>75:
        print("You have got Distinction")
