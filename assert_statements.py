def divisiors(num):
    
    divisors =[]    
    for i in range(1,num + 1):
        if num % i == 0:                          #the red dot is a breakpoint for vscode debugging
                divisors.append(i)
    return divisors
  

def run ():

    num=input('Type a number : ')
    
    assert int(num)>0 and int(num)>0, 'type a positive number'
    print(divisiors(int(num)))
    print('the program ended')        
    


if __name__=='__main__':
    run()