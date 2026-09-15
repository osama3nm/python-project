# Inheritance (الوراثه) & Encapsulation (التغليف/الحمايه) & Abstraction (التجريد)
# Creat class 

class User :
    user_num = 0
    def __init__(self,name,email,age,gender = "male"):      # constructor 
        self.name = name 
        self.email = email
        self.age = age 
        User.user_num +=1         # عدد كم object عملت
        self.__gender = gender    # private (Encapsulation)
    def getting(self):     # بزبط اضيف متغير جوا هاي ال method  وابعثو من خلال الاستدعاء بس راح تكون القيمه محليه وما بقدر اوصللها من خارج هاي ال method 
        return f"My name is {self.name} and I am {self.age} years old ."       

    def has_birthday(self):
        self.age += 1 
    
    def get_gender(self):
        return f"My gender is : {self.__gender}"


# Extend class 
class Customer(User):      # Inheritance 
   def __init__(self,name,email,age):      # constructor 
        self.name = name 
        self.email = email
        self.age = age 
        self.balance = 0
   def set_balance(self,balance):
       self.balance = balance 
    
   def getting(self):   # اذا ما عملت هاي ال method بقدر اسنعمل اللي موجوده بال class user لاني وارثها 
        return f"My name is {self.name} and I am {self.age} years old and my balance is {self.balance} ."       

    





# Initialize User object 
osama = User('osama nemrawi','osamanm21@gmail.com',20)

print(type(osama))                                       # will print <class '__main__.User'>       
print(osama.name,'/',osama.email,'/',osama.age)          # print using variable access 
osama.has_birthday()                                     # method to increment vaiable like (age) by 1 .
print(osama.getting())                                   # print using method 



# Initialize Customer object 
Inher = Customer("noor","noor@gmail.com",25)
Inher.set_balance(98)             # setter        
print(Inher.getting())


 # self._name = name (Protected) بس بوصللها الكلاس تبعي والكلاس الي وارث مني // self.__name = name (Private) // self.name = name (Public)

print(osama.get_gender())        # اذا حطيت كلمه @property فوق ال method الخاصه بنصير نستدعيها بدون الاقواس وبصير استدعائها زي اي متغير بدون اقواس 

# trick to acces to the private variable direct without methods inside class 
print(osama._User__gender)   # HAHAAHAHAHAH
print(User.user_num)      # number of object 


# polymorphic function & class methods & majic methods        