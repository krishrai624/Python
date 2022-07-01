print("WELCOME TO THE WORDS WORLD.")
print("RIGHT NOW! WE ONLY HAVE 3 WORDS, WE WILL ADD MORE IN FUTURE.\nYOU CAN ONLY USE GIVEN WORDS, THEY ARE: Food, Game, Fan. \nNOTE: WRITE THE GIVEN WORDS AS SHOWN.\n")
dictionary = {"Food":"https://en.wikipedia.org/wiki/Food","Game":"https://en.wikipedia.org/wiki/Game","Fan":"https://en.wikipedia.org/wiki/Fan"}
find = input("Enter the word given above:")
print("Meaning of "+ find +":"+dictionary.get(find))

----------------------------------------------------------------------------------------------------------
Output:-
  
WELCOME TO THE WORDS WORLD.
RIGHT NOW! WE ONLY HAVE 3 WORDS, WE WILL ADD MORE IN FUTURE.
YOU CAN ONLY USE GIVEN WORDS, THEY ARE: Food, Game, Fan.
NOTE: WRITE THE GIVEN WORDS AS SHOWN.

Enter the word given above:Food
Meaning of Food:https://en.wikipedia.org/wiki/Food
