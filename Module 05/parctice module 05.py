# end parameter

# num = 150
# while num > 0:
#     print(num,end= ' ')
#     num -= 10

## find prime number
#
# myPrimeNumbers = []
# i = 1
# while i <= 20:
#
#   if i > 1:
#     isPrime = True
#   else:
#     isPrime = False
#
#   j = 2
#   while j < i:
#     if i%j == 0:
#       isPrime = False
#       break
#     j += 1
#
#   if isPrime:
#     print(i, "is a prime number")
#     myPrimeNumbers.append(i)
#   else:
#     print(i)
#
#   i += 1
#
# print(myPrimeNumbers)

## multiple sum

# sum = 0
# ch = 'y'
#
# while ch.lower() == 'y':
#     num = int(input('Enter any number: '))
#     sum = sum + num
#     ch = input('if you want to continue y/n: ')
#
# print('Total number of sum', sum)

## Prime number
# i = int(input('enter num: '))
#
# while i > 0:
#     if  i % 2  == 0:
#         print(' not prime')
#     else:
#         print('prime')
#     # print(i)
#     break

## Prime number

# i = 2
# while i < 20:
#     if i%2 ==0:
#         print('Not prime')
#     break
# else:
#     print('prime')
#     i +=1

# start,end = (1,20)
#
# for i in range(start,end+1):
#     if i % 2 == 0:
#         print(i,'==','not prime number')
#         break
# else:
#     print(i,'==',' prime number')

number = int(input('Please enter a number: '))

i = 2

while i<number:
    if number%i == 0:
        print ("Your number is NOT a prime number!");
        break
    else:
        print ("Your number is a prime number!");