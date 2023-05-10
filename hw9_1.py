# є список, елементами якого будуть інтові та флоатові значення.
# потрібно створити новий список, в якому будуть елементи з списку, зазначеному вище, проте помножені на 2 та переведені в стрічковий формат

# list_of_elements = [2, -6, 5.5, 5, 20, 5]
# for element in list_of_elements:
#     my_new_list.append(i * 5)
#     print(my_new_list)

my_list = [1.5, -2, 3, 4.4, 5.0]
my_new_list = [element * 2 for element in my_list]
string = ''
for element in my_new_list:
    string += str(element)
    string += ' '
print(string)