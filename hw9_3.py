# string = input('Enter any string: ')
# string_upper = string.swapcase()
# print(string_upper)
# # олдварпоОРПлдоролр5656 321!!!.юб
string = input("Enter a string: ")

only_upper = ""

for letter in string:

    if letter.isupper():
        only_upper += letter

print(only_upper)
