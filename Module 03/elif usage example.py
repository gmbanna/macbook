"""
>80         A+
>70         A
>60         A-
>50         B
>40         C
>33         D
>0-32       F
"""

number = int(input('Enter Number: '))

if number > 80:
    print('Gread is A+')
elif number > 70:
    print('Gread is A')
elif number > 60:
    print('Gread is A-')
elif number > 50:
    print('Gread is B')
elif number > 40:
    print('Gread is C')
elif number > 33:
    print('Gread is D')
else:
    print('Gread is F')
