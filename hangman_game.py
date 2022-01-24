import random
import os

clear=lambda:os.system('clear')

def read():
    words=[]
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        for line in f :
            line.replace('\n','')
            words.append(line) 
    return words 

def choose():

    words=read()
    word_random=(str(random.choice(words))).upper()  
    return word_random  

def show():

    word_random=choose()
    list_word_random=[ i for i in word_random.upper() if i!= '\n']
    word_length= len(list_word_random)
    all_letters1='_ ' *word_length
    all_letters=[ i for i in all_letters1 if i!= '\n' and i!=' ']
    
    cont=10
    while all_letters != list_word_random and cont!=0 :

        clear()
        print('You have a ', +cont, 'oportunities' )
        # print (list_word_random)
        # print(all_letters)  
        # print (word_random)

        print("""¡¡¡WELCOME TO THE HANGMAN GAME !!!
        
        """)
        print(all_letters)

        MENU="""    
        TYPE A LETTER :
        """        
        try:  
            letter_choose= (input(MENU)).upper()
            if len(letter_choose)>1:
                raise ValueError('One latter at a time')                      
        except ValueError as ve:
            print(ve)
            break         
       
        letter_selec=[ i for i in range(len(word_random)) if letter_choose==word_random[i] ] 
        print (letter_selec)
        cont -=1
        for i in letter_selec:
            all_letters[i]=letter_choose     
        
    clear ()
    if all_letters == list_word_random:
        word_random=str(word_random)
        word_random=word_random.upper()
        print('YOU WIN THE WORD WAS :', word_random)
    else:
        lose()

def lose():

    GAME_OVER="""

            !YOU LOSE¡

        Do yo want to try again?

        Yes[1]      Exit[2]

        tipe a number 
        
        """
    try:
        out=int(input(GAME_OVER)) 
        if out ==1:
                run()
        if out ==2:
                clear()
                print("""       
                
                            GAME OVER 
                SNAKE?..SNAKE??...SNAKEEEEEEEE!!
                
                
                """              
                )
        if out!= 1 and out!= 2 :
                raise ValueError()          
    except ValueError:
            clear()
            print ('Choose a corret number 1-2')
        
def run():
    show()
    
if __name__=='__main__':
    run()