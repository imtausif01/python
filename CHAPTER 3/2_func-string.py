name = "tausif ahmad"
print (len(name)) # output will be 11 because it counts the number of characters in the string including spaces if any
print(name.endswith("d")) # output will be True and jab string wrong hoga to output will be False
print(name.startswith("t")) # output will be True and jab string right hoga to output will be True
print(name.capitalize()) # output will be 'Tausif ahmad' because it capitalizes the first letter of the string
print(name.upper()) # output will be 'TAUSIF AHMAD' because it converts all letters to uppercase
print(name.lower()) # output will be 'tausif ahmad' because it converts all letters to lowercase
print(name.title()) # output will be 'Tausif Ahmad' because it capitalizes the first letter of each word in the string
print(name.count("a")) # output will be 3 because it counts the number of occurrences of the letter 'a' in the string
print (name.find("u")) # output will be 2 because it finds the index of the first occurrence of the letter 'u' in the string
print(name.replace("tausif","sharik")) # output will be 'sharik ahmad' because it replaces the word 'tausif' with 'sharik' in the string

name2 = "   tausif ahmad   "
print (name2.strip()) # output will be 'tausif ahmad' because it removes any leading or trailing whitespace from the string

print(name.split()) # output will be ['tausif', 'ahmad'] because it splits the string into a list of words based on whitespace

name3 = "tausif","ahmad"
print(" ".join(["tausif","ahmad"]))# output will be 'tausif ahmad' because it joins the list of words into a single string with a space in between each word
