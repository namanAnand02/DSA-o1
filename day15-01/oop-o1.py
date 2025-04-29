## OOP - it is a special way of writing the code in which allows us to create our own datatypes. 

## 1. classes 
## 2. objects 
## 3. Inheritance 
## 4. polymorphism 
## 5. abstraction 
## 6. Encapsulation 


## classes - blueprint of objects - rules and regulations based on which objects are created. 
## Objects - an instance of class 


## think of cars as a class - maruti suzuki, etc all inidividual cars can be called as its objects 

## we define set of rules and regulations inside class which are meant to be followed while creatingg objects of that class. 
## rem - code of class doesnt run on its own - they are only meaningful when an object is created out of it. 


## think of it like this - we made a basic layout of car - how a normal basic level car should have (like having 4 wheels is must, etc) - but if none individuals are to be carved out based on those architecture or anything, it is of no use. 

## class syntax  --> class ClassName (note: ClassName should follow pascal convention )
## object syntax --> objectName = ClassName()


## lets build a simple - ATM - machine demo code base 



## ~~~~~~~~~~ ATM machine demo code ~~~~~~~~~~~~


class Atm: 
    ## constructor 
    ## constructor is also a function but a special type of function which gets called automatically when we create any object of the class. 
    ## with it- all its props and functions inside of it gets executed automatically. 


    def __init__(self):
        ## what are the basic things req for an atm 
        ## think it like that- what are the basic things req from the user when he goes to use an atm. 
        self.pin = " "
        self.balance = 0

        self.menu() ## we want manu fucntion to get executed as soon as we create an object - meaning a user has come 
        ## thats why we have out this menu function inside of this constructor.


        ## we initialised an empty pin and 0 balance initially. 

    ## next - we define a function menu - which will showcase few options to the user when he visits this atm machine 
    def menu(self):
        ## when ever we create any function inside a class, it has to have the self as one of the paramter. 
        user_input = input(
            """
            Hi, How can i help you? 
            1. press 1 for create pin 
            2. press 2 for create a new pin 
            3. press 3 for check balance 
            4. press 4 for withdaw 
            5. press anything else to exit 
            """
        )

        if user_input == "1":
            ## create pin 
            self.create_pin()
            # pass 
        elif user_input == "2":
            ## create new pin 
            self.new_pin()
            # pass 
        elif user_input == "3":
            ## check balance 
            self.check_balance()
            # pass
        elif user_input == "4":
            ## withdraw 
            self.balance_withdraw()
            # pass 

        else: 
            exit()





    ## next step - lets create this individual functions which serves as per what the user enters 
    def create_pin(self):
        user_pin= input("enter your pin: ")
        user_balance = int(input("enter your balance: "))
        self.pin = user_pin
        self.balance = user_balance
        print("pin created successfully")
        self.menu()



    def new_pin(self):
        user_pin = input("enter your old pin: ")
        if (user_pin == self.pin):
            new_pin = input("enter new pin: ")
            self.pin = new_pin

            print("new pin generated successfully")
            self.menu()
        else:
            print("wrong old pin")
            self.menu()


    def check_balance(self):
        user_pin = input("enter your pin : ")
        if user_pin == self.pin:
            print("your balance is: ", self.balance)

            self.menu()

        
        else:
            print("pin is wrong")
            self.menu()


    def balance_withdraw(self):
        user_pin = input("enter your pin: ")
        if user_pin == self.pin:
            ## allowed to withdraw

            amount = int(input("Enter the amount you want to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                ## self.balance already holding the int amount - so does this amount. so we can easily sub that. if any of it were string, we couldn't. 

                print("withdraw successful, rest balance is: ", self.balance)
                # self.menu()
            else:
                ## he asked from money more that what is in his account
                print("stay in your linit, young man! ")
                # self.menu()
                

        else:
            print("pin is wrong")
            # self.menu()

        ## lets final call this menu function here - outside of all if_else 
        self.menu()


    
obj = Atm()


        












