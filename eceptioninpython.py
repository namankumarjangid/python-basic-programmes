try:
    age=int(input('Age:'))
    income=int(input('income:'))
    print(income/age)
except ZeroDivisionError:
    print('age can not be 0.')
except ValueError:
    print('invalid value')