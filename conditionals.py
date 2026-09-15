
x = 10 
y = -5 

if x > y :
    print(f"{x} greater than {y}")
elif x < y :
    print(f"{y} greater than {x} ")
else:
    print(f'{y} is equal to {x}')


# nested if 
if x > 2 :
  if x <= 10 :
    print(f"{x} is greater than 2 and less than or equal to 10 ")

# and & or 
score = 90
if score >=90 and score <=99 :
   print(f"The score of student is : {score}")

if score >=90 or score >=84 :
   print(f"score is {score}")

if not (score == 90 or score > 90) :
   print(f"score less than 90")
   

