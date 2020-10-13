from random import randrange
with open("C:\Bojan\_imena.txt", "r") as names: 
    lista = []
    for name in names.readlines():   
        lista.append(name[:-1])
    print(lista)
    print(len(lista))
    salary = []
    for salary in range(50):
        salary.append(randrange(1500, 15000))
    print(salary)
    for name,salary in zip(lista, salary):
        if salary > 12000 and salary < 15000:
            print("{}: {}.".format(name,"Executive" ))
            print("salary:{} ".format(salary))
            print("*"*30)
        elif salary > 9000  and salary < 12000:
            print("{}: {}.".format(name, "Higher Manager"))
            print("salary:{}".format(salary))
            print("*"*30)
        elif salary > 7000  and salary < 9000:
            print("{}: {}.".format(name, "Middle Manager"))
            print("salary:{}".format(salary))
            print("*"*30)
        elif salary > 5000  and salary < 7000:
            print("{}: {}.".format(name, "Low Manager"))
            print("salary:{}".format(salary))
            print("*"*30)
        elif salary > 3000  and salary < 5000:
            print("{}: {}.".format(name, "Low Manager"))
            print("salary:{}".format(salary))
            print("*"*30)
        elif salary < 3000:
            print("{}: {}.".format(name, "Intern"))
            print("salary:{}".format(salary))
            print("*"*30) 
        else:
            print("Not defined")
        
        
    
