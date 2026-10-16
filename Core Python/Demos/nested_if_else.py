gender = input("enter gender (M/F): ")
age  = int(input("enter age: "))

if(gender=="M" or "m"):
    if(age>=21):
        print("you are eligible")
    else:
        print("not eligible")
        
elif(gender=="F" or "f"):
    if(age>=18):
        print("eligible")
    else:
         print("not eligible")
         
else:
    print("invalid")