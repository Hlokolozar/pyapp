# Python App calculate years
import datetime

now = datetime.datetime.now()

full_name = input('Enter Name: ')
profession = input('What\'s your profession? ')
birth_year = input('Enter your Birth year: ')
age = now.year - int(birth_year)


print('Hi ' + full_name + ', We love ' + profession + 's at the age ' + str(age) + ', Wow great!!!')
print(age)
