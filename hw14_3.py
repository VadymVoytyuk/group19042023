
def replace_characters(e, t):
    my_string = str(input("Please enter your text: \n"))
    return my_string


def character_replacement(my_string):
    my_new_string = my_string.replace("e", "").replace("t", "").replace("T","").replace("E","")
    return my_new_string


string_for_test = 'SvevTdvrEttt'
result = character_replacement(string_for_test)
print(result)

