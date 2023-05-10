# string = input('Enter any string: ')
# string_upper = string.swapcase()
# print(string_upper)
# # олдварпоОРПлдоролр5656 321!!!.юб
string = input("Enter a string: ")

only_upper = ""

for char in string:

    if char.isupper():
        only_upper += char

print(only_upper)
