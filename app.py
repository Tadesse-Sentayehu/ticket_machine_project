
from ticket_machine_functions import wait
from ticket_machine_functions import wait2
from ticket_machine_functions import wait3
from ticket_machine_functions import messages
from utiles import countdown


message = "Your+ number is:"
lists = ["c", "p", "ph"]
idList = [346369507, 342650983]
print("**** Welcome to our pharmacy (drugstore):**** ")
stop = ""
count=0
id = int(input('Enter id '))
while count < 3:
    if id == idList[0] or id == idList[1]:
        clientChoice = input("""
              choose 'C' for cosmetics
              choose 'P' for perfumery
              choose 'Ph' for pharmaceutical
              """)
        if clientChoice == lists[0]:
            print(message, "C - ", next(wait))
            messages()
        elif clientChoice == lists[1]:
            print(message, "P - ", next(wait2))
            messages()
        elif clientChoice == lists[2]:
            print(message, "PH - ", next(wait3))
            messages()
        else:
            print("Sorry, You didn't enter a valid input to visit, Please try again:")
            print("******************************************")
        stop = input("Do you want another ticket? ")
        if stop != "yes":
            break

    else:
        count1 = 0
        while count1 < 3:
            x =input('Access denied. Try again.')
            count1 += 1
        # count += 1
        countdown(10)
        break