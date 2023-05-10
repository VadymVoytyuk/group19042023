# з клавіатури вводяться прізвища (можуть вводитися як з малої, так і з великої літери) учнів.
# за допомогою split створити список учнів (всі прізвища строго з великої літери),
# упорядкувати за алфавітом та вивестив консоль за допомогою циклу for

surnames = input('Enter surnames of the students: ')
corrected = (surnames.title().split())
corrected.sort()
print(corrected)
