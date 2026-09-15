# part 1
class member :
      user_num = 0
      def __init__(self,fname,lname):
        self.__firstname = fname # private
        self.lastname = lname
        member.user_num += 1
      def get_name(self):   # getter
        return f"Hello your first name is : {self.__firstname}"
      
      def set_name(self,new_fname):   # setter
         self.__firstname = new_fname
         return new_fname
            

firststudent = member("osama","nemrawi")
secondstudent = member("ali","khaled")
thirdstudent = member("musa",'altamare')
#print(firststudent.firstname)
#print(firststudent.lastname)
print(firststudent.get_name())
print(secondstudent.get_name())

#print(firststudent.__fname) 
print(firststudent.get_name())

print(member.user_num)    # number of student 
firststudent.set_name("noor") # call setter
print(firststudent.get_name()) # call getter



# part 2 


# دراسه  majec methods & polymorphic function & static & class methods 

