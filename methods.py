
import numbers


print("Hello World")

# x = 10         # int 
# y = 1.5        # float 
# name = "osama"    # string   
# is_cool = True # bool 


# Multiply Assignment 
x , y , name , is_cool = ( 14 , 5.3 , 'osama' , False)
print(x,y,name,is_cool)

sum = x + y 
print(sum)


#casting 

print(type(x))
x = str(x)
print(type(x))


print(type(y) , y)
y = int(y)
print(type(y) , y)

z = float(y)
print(z)


#concatenate  تركيب اسماء او متغيرات

first_name = "osama"
last_name = "nemrawi"

full_name = first_name +" "+ last_name
print(full_name)

points = 55
message = "the points his person is : " + str(points)
print(message)


#string formatting 
name = "osama"
number_of_children =  3 
message = f"heloo {name} , are you have {number_of_children} children ? "
print(message)

#string method  (function)
user_input = " Osama06@Gmail.Com  "
print(user_input)
clean_email = user_input.strip()                                      # بشيل الفراغات من النص 
print(f"After remove the space : '{clean_email}'")      
final_email = clean_email.lower()                                     # بخلي كل الاحرف small 
print(f"The Email After Modification : '{final_email}' ")
company_email = final_email.replace("gmail.com" , "company.com")      # ببدل النص بنص اخر 
print(f"The Email After Replace : {company_email}")
print(f"The Email After Modification first character :{company_email.capitalize()}")     # بخلي اول حرف  capital 

# طريقه ثانيه في سطر واحد وطباعه وحده 
row_input = "  Ahmad95@GMAIL.com  "
print(row_input)
perfect_email = row_input.strip().lower()
print(f"The Final Email For Database :{perfect_email}")

word = "bananaa" 
sub = 'a'
print(f"number of character (a) is : {word.count(sub)}")       # عد مرات تكرار حرف معين في النص 

print(f"find location is character (b) in the word (like is array) : {word.find('b')}")  #يطلع موقع حرف معين في النص ولو مش موجود يطلع -1


# creat list 
number = [1,2,3,4,5,6]              # more common to creat array 
number2 = list((1,2,3,4,5,6))       # othar way 
print(number,number2)

fruits = ['Apples','Oranges','Grapes','Pears']
print(fruits[1]," ",fruits[0])
print(f"To find the (lenth) of the array is : {len(fruits)}")   # method to length
fruits.append('Mangos')             # add at the last of array
print(f"length After adding new fruit : {len(fruits)}")
fruits.remove('Oranges') 
fruits.remove('Apples')
print(f"array After remove 2 fruits : {fruits}")
fruits.insert(1,'banana')           # Add to a specific location
print(f'Ater Adding to a specific location : {fruits} ')

deleted_fruit = fruits.pop(1)       # To remove from array & using in another variable (like refrence) .
print(f"deleted fruit is : {deleted_fruit}")
print(f"The array After Pop : {fruits}")

fruits.reverse()                    # Method To reverse the array
print(fruits)

numbers = [4,5,9,0,11,-2,3,20]
numbers.sort()                       # to sort the array
print(numbers)

numbers.sort(reverse=True)           # to reverse sort the array 
print(numbers)                       

numbers[1] = -10                     # to change the value from a specific location
print(f"the array After change the value : {numbers}")



# creat taple 
days_of_the_week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')      # تستعمل لأشياء ثابته ممنوع التعديل عليها سواء حذف او اضافه مثل ايام الاسبوع او احداثيات موقع معين
print(f"days_of_the_week is : {days_of_the_week}")



# creat set 
fruits_set = {'Apples','Oranges','Grapes','Apples','Pears'}     # لا تكرر المدخلات اذا تكررت عند الطباعه وتأخذ فقط نسخه وكمان ما الها ترتيب محدد فكل طباعه لها نتيجه مختلفه 
print(f"The set is : {fruits_set}")
# cheack if in set 
print("Apples" in fruits_set )              # the output True or False
# to delete set 
del fruits_set
#print(fruits_set)   # is not defineddd 