__author__ = 'drake'

a = 20
b = 0


while a > b:
    if a != 10:
        print(a)
    if a % 5 == 0:
        if a == 10:
            print('halfway done')


        a -= 2

    else:
        a -= 1
else:
    print('all done')









