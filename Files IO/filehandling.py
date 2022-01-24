#open 
file=open('file1.txt','r')  #here file is variable


for i in file:
    print(i)


#for closing the file
file.close() 


file=open('file1.txt','r')

print(file.read(4))

file.close()


#write mode w
file=open('file2.txt','w')
file.write('hi')

file.write("hello")
file.close()


file=open('file2.txt','r')
print(file.read())
file.close()

file=open('file1.txt','w')


file.write("Ecolibrium energy")
file=open('file1.txt','r')
print(file.read())

file.close()


#append mode a
file=open('file1.txt','a')
file.write("pune")
file=open('file1.txt','r')
print(file.read())
file=open('file1.txt','r+')
file.write('aniket')
print(file.read())

file.tell()  #cursor position

file.seek(0)

print(file.read())

file.close()


#os module
import os

#create a new directory
#os.mkdir("dirname")
os.mkdir("myfolder")

#remove a directory
os.rmdir('myfolder')

#change dir
os.chdir("Dictionary")


#get current directory Name
#os.getcwd()
aa=os.getcwd()
print(aa)

os.chdir("../Files IO")
print(os.getcwd())
