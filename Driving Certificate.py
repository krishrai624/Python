print("Welcome to the driving eligible certificate.")
person_age= int(input("Enter your age: "))

if person_age>18:
    print("You can drive.\nCongrats! For driving certification.")
elif person_age==18:
    print("You are 18 so we can't decide that you can drive.\nPlease, come to our office physically to know more information.")
else:
    print("You can't drive.\nSorry! you can't get driving certificate.\nPlease come after becoming 18 years old or later.")

---------------------------------------------------------------------------------------------------------------------------------------------------
Output:-

Welcome to the driving eligible certificate.
Enter your age: 12
You can't drive.
Sorry! you can't get driving certificate.
Please come after becoming 18 years old or later.
