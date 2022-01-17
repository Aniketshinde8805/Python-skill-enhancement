s1="this is my string"
print(s1[0])
print(s1[8])
print(s1[5])

# slicing string elements from index 4 to the end of string
print(s1[4:])

# slicing string elements from starting index to 7th index of string
print(s1[:7])

# slicing string elements from index 0 to 9 index
print(s1[0:9])

# slicing string elements to display whole string
print(s1[:])

print(s1[::])

# reversing string elements by slicing 
print(s1[::-1])

#reverse string element and displaying elements with gap of 2 indexes
print(s1[::-2])

# slicing string elements and display elements with gap of 2 indexes
print(s1[::2])

#using "in" operator in string
for i in s1:
    print(i)

# using "not in " operator to display the elements that are not in s1 when compared with s2
s1="string14356755"
s2="string22345456"
for i in s1:
    if i not in s2:
        print(i)
    
        
