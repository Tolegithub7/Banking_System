
# Has a function to show the user details
# Child class  : Bank
# Stores detail about acount balance
# Store detail about amount
# Allow for deposits, withdrawals and viewbalance

# Creating Parent class called : User
class User:
    def __init__(self, name, age, gender): # Hold details about the user
        self.name = name
        self.age = age
        self.gender = gender
    def show_user_details(self):# function to show the user details
        print("Personal Details /n")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
    
Tolosa = User("Tolosa Diriba ", 20, "Male") # creating object
Tolosa.show_user_details()

class Bank(User):# creating child class Bank
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    def deposit(self, amount): # Method that stores the amount of deposit from user
        self.amount = amount
        self.balance += amount
        print("Account balance has been updated: ", self.balance, "$")
    def withdrawal(self, amount):
        self.amount = amount
        if (self.amount > self.balance):
            print("Insufficient funds | Balance available: ", self.balance, "$")
        else:
            self.balance -= amount
            print("Your account balance is now: ", self.balance, "$")
    def viewBalance(self):
        self.show_user_details()
        print("Account balance is: ", self.balance, "$")
        
Jonathan = Bank("Jonathan", 21, "Male") # creating an object
Jonathan.deposit(int(input("Enter the amount to deposit: ")))
Jonathan.withdrawal(int(input("How much money you want withdraw: ")))
Jonathan.viewBalance()