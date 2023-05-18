"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""

student = {
    'Іван Петров': {'Пошта': 'Ivan@gmail.com', 'Вік': 14, 'Номер телефону': '+380987771221', 'Середній бал': 95.8},
    'Женя Курич': {'Пошта': 'Geka@gmail.com', 'Вік': 16, 'Номер телефону': None, 'Середній бал': 64.5},
    'Маша Кера': {'Пошта': 'Masha@gmail.com', 'Вік': 18, 'Номер телефону': '+380986671221', 'Середній бал': 80}}
print(f'Original dictionary :\n{student}\n\n')


student['Сидор Сидоров'] = {'Пошта': 'Sidor@gmail.com', 'Вік': 27, 'Номер телефону': '+380986671245',
                            'Середній бал': 91}
print(f'Updated dictionary with new student:\n{student}\n\n')

for key, value in student.items():
    for key1, value1 in value.items():
        if key1 == 'Середній бал' and value1 >= 90:
            print(f'Student with grades higher then 90 is:{key, value1}')

count = 0
for key, value in student.items():
    for key1, value1 in value.items():
        if key1 == 'Середній бал':
            count += value1
group_average = count / len(student)
print(f'Group average grade is : {group_average}')

for key, value in student.items():
    for key1, value1 in value.items():
        if key1 == 'Номер телефону' and value1 is None:
            print(f'{key} - Please provide your parents phone number:')

student['Женя Курич']['Номер телефону']=+380986677777
print(f'Updated dictionary with Женя Курич parents phone number :\n {student}')