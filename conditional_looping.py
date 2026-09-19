#
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# and
# or
# not
'''
num_1 = int(input('Enter a number: '))
if num_1  > 0:
    print('Positive number')
elif num_1 < 0:
    print('Negative number')
else:
    print('Zero')
'''

'''
n = int(input('Enter a number: '))
if n % 2 == 0:
    print('Even number')
else:
    print('Odd number')
'''
'''
grade_evaluation_num = float(input('Enter a number: '))
if grade_evaluation_num < 0 or grade_evaluation_num > 100:
    print('Invalid input')
elif grade_evaluation_num  >= 90:
    print('Excellent')
elif grade_evaluation_num >= 70:
    print('Good')
elif grade_evaluation_num >= 50:
    print('Pass')
else:
    print('Fail')
'''
'''
username = 'admin'
password = 'python123'
usr = input('Enter a username: ')
pwd = input('Enter a password: ')
if usr == username and password == password:
    print('Login Successful')
else:
    print('Invalid credentials')
'''
#for i in range(0, 10):
#    print(i)
'''
for i in range(1, 11):
    print(" 5 X ", i, " = ", 5*i)
'''
'''
i = 1
while i <= 10:
    print(" 5 X ", i, " = ", 5*i)
    i += 1
'''
'''
for i in range(1, 11):
    print(i)
'''
'''
num = int(input('Enter a number: '))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i }")
'''
