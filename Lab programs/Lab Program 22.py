# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
# Write a Program to write roll no, name and marks of a student in a data file marks.dat

fw = open("Text Files/Lab Program 22, 23/marks.dat","a")
count = int(input("Number of students:"))
for i in range (count):
    print("Enter details of student",i+1,"below")
    rollno= int(input("Roll no:"))
    name = input("Name:")
    marks = float(input("Marks:"))
    rec = str(rollno) + ", " + name + ", " + str(marks) + "\n "
    fw.write(rec)
fw.close()
print("Done!")