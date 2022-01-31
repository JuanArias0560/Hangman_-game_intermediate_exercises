def run ():
    # keys={i for i in range (1,100)}
    # numbers = {i**3 for i in range (1,100)}    #frist try, error.
    # my_dict={f'{keys}':numbers}

    # print(my_dict)

    # my_dict={}                                  #Normal mode 
    # for i in range(1,101):
    #     if i %3 !=0:
    #         my_dict[i]= i**3
   
    # my_dict={i: i**3 for i in range (1,101) if i%3 !=0}  #dictionary comprehensions

    my_dict={i: round(i**0.5,2) for i in range (1,1001)}  #Exercise of dictionary comprehensions
    
    print(my_dict)


if __name__=='__main__':
    run()