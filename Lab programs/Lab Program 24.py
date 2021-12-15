# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
#A binary file book.dat has structure ["Book No, Book_name, Author, Price"]
# Write a user defined function to input and add records.
# Count no of nooks by the given author. Make a user defined function called count() that accepts the author and returns the count

import pickle
file_path = "Text Files/Lab Program 24/book.dat"
def add_entries():
    f = open(file_path,"ab")

    more_entries = True
    while more_entries:
        BookNo = int (input("Book no:"))
        BookName = input("Book name:")
        Author = input("Authour name:")
        Price = int(input("Book price:"))
        rec = [BookNo,BookName,Author,Price]
        pickle.dump(rec,f)
    
        if ask_if_more_entries():
            pass
        else:
            break
    f.close()

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


def count(authour):
    f = open(file_path,"rb")
    num = 0
    try:
        while True:
            rec = pickle.load(f)
            # print(rec)
            if authour.lower() == rec[2].lower():
                num += 1
                for x in rec:
                    print(x,end = ", ")
                print()
    except:
        f.close()
        print("Total number of books:",num)

            



def main():
    add_entries()
    authour = input("Enter the Authour's name whose book count I need to find:")
    count(authour)
main()





