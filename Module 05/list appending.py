name = ['Banna', 'Tuhin', 'tasfiya']

# name.append('Taslima')        # variable vetore notun kisu add korte use kora hoi append korle list er vertor sobar sese jog hoi
# print(name)

# name[0] = 'Jobaer'
# print(name)


# name[2] = 'mahreen'
# print(name)

ch = 'y'
names = []
while ch.lower() == 'y':
    name = input('What is your name: ')
    names.append(name)
    ch = input('Do you want to continue (y/n): ')

    print(names)



