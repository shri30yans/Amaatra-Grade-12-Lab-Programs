# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21\
#Consider the following defination of a dictionary member {"member_no":_____, "member_name":_____}
#Write a program to enter the contents of this dictinary in a binary file

import pickle
f = open("Text Files/Lab Program 25/book.dat","wb")

def ask_if_more_entries():
    question = input("Do you want to continue? (Y/N)")
    if question in ["Y","y"]:
        return True
    elif question in ["N","n"]:
        return False
    else:
        print("You entered a invalid response. You can only enter in Y or N. Have another chance.")
        ans = ask_if_more_entries()
        return ans

while True:
    d = {}
    no = int(input("Enter member no:"))
    name = input ("Enter member name:")
    d["member_no"] = no
    d["member_name"]= name
    pickle.dump(list(d.values()),f)

    if ask_if_more_entries():
            pass
    else:
        break


f.close()


