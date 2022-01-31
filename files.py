import numbers


def read():
    numbers=[]                                                    #how to open files,only read
    with open('./files/number.txt','r',encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():                                                        #How to open files, Append
    names=['Maria','Fernanda']
    with open('./files/names.txt','a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__=='__main__':
    run()