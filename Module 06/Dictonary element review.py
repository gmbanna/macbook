car = {
    'brand':'bmw',
    'model': '2020'

}

print('Previous model and brand: ',car['model'], car.get('brand'))
# car['modeldel'] = 'ford'
# car.update({'model':2022})
# car['model'] = '2022'
# car.get('model')
# car.popitem()
# add new item
car['country'] = 'korea'
# car.pop('model')
car.popitem()
print('new',car)