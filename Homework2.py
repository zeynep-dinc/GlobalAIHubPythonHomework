import datetime

nowYear=datetime.date.year()
dizi=[]
dizi[0]=input("First Name: ")
dizi[1]=input("Last Name: ")
dizi[2]=int(input("Age: "))
dizi[3]=int(input("Date of birth (just year): "))
for x in range(len(dizi)):
    print(dizi[x])

if(nowYear-dizi[3]==dizi[2]):
    if(dizi[2]>=18):
        print("You can go out to the street.")
    else:
        print("You can't go out because it's too dangerous!")
else:
    print("You should to control your age or your date of birth year!")