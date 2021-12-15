f = open("Practice Program 1/mytextfile.txt")
lines = f.readlines()
for x in lines:
    print(x.replace(" ","#"))