letter = input("Enter string: ")
vowel = ['a','e','i','o','u']
count = 0
for i in letter:
    if i.lower() not in vowel:
        count = count + 1

print("There is " + str(count) + " non vowel words in given string.")
