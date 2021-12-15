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

    f = open("Practice Program 5/myfile.dat","wb")
    while True:
        roll_number = int(input("Enter Roll number:"))
        name = input("Enter name:")
        marks = int(input("Enter marks:"))
        dict = {"name":name,"roll_number":roll_number,"marks":marks} 
        pickle.dump(dict,f)
        response = more_entries()
        if not(response):
            break
    f.close()

def read():
    f = open("Practice Program 5/myfile.dat","rb")
    try:
        while True:
            entry = pickle.load(f)
            print(entry)            
    except EOFError:
        f.close()


def search():
    f = open("Practice Program 5/myfile.dat","rb+")
    roll_number = int(input("Enter roll number to search:"))
    found = False
    try:
        while True:
            pos = f.tell()
            entry = pickle.load(f)
            if entry["roll_number"] == roll_number:
                print("Roll Number",entry["roll_number"],"Name",entry["name"],"Marks",entry["marks"])
                
                # Enter marks.
                marks = int(input("Enter new marks:"))
                entry["marks"] = marks
                f.seek(pos)
                pickle.dump(entry,f)
                found = True
    except EOFError:
        f.close()
    
    if found is False:
        print("Marks were updated.\nNew marks:")
        read()
    else:
        print(roll_number, "was not found.")



write()
read()
search()





