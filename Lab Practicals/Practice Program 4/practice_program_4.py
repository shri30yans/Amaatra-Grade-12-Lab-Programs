import pickle
def write():
    def more_entries():
        response = input("Do you want to enter more entries?(Y,N)")
        if response.lower() in ["y","yes"]:
            return True
        elif response.lower() in ["n","no"]:
            return False
        else:
            print("That wasn't a correct response. Please try again.")
            response = more_entries()
            return response

    f = open("Practice Program 4/myfile.dat","wb")
    while True:
        roll_number = int(input("Enter Roll number:"))
        name = input("Enter name:")
        dict = {"name":name,"roll_number":roll_number} 
        pickle.dump(dict,f)
        response = more_entries()
        if not(response):
            break
    f.close()

def read():
    f = open("Practice Program 4/myfile.dat","rb")
    try:
        while True:
            entry = pickle.load(f)
            print(entry)            
    except EOFError:
        f.close()

def search():
    f = open("Practice Program 4/myfile.dat","rb")
    roll_number = int(input("Enter roll number to search:"))
    found = False
    try:
        while True:
            entry = pickle.load(f)
            if entry["roll_number"] == roll_number:
                print("The person with roll number",roll_number,"is",entry["name"])
                found = True
    except EOFError:
        f.close()
    if found is False:
        print(roll_number, "was not found.")

write()
read()
search()





