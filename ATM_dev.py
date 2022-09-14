print("Welcome to AMEER BANK\n\nInsert Your Card") # bank by ameerulfaiz

password=1234
balance=10000 #ini duit kamu
choice=0

pin=int(input("Enter your four digit pin\n"))

if pin==password:

    while choice != 4:

        print("**** Menu ****")
        print("1 == balance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel\n")

        choice=int(input("\nEnter you option:\n"))

        if choice==1:
            print("Balance = RM", balance)

        elif choice==2:
            dep=int(input("Enter your deposit: RM"))
            balance += dep
            print("\n deposited amount: RM" ,dep)
            print("balance = RM", balance)
        
        elif choice==3:
            wit=int(input("Enter the amount to withdraw: RM"))
            balance -= wit
            print("\nwithdrawn amount: RM" ,wit)
            print("balance = RM", balance)
        
        elif choice==4:
            print("\n Session Ended!! Goodbye")

        else:
            print("\nInvalid Entry!!")
        
        

else:
    print("Pin Incorrect!! Try again")
