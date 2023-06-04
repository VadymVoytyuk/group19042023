


def infinite():
    num = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    while True:
        yield num[0]
        yield num[1]
        yield num[2]
        yield num[3]
        yield num[4]
        yield num[5]
        yield num[6]
        yield num[7]
        yield num[8]
        yield num[9]
        yield num[10]
        yield num[11]


for x in infinite():
    print(x)
