list_name=[]
list_grade=[]
data={}
def add():
    while (1):
        name=input("Enter the name:")
        list_name.append(name)
        grade=input("Enter the grade:")
        list_grade.append(grade)
        print(list_name)
        print(list_grade)
        a=input("Continue adding data? (Y/N):")
        if a=="Y":
            continue
        else:
            break
    
    data={list_name[i]:list_grade[i] for i in range(len(list_name))}
    print(data)
    
    search=input("Enter the name of the student whose grade is required:")
    print("The grade obtained by ", search, "is ", data[search])
    
    b=input("Would you like to add grades for a student?(Y/N)")
    if b=="Y":
        add()
    else:
        print("Thank you!")
    

add()

#Providing the user an option to add or search
while(1):
    option=input("Would you like to 1. search a student grade or 2. add to the list?")

    if option=='1':
        search=input("Enter the name of the student whose grade is required:")
        print("The grade obtained by ", search, "is ", data[search])
    elif option=='2':
        add()
        





    
    
    
    
    


