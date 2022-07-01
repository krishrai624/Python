numbers = [3,4,56,75,82,1,5,]
print("Numbers above 6 are given below:")
for item in numbers:
    if str(item).isnumeric() and item > 6:
        print(item)
        
-------------------------------------------------------------------------------------------------------------------       
Output:-
Numbers above 6 are given below:
56
75
82
