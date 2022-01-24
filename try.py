   
word_random='ana'
letter_choose=input('escribe un numero')
list_word_random=[ i for i in word_random if i!= '\n']
word_length= len(list_word_random)
all_letters='_ '*word_length
all_letters=[ i for i in all_letters if i!= '\n' and i!=' ']
(print(all_letters))


    
letter_selec=[ i  for i in range(len(word_random)) if letter_choose==word_random[i]]
print (letter_selec)

for i in letter_selec:
    all_letters[i]=letter_choose




print(all_letters)

