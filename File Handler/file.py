#Opening the file
file1=open("text.txt", "r")
for i in file1:
    print(i)
#Method 2
file2=open("text.txt", "r")
print(file2.read())
#Method 3
file3=open("text.txt", "r")
print(file3.read(5))
#Writing on File
file4=open("text.txt", "w")
file4.write("Hello!\n")
file4.write("Files\n")
file4.write("Hey\n")
file4.close()
#Appending
file5=open("text.txt", "a")
file5.write("Duolingo")