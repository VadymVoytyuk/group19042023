# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below

footprint = '\U0001F463'  # Unicode  described by number
user_name = input('Please, enter your name >>>')  # Name request description added ;Extra space; Variable lowercase
user_age = input('Please, enter your age >>>')  # Extra space; Variable lowercase
result = f'My name is {user_name}, I am {user_age} years old{footprint}'  # f-string syntax; Cyrillic input replaced
print(result)  # Cyrillic input  replaced