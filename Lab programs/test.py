# def ChangeVal(M,N):
#     for i in range(N):
#         if M[i]%5 == 0:
#             M[i]//=5
#         if M[i]%3 == 0:
#             M[i]//=5
# L = [25,8,75,12]
# ChangeVal(L,4)
# for i in L:
#     print(i,end="#")
Name="PythoN3.1"
R=""
for x in range(len(Name)):
    if Name[x].isupper():
        R=R+Name[x].lower()
    elif Name[x].islower():
        R=R+Name[x].upper()
    elif Name[x].isdigit():
        R=R+Name[x-1]
    else:
        R=R+"#"
print(R)
# b=1
# for a in range(1,10,2):
#     print(a)
#     b+=a+2
# print(b)

