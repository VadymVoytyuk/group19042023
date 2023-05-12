number_1 = 1
number_2 = 5

# division_result = 0
# if number_2 != 0:
#     division_result = number_1 / number_2
# print(division_result)
division_result = 0
try:
    division_result = number_1 / number_2
    # int('10.0') - bad code, too many bad code in try-except
except ZeroDivisionError:
    print('division on zero')
except (TypeError, ValueError):
    print('type error or value error')
    # raise
    # raise ArithmeticError
# except Exception:
#     print('general error')
else:  # work if there were no errors
    print('All right')
finally:  # works every time try run
    # division_result = 5555555
    print('close file')

print(division_result)