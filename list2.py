#Gregory Clarke
#Computer Programming
#1/17/2018

def list_2():
    info=["Gregory", "13", "September", "2002", "Austin"]
    index=0
    for x in info:
        print(info[index])
        index+=1
    print("I was born in "+info[4])
    print("The month was "+info[2])
    info[2:2]=["Neal"]
    print(info)

list_2()
