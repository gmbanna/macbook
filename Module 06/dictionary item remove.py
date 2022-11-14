mobile = {'name': 'samsung',
          'country':'korea',
          'ram': '8GB',
          'rom' : '256GB'}

mobile['releasing year'] = 2020     # notun item add korte pari
mobile['name'] = 'samsung note 2'   # exiting item edit korte pari

print('1st : ',mobile)

mobile.update({'display':'15 inch'}) # notun item add korte pari othoba edit korte pari
print('2nd : ', mobile)

mobile.pop('rom')       # item remove korte pari
print('3rd : ', mobile)

del mobile['name']      # item remove/delete korte pari
print('4th : ', mobile)

mobile.popitem()        # sobar ses remove/delete korte pari
print('5th : ', mobile)

mobile.clear()          # pura dictionary cleare korte pari
print('6th : ', mobile)