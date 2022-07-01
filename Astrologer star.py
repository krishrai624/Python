print("Welcome to the star maker.")
star = int(input("Enter the number for rows: "))
print("True for 1 which give increasing star and False or 0 which give decreasing star.")
boolean = int(input("Press one or zero: "))
num = bool(boolean)
if num == 1:
    for i in range(0, star+1):
        print("* "* i)
else:
    for i in range(star,0,-1):
        print("*" * i)
 -----------------------------------------------------------------------------------------------------------------------------
 
Output:-
 
Enter the number for rows: 5
True for 1 which give increasing star and False or 0 which give decreasing star.
Press one or zero: 0
* * * * * 
* * * * 
* * * 
* * 
* 
