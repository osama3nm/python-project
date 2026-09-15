
# Creat dictionary 
person = {
    "first_name " : 'osama ' ,
    "last_name " : 'nemrawi ' ,
    "age " : 20 
    }

person2 = dict(            # use constructor
    first_name = 'osama' ,
    last_name = 'nemrawi' ,
    age = 20
    )
print(person ,"  ",type(person))
print(person2," ",type(person2))

# Get value 
print(person['first_name '])         # the more common way 
print(person.get('last_name '))      # other way

# Add key/value 
person['phone'] = '079654024'
print(person['phone'])

# Get dict keys 
print(person.keys())       # components of array

# Get dict values
print(person.values())     # data of array

# Get dict items 
print(person.items())      # details of array (components & data) 

# Copy dict 
person3 = person.copy()
person3['city'] = 'irbid'
print(person3)

# delete item 
del(person3['age '])       # the more common way 
person3.pop('phone')       # in another way
print(person3)

# Clear 
person3.clear()
print(person3)   # no output just {}

# Get length of dic 
print(len(person2))

# List of dictionary 
people = [
       {'name' : 'osama' , 'age' : 20} ,
       {'name' : 'noor' , 'age' : 30}
    ]
print(people)
print(people[1]['name'])

# nested dict 
family1 = {"father" : 'ali' ,
 "son" : "osama",
 "phone" : "0796540024"
}
family2 ={"father" : 'mohammed',
 "son" : 'saaed',
 "phone":"078854201"
}
allfamily = {
"family1":{"father" : 'mohammed',
"son" : 'saaed',
"phone":"078854201"} ,
"family2":{"father" : 'mohammed',
"son" : "saaed",
"phone":"078854201"}
}

#print(dir(allfamily))                all items of dict 
print(allfamily["family2"]["son"])

