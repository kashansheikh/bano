'''#mixture
f=open("new.txt",'a')
f.write("\n hello1")
f.close()
f=open("new.txt")
print(f.read(6))
print(f.tell())
f.seek(0)


#to open file
f=open("new1.text")
print(f.read())


#to replace ans write
f=open("new.txt",'w')
f.write("\n hello1")
f.close()


#to add text to the file
#\n for next line
f=open("new.txt",'a')
f.write("\n hello1")
f.close()

f=open("new.txt")
print(f.readlines())
print(f.readlines())
print(f.readline(100))'''

import csv
with open('student.csv',"w", newline='') as file:
    write=csv.writer(file)
    write.writerow(["SN","Movie Name","writer"])
    write.writerow([1,"Lord of thw eings","hello"])


                     




