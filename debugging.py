from multiprocessing.sharedctypes import Value


def divisiors(num):
    
    divisors =[]
    try:
        if num<0:
            raise ValueError('type a positive number')
        for i in range(1,num + 1):
            if num % i == 0:                          #the red dot is a breakpoint for vscode debugging
                divisors.append(i)
        return divisors
    except ValueError as ve:
            print(ve)
            return False


def run ():

    try:
        num=int(input('Type a number : '))
        print(divisiors(num))
        print('the program ended')        
    except ValueError:
        print('you must enter a number')


if __name__=='__main__':
    run()