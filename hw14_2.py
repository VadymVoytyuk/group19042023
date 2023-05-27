# написати функцію, яка отримує довжину та ширину прямокутника,
# а повертає флоатове значення периметра (без округлень, але флоат)
def get_sides_of_rectangle():
    side_a = float(input("Please enter side A: \n"))
    side_b = float(input("Please enter side B: \n"))
    return side_a, side_b


def area_message(area_floated):
    print(f"The area of the rectangle is: {area_floated}")


def calculate_area_of_rectangle():
    side_a, side_b = get_sides_of_rectangle()
    area_floated = float(side_a * side_b)
    area_message(area_floated)


calculate_area_of_rectangle()
