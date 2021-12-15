f = open("Practice Program 2/mytextfile.txt")
text = f.read()
vowel, consonants, upper,lower = 0,0,0,0
vowels = "aeiouAEIOU"
for x in text:
    if x in vowels:
        vowel+=1
    elif x not in vowels and x.isalpha():
        consonants+=1
    if x.isupper():
        upper+=1
    elif x.islower():
        lower+=1
print("Number of vowels:",vowel)
print("Number of consonants:",consonants)
print("Number of uppercase:",upper)
print("Number of lowercase:",lower)

