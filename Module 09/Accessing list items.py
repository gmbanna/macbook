# Accessing list item
#               0        1         2        3           4
name_list = ['jobaer', 'banna', 'tuhin', 'tasfiya', 'mahreen']
#              -5          -4        -3       -2          -1

print(name_list[3])
print(name_list[0])
print(name_list[-1])
print(name_list[-5])

print(name_list[1:3])  # Last element will be excluded

print(name_list[0:3])  # Last element will be excluded

print(name_list[:3])  # Last element will be excluded
print(name_list[3:])  # Last element will be excluded
print(name_list[ -4:-2 ])  # Last element will be excluded
print(name_list[ :-2 ])  # Last element will be excluded


if 'jobaer' in name_list:
    print('Exists')
else:
    print('Not found')





