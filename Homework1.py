value1=input("Value :  ")
value2=input("Value :  ")
value3=input("Value :  ")
value4=input("Value :  ")
value5=input("Value :  ")


print(f"{type(value1)}  {type(value2)}  {type(value3)}  {type(value4)}  {type(value5)}")

#kullanıcıdan alınan her değer aksi özel olarak belirtilmediği sürece string türündedir.
#Eğer integer, float, complex gibi bir tür alınacaksa veritipi(input("...")) şeklinde olacaktır.
#özel durumlar ve çıktıları şu şekildedir;


value11=int(input("Value int: "))
value21=float(input("Value float: "))
value31=complex(input("Value complex: "))
value41=bool(input("Value boolean: "))

print(f"{type(value11)}  {type(value21)}  {type(value31)}  {type(value41)}")