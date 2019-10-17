# Python App calculate years
import datetime

now = datetime.datetime.now()

full_name = input('Enter Name: ')
profession = input('What\'s your profession? ')
birth_year = input('Enter your Birth year: ')
age = now.year - int(birth_year)
weight_in_lbs = input('Please enter your weight (lbs): ')
weight = int(weight_in_lbs) * 0.45


print('Hi ' + full_name + ', We love ' + profession + 's at the age ' + str(age) + ' with ' + str(weight) +
      'kg weight, Wow great!!!')

