import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.date())
bdate = datetime.date(2006, 7, 27)
print((now.date() - bdate).days)




list1= [1,5,4,10,8,9]
list2 = [10,1,5,9,8,10]
s1 = set(list1)
s2 = set(list2)
print(s1|s2)  # union                  دمج العناصر الموجوده بالمجموعتين بدون تكرار
print(s1&s2)  # intersection           دمج العناصر المشتركه فقط بالمجموعتين 
print(s1-s2)  # difference             شو العناصر اللي بال s1 مش موجوده ب s2 
print(s2-s1)  # difference

# لطباعه التاريخ مع الاسماء مثلا الخميس 30 يونيو بستخدم method (strftime)
now = datetime.datetime.now()
format2 = now.strftime("%A, %B %d, %Y")
print("Time : ", format2)


# شو التاريخ بعد عدد ايام معين 
today = datetime.date.today()
ten_days = datetime.timedelta(days=10)

# جمع المدة مع تاريخ اليوم
future_date = today + ten_days
print(future_date) # سيطبع التاريخ بعد 10 أيام
