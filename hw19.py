import csv

with open('airports.csv', mode='r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    for line in content[1:]:
        country = line.strip().split(';')
        ua_iso_country = country[5]
        if ua_iso_country == 'UA':
            print(country)
