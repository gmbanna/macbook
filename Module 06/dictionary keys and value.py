mobile = {'name': 'samsung',
          'country':'korea',
          'ram': '8GB',
          'rom' : '256GB'}
print('1st : ',mobile.keys())

print('2nd : ',list(mobile.keys()))

print('3rd : ',mobile.values())

print('4th : ',list(mobile.values()))

if 'ram' in mobile.keys():
    print('you can change random access memory')
if '8GB' in mobile.values():
    print('you can change the value')
print(mobile.items())






