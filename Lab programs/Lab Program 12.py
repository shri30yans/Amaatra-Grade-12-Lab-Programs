# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to read a file named "abc.txt" and copy these contents into another file name "xyz.txt"

def move():
    f=open("Text Files/Lab Program 12/abc.txt","r")
    f_copy=open("Text Files/Lab program 12/xyz.txt","w")
    while True:
        c=f.read(1)
        if not c:
            break
        f_copy.write(c)
    f.close()
    f_copy.close()
move()
