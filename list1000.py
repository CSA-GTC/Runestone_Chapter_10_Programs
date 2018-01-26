#Grefory Clarke
#Computer Programming
#1/24/2018



def list_quiz_function1(list1):
    input1=input("What name would you like to add to the list?: ")
    list1.append(input1)
    print("""
    1. Yes
    2. No
    """)
    choice1=input("Would you like to add another name to the list?: ")
    if choice1=="1":
        input2=input("What name would you like to add to the list?: ")
        list1.append(input2)
        print(list_quiz_function1(list1))
    elif choice1=="2":
        return list1
        quit()
    else:
        print("Invalid Option")
        print(list_quiz_function1(list1))
        
    
print(list_quiz_function1(["Dan","Lee","Jose","Natasha","Shaiqua"]))
    
