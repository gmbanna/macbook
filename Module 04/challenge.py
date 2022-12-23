# age = int(input('Enter your age: '))
# gender = input('Enter m of f: ')
#
# if gender == 'f':
#     print('She will work only urban area')
#
# if gender == 'm' and age >= 20 and age < 40:
#     print('They may anywhere')
#
# elif gender == 'm' and age >= 40 and age < 60:
#     print('He will be work in urban area')
# else:
#     print('Error')



# Python program to reverse a number
#
# num = 1234
# rev = 0
#
# while num > 0:
# 	a = num % 10           # 1234/10	= 4
# 	rev = rev * 10 + a	   # 0 * 10 + 4 =  4
# 	num = num // 10		   # 123
#
# print(rev)				   # 4 3 2 1

# salary = int(input('Enter your salary: '))
# service_yeres = int(input('Enter your service yere: '))
# bonus = salary*(5/100)
# paid_amount = salary+bonus
#
# print(type(bonus))
#
# if service_yeres > 5:
#     print('your paid sailary with bonus',paid_amount)
# else:
#     print('you can not get bonus')
#
# purchased_quentityy = int(input('Enter shopping amount: '))
# unit_cost = purchased_quentityy * 100
# discount = unit_cost*(10/100)
# total_discount = unit_cost - discount
# if purchased_quentityy >= 1000:
#     print('your total discount is', total_discount)
#
# else:
# 	print('you are not eligible to get discount')


## find sum and average
# sum = 0
# i = 1
# while i <= 10:
# 	sum = sum + i
# 	print(i, '=', sum/10)
# 	i += 1
#
# print(sum/10)

## ODD AND EVEN NUMBER PRINT AND AFTER TOTAL OF SUM

# sum = 0
# i = 2
# while i <= 10:
# 	sum = i + sum
# 	print(i, '=', sum)
# 	i +=2

## Factorial num
# sum = 1
# i = 1
# while i <= 8:
# 	sum = sum * i
# 	print(i,'=', sum)
# 	i += 1

## Factorial num with while loop

number = int(input('Enter any number: '))
factorial = 1
while number >= 1:
	factorial =  factorial * number
	number -= 1
print(factorial)

## Factorial num with for loop

num = int(input('Enter any number: '))

factorial = 1

for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

## find prime number

number = int(input('Enter any number: '))

while True:

    if number % 2 == 0:
        print('its not a prime number')
    else:
        print('Its a prime number')
    break