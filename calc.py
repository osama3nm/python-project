class Calculater :
    def __init__(self , name , price ,year = 2006):    # year is defult 
        self.rrnamename = name 
        self.ddprice = price   
        self.year = year  
    def sum(self , num1 , num2):
        print("Sum is : " , num1+num2)

class advanceCalculater(Calculater):
    def power(self,a):
        return a*a 
    def sum(self,num1,num2):
        return num1*num2

Mycalc = Calculater("casio",22,2026)    # constructor 1
Mycalc.sum(4,5)

osamacalc = Calculater("osama",50) # constructor 2
osamacalc.sum(40,20)
print(Mycalc.year)

inhertance = advanceCalculater("noor",20,1995)
print(inhertance.year) 
print(inhertance.power(5))
print(inhertance.sum(9,9))



# try except function (key error & value error & syntax error & runtime error/index error & type error &)




