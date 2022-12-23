# multi_line_str = """
# Shakib khan the great make a movie
# with bulbuli, Din the day.
# """
#
# print(multi_line_str)

"""
The mobile is released on 19 octobor.
Its model is samsung note15
camera: 300M
Price in Bd: 500 BDT
"""

released_date = input('Enter mobile released date:')
model = input('Enter Mobile Model:')
camera = input('Enter camera Megapixel:')
price = input('Price in bd:')
print(released_date,model,camera,price)

template = f"""
The mobile is released on {released_date}.
Its model is {model}
camera: {camera}M
Price in Bd: {price} BDT
"""
print(template)