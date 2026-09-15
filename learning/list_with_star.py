l =[]

while True :
    x = input("Enter a num or type q to exit : ")
    if x.lower() == "q":
        break
    x = float(x)
    l.append(x)
print(l)    

def average(li) :

    if len(li) == 0:    # إذا كانت القائمة فارغة، len(li) ستكون 0
        return 0 

    sum = 0
    for i in li :
        sum += i
    avg = sum/len(li)

    return avg

print(average(l))    

# part 2

def average1(*li):   # we use The star to acces to the Tuple  يعني مش بحاجه ل ليست عشان احط الارقام 

    if len(li) == 0:    # إذا كانت القائمة فارغة، len(li) ستكون 0
        return 0 
    
    sum = 0 
    for i in li :
        sum += i
    avg = sum    /len(li)
    return avg 
print(average1(1,2,3,4,5))
print(average1(*l))       # باستعمال ال * قدرت استعمل اللست بس بدونها راح يوخذ الليست كقيمه وحده مش عده قيم وراح يكون غلط

# part 3 (factorial)
x = 5
z = 1
for i in range(x,0,-1):
    z = z*i
print(z)