
import random
imagine_number = random.randint(1,50)
for trying in range(1,6):
    
    guessing = int(input("Enter your number: "))
    if guessing > imagine_number:
        print("Try a smaller number///")
    elif guessing < imagine_number:
        print("Try a larger number///")
    elif guessing == imagine_number:
        print("You hit our imaginary number", imagine_number)
    else:
        print("Sorry, try one more time!")
    