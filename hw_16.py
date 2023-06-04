def infinite_month():
    month = [
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
        yield month[0]
        yield month[1]
        yield month[2]
        yield month[3]
        yield month[4]
        yield month[5]
        yield month[6]
        yield month[7]
        yield month[8]
        yield month[9]
        yield month[10]
        yield month[11]


for month in infinite_month():
    print(month)
