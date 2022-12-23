'Messi is the footballer of argentina. He is 36 years old'

name = input('Enter your name: ')
profession = input('Enter profession: ')
country = input('Enter country name: ')
birth_year = input('Enter your birth year: ')
gender = input('Male or Female: ')

age = 2022 - int(birth_year)
if gender == 'm':
    pronoun = 'He'
else: pronoun = 'she'

text =f'{name} is the {profession} of {country}. {pronoun} is {age} years old'
print(text)
