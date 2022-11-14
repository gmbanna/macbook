names = ['salman khan', 'sahrukh khan', 'saif ali khan']
print('first list:', names)

names.append('amir khan')
print('second:',names)

names.insert(0,'sakib khan')
print('third: ', names)

names.insert(3,'sakib khan')    # variable vetore notun kisu add korte use kora hoi
print('forth', names)

del names[3]        # variable vetore thaka index number remove korte use kora hoi
print('fifth', names)

names.pop(0)        # variable vetore thaka index number remove korte use kora hoi
names.remove('amir khan')
print('sixth', names)

names.clear()       # list clear korar jonno use kora hoi
print(names)