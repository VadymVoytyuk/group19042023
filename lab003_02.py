name = input('please enter your name >>>>').title().lstrip(' 0123456789')
surname = input('please enter your surname >>>>').upper().lstrip(' 0123456789')
#print(name , surname)
name_length = len(name)
template = 'Hello,{name} {surname},did you know ,that your name contains {name_length} letters'.strip('')
name_info = template.format(name=name, surname=surname, name_length=name_length)
#print(name_info)
name_info_updated = name_info.replace('Hello', 'Hi',)
#print(name_info_updated)
name_info_final= f'{name_info_updated} ?'
print(name_info_final)






# Привіт, Андрій ШЕВЧЕНКО, а ти знав, що твоє імя складється з 6 літер"
