class BankAccount:
    def __init__(self, Name, mob, Age, Dob, Balance):
        self.Name = Name
        self.mob = mob 
        self.Age = Age 
        self.Dob = Dob 
        self.Balance = Balance

    def Display_info(self):
        print(f"{self.Name}, is {self.Age} years old and user Dob is {self.Dob} and mob is {self.mob} and has blance of {self.Balance} ")

    def Deposit(self, Amount):
        if Amount > 0:
            self.Balance += Amount
            print(f"Deposit {Amount} New Balance is {self.Balance} .  ")

    def withdraw(self, Amount):
        if Amount <= 0:
            print("Invalied Amount. ")
        elif Amount > self.Balance:
            print("Insufficient Blance. ")
        else:
            self.Balance -= Amount
            print(f"{Amount} Withdraw Succsefully new balance is {self.Balance} . ")


print("========================================")
print("     BANK ACCOUNT MANAGEMENT SYSTEM     ")
print("========================================")

Account = []

while True:

    print(
    " A. Create New Account \n" 
    " B. Check Account Details\n"
    " C. Deposit Money \n"
    " D. Withdraw Money \n" 
    " E. Check Account Balance \n" 
    " F. Display All Accounts \n" 
    " G. Exit \n ")

    choice = input("Enter your choice:  ")


    match choice:

        case "A":
            Name = input("Enter Customer Name:")
            mob = input("Enter Mobile Number:")
            Age = input("Enter Age:")
            Dob = input("Enter Date of Birth (DD-MM-YYYY):")
            Balance = int(input("Enter Initial Balance:"))

            user = BankAccount(Name, mob, Age, Dob, Balance)
            Account.append(user)

            # print( [ x.Name for x in Account  ])

        case "B":

            user_mob = input("Enter your Mobile Number : ")

            for x in Account:
                if x.mob == user_mob:
                    x.Display_info()
        case "C":

            user_mob = input("Enter your Mobile Number : ")
            Amount =  int(input("Enter Amount you want to deposit: "))

            for x in Account:
                if x.mob == user_mob:
                    x.Deposit(Amount)

            
        case "D":
            Amount =  int(input("Enter Amount you want to withdraw: "))
            user_mob = input("Enter your Mobile Number : ")
            
            for x in Account:
                if x.mob == user_mob:
                    x.withdraw(Amount)
        case "E":
            user_mob = input("Enter your Mobile Number : ")
                        
            for x in Account:
                if x.mob == user_mob:
                    print(x.Balance)
        case "F":
            for x in Account:
                x.Display_info()
            
        case "G":
            print("Shutting Down the ATM ...............")
            exit(0)
        case _:
            print(  "Invalid Selection.  ")

    print("-" * 40)
