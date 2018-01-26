#Gregory Clarke
#Computer Porgramming
#1/22/2018

def list_function():
    myList=[]
    myList.append(76)
    myList=myList+[92.3]
    myList.append("hello")
    myList=myList+[True]
    myList.append(4)
    myList=myList+[76]
    print(myList)

def random_numbers():
    import random
    random_integers=[]
    for x in range(100):
        x=random.randint(0,1000)
        random_integers.append(x)
    listSum=sum(random_integers)
    listLen=len(random_integers)
    listAverage=listSum/listLen
    return listAverage
    
list_function()
print(random_numbers())

