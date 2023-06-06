def returns_str(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == str:

            return '<b>' + result + '</b>'
        return result

    return wrapper


@returns_str
def data(value):
    return value


print(data("hello"))
print(data(5))
print(data('5'))
