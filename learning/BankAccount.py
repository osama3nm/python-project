class BankAccount :
    customers = 0
    total_savings = 0        # اجمالي المدخرات 
    def __init__(self,id=0,balance=0,iban=""):      # iban : number of bank account like(5478-8569-5847-9658)
        self.__id = id
        self.__balance = balance         
        self.__iban = iban
        BankAccount.customers += 1
        BankAccount.total_savings +=balance

    def set_id(self,id):
        self.__id = id 

    def get_id(self):
        return self.__id
    
    def deposit(self):        # ايداع
        check = int(input("Please enter the ID number to verify your account name :"))
        bal = float(input("Enter the amount you wish to deposit :"))
        if check == self.__id :
            if bal > 0 :
                print("Deposit completed successfully ✅") 
                self.__balance += bal 
                BankAccount.total_savings += bal
                return True
            else :
                print("\aerror ❎ : The deposit amount must be higher than zero !!")
                return False
        else :
            print("Error,try again enter the id :")



    def withdraw(self):       # سحب 
      check = str(input("Please enter your iban to verify that you are the account owner :"))
      bal = float(input("Enter the amount you wish to withdraw :"))
      if check == self.__iban :
            if bal > self.__balance :
                print("\aerror ❎ : Insufficient funds to complete the transaction !!")
                return False 
            elif bal <= 0 :
                print("\aerror ❎ : The withdrawal amount must be greater than zero !!")
                return False
            else :
                print("Withdrawal completed successfully ✅")  
                self.__balance -= bal  
                BankAccount.total_savings -= bal
                return True
      else :
          print("Error,try again enter the iban :")



    def display_balance(self,name):
        check = int(input("Please enter the ID number to verify your account name :"))
        if check == self.__id :
            print(f"Hello M'r {name} your balance in your bank account is :{self.__balance} .")
        else :
            print(f"Error,try again enter the id :")

    
    def set_iban(self,iban):
        self.__iban = iban
    def get_iban(self):
        return self.__iban
    

number_customers = {}     # dictionary to acces to the customers 
def create_customer(customer_name,id=0,balance=0,iban=""):              # method to creat new customer when i want
    if customer_name in number_customers :
        print("\aerror ❎ : The customer's name already exists, edit it 👍")
    else :
        number_customers[customer_name] = BankAccount(id,balance,iban)   # create a customer and storage him in dictionary 


def operations():
    chose_the_operation = int(input("Chose of them operations :\n1️⃣  .(diposit)\n2️⃣  .(withdraw)\n3️⃣  .(display_blance) "))
    if chose_the_operation == 1 :
        name = str(input("ُEnter the account name :"))
        number_customers[name].deposit()
    elif chose_the_operation == 2 :
        name = str(input("ُEnter the account name:"))
        number_customers[name].withdraw()
    elif chose_the_operation == 3 :
        name = str(input("ُEnter the account name:"))
        number_customers[name].display_balance(name)
    else :
        print("Invalid operation")





# to create Account by using method .....
create_customer("zaid",2054688541,10,"2554-7745-8896-1124") 
create_customer("osama",200255546,1000,"5548-5586-9856-3317")
create_customer("noor",44758996,500,"8854-3321-4410-2707")
# print(number_customers[0].display_balance())    # using list[]  


# create customers without method 
tariq = BankAccount(balance=100)     # بزبط احدد متغير واحد واوديلو قيمو من خلال انو احط اسم هاض المتغير 
ahmad = BankAccount(2044568,100,"2556-9665-5447-7885")

print(f"number of Customers is : {BankAccount.customers}")
print(f"Total savings is : {BankAccount.total_savings}")

operations()
