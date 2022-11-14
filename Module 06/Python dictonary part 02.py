mobile = {'name': 'samsung',
          'country':'korea',
          'ram': '8GB',
          'rom' : '256GB'}

print('1st = ', mobile)

mobile['rom'] = '128GB'
print('2nd = ', mobile)

mobile.pop('rom')
print('3rd = ', mobile)

mobile.update({'relies year':2020})
print('4th', mobile)