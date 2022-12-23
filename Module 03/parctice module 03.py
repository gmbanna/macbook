# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname + " " + fname)

# age = int(input('Enter your age: '))
# if age >= 18:
#     print('you can vote')
# else:
#     print('you can not vote')
#
# x = 3
# y = 5
#
# if x > y:
#     print('x is greater than y')
# else:
#     print('x is less than y')

# find leap year
# current_year = 2024
# if current_year % 4 == 0:
#     print(current_year, 'is a leap year')
# else:
#     print(current_year,'is not a leap year')

# if , elif and else how to use?

# number = int(input('Enter number: '))
#
# if number > 0:
#     print('positive number')
# elif number < 0:
#     print('negetive number')
# else:
#     print('number is zero')
#
# name = input('Enter name: ')
# profession = input('Enter profession: ')
# country = input('Enter country: ')
# birth_year = int(input('Enter birth uear: '))
# gender = input('Enter m or f: ')
#
# age = int(2022 - birth_year)
#
# if gender == 'm':
#     pronoun = 'he'
# else:
#     pronoun = 'she'
#
# output = f'name is {name} profession {profession} of {country}. {pronoun} is {age} year old'
#
# print(output)
#
# number = int(input('Enter number: '))
#
# if number > 0:
#     print('it is positive number')
# elif number < 0:
#     print('its a negetive number')
# else:
#     print('number is zero')

# my_age = int(input('Enter my age: '))
#
# my_sister_age = int(input('Enter my sister age: '))
#
# if my_age >= my_sister_age:
#     print('my sistee is younger then me')
#
# else:
#     print('my sister is older than me')

"""
>80         A+
>70         A
>60         A-
>50         B
>40         C
>33         D
>0-32       F
"""
# number = int(input('Enter Number: '))
#
# if number > 80:
#     print('Your gread is A+ ')
# elif number > 70:
#     print('Your gread is A ')
# elif number > 60:
#     print('Your gread is A- ')
# elif number > 50:
#     print('Your gread is B ')
# elif number > 40:
#     print('Your gread is C ')
# elif number > 33:
#     print('Your gread is D ')
# else:
#     print('feltus')

#  5+55+555
# number = input('Enter number: ')
# print(int(number)+int(number*2)+int(number*3))
#
# print(type(number))
#
# number = int(input('Enter a positive number: '))
# sum = number*(number+1)/2
# print(round(sum))

# age = int(input('Enter age :'))
# gender = input('Enter m or f :')
#
# if age > 40 and gender == 'm':
#     print('hi uncle')
# elif age > 40 and gender == 'f':
#     print('Hi aunty')
# else:
#     print('Hi apu')
#
# user_input = input('Enter your name: ')
#
# if user_input == 'tasfiya' or 'tuhin':
#     print('she is gazi gazi family member')
# else:
#     print('she is not gazi family memeber')

# x = 5
#
# if x < 3 or x > 6:
#     print('it is a positive nuber')
# else:
#     print('negetive')

# num = int(input('Enter number: '))
#
# if num % 2==1:
#     print('odd number')
# else:
#     print('even number')

# age = 37
# age -= 2
# print(age)
#
# age = 37
# age *= 2
# print(age)

gender = not 'f' or not 'm'

if gender != 'm':
    print('male')
if gender != 'f':
    print('female')

y = 10
print(y < 100 and y > 6) # and er khetre 2ta condition true hote hobe tahole print true hobe
y = 10
print(y < 100 or y > 15) # or er khetre jekono akta condition true holei hobe tahole print true hobe

x = ' apple'
y = 'apples'

print(x is y,': test')
print(x is not y,': teat2')


print(id(x))
print(id(y))



