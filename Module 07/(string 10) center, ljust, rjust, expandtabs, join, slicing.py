str1 = 'Banna'
str2 = 'My name is \t Jobaer '



print(str1.center(10,'*'))  # center

print(str1.ljust(10,'*'))   # ljust

print(str1.rjust(10,'*'))   # rjust

# expandtabs
print(str2.expandtabs(20))
print(str2.expandtabs(30))
print(str2.expandtabs(50))

# join

mylist = ['my', 'name', 'is', 'jobaer' ]
str3 = '_'.join(mylist)
print(str3)

#slacing

str4 = 'Banna'
print(str4[3])


