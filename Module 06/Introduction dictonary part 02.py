mobile = {'name':'Samsung note 10',
          'brand':'Samsung',
           'country':'Korea',
            'camera':'10 MP',
            'ram':'8GB',
            'rom':'256GB'}

# print(mobile['ram'])
# print(mobile.get('rom'))

print(mobile)
mobile['rom'] = '64 GB'
# mobile['camera'] = '15MP'
mobile.update({'camera': '15MP'})
print('after update: ', mobile)
