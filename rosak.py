print("Welcome to AMEER BANK\n\nInsert Your Card")

password=1234
balance=10000
choice=0

pin=int(input("Enter your four digit pin\n"))

if pin==password:

    while choice != 4:

        print("**** Menu ****")
        print("1 == balance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel\n")