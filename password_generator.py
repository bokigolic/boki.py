import string as s
from random import randrange, shuffle

def generate_upper_letter():
    return s.ascii_uppercase[randrange(26)]

def generate_lower_letter():
    return s.ascii_lowercase[randrange(26)]

def generate_digit():
    return str(randrange(10))

def generate_spec_character():
    return s.punctuation[randrange(32)]

def main():
    name_site = str(input("What is name of the site: "))
    user_name = str(input("What is your user name: "))    
    int_input = ''
    while type(int_input) == str or int(int_input) not in range(7,16):
        try:
            int_input = int(input("How many caracters: "))
        except:
            print("can't be converted")
    functions = [generate_upper_letter, generate_lower_letter, 
                  generate_digit, generate_spec_character]
    pw = ''
    for x in range(14):
        pw +=  functions[randrange(4)]()
    print("\n")
    print("Yoyr password is: ", pw)
    
    with open (r"C:\Bojan\passwordi.txt", "a") as code:
        print("name site:" , name_site, "user_name: ", user_name, "password", pw, file = code)
        
main()
    

  




    
    
    
    