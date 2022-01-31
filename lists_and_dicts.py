from traceback import print_tb


def run():
    my_list= [1,'hellow', True , 4.5]
    my_dict= {'fristname': 'Juan' , 'lastname' : 'arias'}
    
    super_list= [
    {'fristname': 'juan' , 'lastname' : 'arias'},
    {'fristname': 'miguel' , 'lastname' : 'torres'},
    {'fristname': 'pepe' , 'lastname' : 'rodelo'},
    {'fristname': 'susana' , 'lastname' : 'martinez'},
    {'fristname': 'jose' , 'lastname' : 'garcia'}
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'interger_nums':[-1,-2,0,1,2],
        'floating_nums': [1.1,4.5,6.43]
    }

    for key,value in super_dict.items():    #how to print dictionaries and list 
        print(key,'-',value)  

    for value in super_list:
        print(value)

if __name__=='__main__':
    run()