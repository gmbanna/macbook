# 'spilt', 'rspilt', 'lspilit', 'spilitlines'

str1 = " hello, my name is banna, i am 37 years old."
str2 = " hello\n, my name is banna,\n i am 37 years old."

print(str1.split())
print('2nd',str1.split(',', maxsplit=1))

print(str2.splitlines())

# # str4 = "In order to get the best virtual data rooms for the specific business,\n responsible managers should consider such steps that should be made"
str3 = " Hi, My name is banna, i love my country"

str4 = " Hi, My name is banna, \n i love my country"

print(str3.split())
print(str3.split(',', maxsplit=2))
print(str3.splitlines())
print(str4.splitlines())






