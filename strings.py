import random

message = '''
    Hi Hlokolozar, 
    
    Thank You for your interest on our Python Program.
    
    Regards,
    
    The PyTeam
'''
course = 'Python for Beginners'
print(len(course))
print('My favourite letter in python is "' + course[random.randint(0, len(course))] + '"')
print(message)
