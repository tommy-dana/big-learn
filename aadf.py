number = int(input())
import sys

def collatz(inputnumber):
    global number
    if number == 1:
        print ('You win!')
        return ()

    if  number != 1:
        if (number) % 2 == 0:
            print (number / 2)
            number = (number / 2)
            collatz (int(number))

        if (number) % 2 == 1:
            print (int(3 * number + 1))
            number = (int(3 * number + 1))
            collatz (int(number))

collatz(number)