# set1 = set()
# print(set1)
#
# set2 = {5, 6, 6, 6, 'jj', 'k', 5.5, 7., True}
# # print(set2)
# # print(len(set2))
# #
# cities = ['Київ', "Київ", 'London']
# unique_cities = set(cities)
# print(unique_cities)
# #
# # unique_letters = set('London l')
# # print(unique_letters)
# #
# # letters = list(unique_letters)
# # print(letters)
#
# # add element
# unique_cities.add('Paris')
# unique_cities.add('Paris')
# print(unique_cities)
# unique_cities.update('abc')
# print(unique_cities)
# print('a' in unique_cities)
# unique_cities.remove('a')  # raise error if no element
# print('a' in unique_cities)
# print(unique_cities)
# # data = unique_cities.pop()
# # print(data, unique_cities)
# unique_cities.discard('a')  # doesn't raise error if no element
# print(unique_cities)

# words = set(input('enter your text >>>> ').upper().replace('(', ' '
#             ).replace(',', ' ').replace(')', ' ').split())
# print(words)

set1 = {1, 2, 3}
set2 = {4, 2, 3}

# work with sets - can create new variable
# common elements
new_set_common = set1.intersection(set2)
print(new_set_common)
new_set_common_3_10_and_high = set1 & set2
print(new_set_common_3_10_and_high)
print(new_set_common == new_set_common_3_10_and_high)

# union elements
new_set_union = set1.union(set2)
print(new_set_union)
new_set_union_3_10_and_high = set1 | set2
print(new_set_union_3_10_and_high)

# difference elements
new_set_dif = set1 - set2 #  unique only for first set
print(new_set_dif)
new_set_dif_both = set1 ^ set2 #  unique only for both sets
print(new_set_dif_both)