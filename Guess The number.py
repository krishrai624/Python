inp = 50
print("Please choose the number between 0 to 100")
guess = 9
done = 0

while(True):
    num = int(input("Enter the guess number: "))
    done = done + 1
    if inp == num:
        print("You have guess in", done, "times.","You are correct")

        break
    else:
        if guess == 0:
            print("Your guess is incorrect and exceeds the limit.\nGame Over")
            print("Number of guess left: ", guess, "\n")
            guess = guess - 1
            break
        else:
            if inp > num:
                print("Your guess is low")
                print("Number of guess left: ", guess, "\n")
                guess = guess - 1
            else:
                print("Your guess is high")
                print("Number of guess left: ", guess, "\n")
                guess = guess - 1
                
----------------------------------------------------------------------------------------------
Output:-

Enter the guess number: 12
Your guess is low
Number of guess left:  9 

Enter the guess number: 2
Your guess is low
Number of guess left:  8 

Enter the guess number: 3
Your guess is low
Number of guess left:  7 

Enter the guess number: 4
Your guess is low
Number of guess left:  6 

Enter the guess number: 64
Your guess is high
Number of guess left:  5 

Enter the guess number: 67
Your guess is high
Number of guess left:  4 

Enter the guess number: 88
Your guess is high
Number of guess left:  3 

Enter the guess number: 56
Your guess is high
Number of guess left:  2 

Enter the guess number: 543
Your guess is high
Number of guess left:  1 

Enter the guess number: 50
You have guess in 10 times. You are correct
