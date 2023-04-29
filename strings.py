from hashlib import new

my_love = 'I love python'

initial_number = 54
number_one = 5
number_two = 4

print(id(number_two))
result = number_two * 10 + number_one

print(number_two, number_one, sep='', end='--------')
print(result)

# to many plusses not a good practice
city = 'Kyiv'
country = 'Ukraine'
continent = 'Europe'

city_o = 'Oslo'
country_n = 'Norway'

capital_city = city + ' ' + country + ' ' + continent
pass

# good practice
# 1 f-string - immediately
capital_city_correct = f'{city} {country} {continent}'
print(capital_city_correct)

# 2-format method
template = '{city} -  {country} {continent}'
kyiv_info = template.format(city=city, country=country, continent=continent)
print(kyiv_info)
oslo_info = template.format(city=city_o, country=country_n, continent=continent)
print(oslo_info)

# smiles utf -8

# Unicode Name	Fire   Unicode Number	U+1F525 🔥

fire_1 = 'fire \U0001F525'
fire_2 = 'fire \t🔥'
fire_3 = 'fire \N{Fire}'
fire_4 = r'fire sdvsvsvsv\svsvsv\svsvsv\N{Fire}🔥'  # r (role) - for clasting the outputs in one line
print(fire_1, fire_2, fire_3, fire_4, end='\n\n\n')

# user_name = input('please enter your name >>>> ').title() #only title leters
# user_name = input('please enter your name >>>> ').capitalize()
# user_name = input('please enter your name >>>> ').upper()
# user_name = input('please enter your name >>>> ').lower().strip('\025t')#stripping spaces before first input or enterd data"xx"
# user_name = input('please enter your name >>>> ').lower().lstrip('\025t')
# user_name = input('please enter your name >>>> ').lower().rstrip('\025t')
##user_name = input('please enter your name >>>> ').casefold() #Straße
# user_name = input('please enter your name >>>> ').swapcase()  # Straße
# print(user_name)

# replace

street = "Baker Street 125 , room 125"
sherlock_address = street.replace('125', '234', 1)
print(sherlock_address)

# a->e , e->b (letter by letter)
# replacer = street.replace('a', 'e')
# replacer = street.replace('e', 'b')
# print(replacer) # not the way to do

translate_map = str.maketrans('ae', 'eb')
trans_result = street.translate(translate_map)
print(trans_result)

street_length = len(trans_result)
print(street_length)

from flask import Flask

app = Flask(__name__)


@app.get('/')
def j():
    result = sherlock_address + fire_3
    return result


app.run()
