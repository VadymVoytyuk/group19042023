
def ten_numbers(number_input=2):
    if number_input >= 1:
        m = [number for number in range(number_input, number_input + 10)]
        return m
    else:
        raise ValueError


result = ten_numbers(5)
print(result)
