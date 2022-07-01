print("welcome to the calculation universe.")
# This is the faulty calculator which gives students a lesson who want to cheat in exam
# faulty calculation are: 45*3 = 555, 56+9 = 77, 56/6 = 4.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("These are the operators you can use:\n1.Multiplication for m\n2.Addition for a\n3.Divide for d\nEnter the operators: ")

if operator == "m":
    if first_number == 45 and second_number == 3:
        print(555)
    else:
        print("The answer is ", first_number * second_number)
elif operator == "a":
    if first_number == 56 and second_number == 9:
        print(77)
    else:
        print("The answer is ", first_number + second_number)
elif operator == "d":
    if first_number == 56 and second_number == 6:
        print(4)
    else:
        print("The answer is ", first_number / second_number)
else:
    print ("Operators error")
    
----------------------------------------------------------------------------------------------------------------------------------   
Output:-
welcome to the calculation universe.
Enter the first number: 45
Enter the second number: 3
These are the operators you can use:
1.Multiplication for m
2.Addition for a
3.Divide for d
Enter the operators: m
555
