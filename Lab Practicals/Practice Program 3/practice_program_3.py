f = open("Practice Program 3/mytextfile.txt")
fout = open("Practice Program 3/output.txt","w")
lines = f.readlines()
for x in lines:
    if not("a" in x):
        fout.write(x)

