# написати код з наступною логікою роботи:
# користувач вводить логін та пароль (дві змінних). в логіні допустимі тільки літери, в паролі тільки літери та цифри
# просимо підтвердити пароль - якщо він такий же як і в першому випадку, вивести повідомлення, що користувач залогінений
# вивести повідомлення, що користувач розлогінений через примхи викладача
# попросити знову ввести логін та пароль - якщо вони співпадуть з першочерговими - знову повідомлення про залогінення (текст такий, як і в перший раз, то ж подумайте про створення окремої змінної)
import time

user_name = input('enter your user name:')
if user_name.isalpha() is not True:
    print('user_name should contain only letters')
    time.sleep(2)
    raise ValueError('user_name should contain only letters')
password = input('enter your password:')
if password.isalnum() is not True:
    print('password should contain  letters and numbers')
    time.sleep(2)
    raise ValueError('password should contain  letters and numbers')
elif password.isdecimal():
    print('password should contain  letters and numbers')
    time.sleep(2)
    raise ValueError('password should contain  letters and numbers')
elif password.isalpha():
    print('password should contain  letters and numbers')
    time.sleep(2)
    raise ValueError('password should contain  letters and numbers')
password1 = input('confirm your password:')
if password == password1:
    print('you are logged in')

    time.sleep(1.5)
    print("You are logged off by admin request")

    user_name1 = input('enter your user name:')
    if user_name1.isalpha() is not True:
        print('user_name should contain only letters')
        time.sleep(2)
        raise ValueError('user_name should contain only letters')
    password2 = input('enter your password:')
    if password2.isalnum() is not True:
        print('password should contain  letters and numbers')
        time.sleep(2)
        raise ValueError('password should contain  letters and numbers')
    elif password2.isdecimal():
        print('password should contain  letters and numbers')
        time.sleep(2)
        raise ValueError('password should contain  letters and numbers')
    elif password2.isalpha():
        print('password should contain  letters and numbers')
        time.sleep(2)
        raise ValueError('password should contain  letters and numbers')

    if password2 == password:
        print('you are logged in')
        time.sleep(2)
    else:
        print('incorrect password\nstart your log in from beginning')
        time.sleep(3)

else:
    print('passwords are not matching\nstart your log in from beginning')
    time.sleep(3)