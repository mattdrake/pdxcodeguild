__author__ = 'drake'
#reques input from user for any number
question = input("Enter a number. ")

#created variable for incrementing input from user
num = -1

#create loop to count from zero to user input number
while question > num:
#incrementing by one
    num += 1
#test if number is a multiple of both 3 and 4 not including zero
    if num % 3 ==0 and num % 4 == 0 and num != 0:
        print('\033[1;32mfizzbuzz\033[1;m')
#test if number is a multiple of 3 not including zero
    elif num % 3 == 0 and num != 0:
        print('\033[1;31mfizz\033[1;m')
#test if number is a multiple of 4 not including zero
    elif num % 4 == 0 and num != 0:
        print('\033[1;34mbuzz\033[1;m')
#otherwise print number incremented
    else:
         print(num)




