# take user input of 3 fav movies and store in  list .
"""movie1 = str(input("mv1 : "))
movie2 = str(input("mv2 : "))
movie3 = str(input("mv3 : "))
movie4 = str(input("mv4 : "))
mv = [movie1 , movie2 , movie3 , movie4]
print("fav movie list : " , mv) """
# akka answer
"""movies = []
movies.append(input(" 1 movie : " ))
movies.append(input(" 2 movie : " ))
movies.append(input(" 3 movie : " ))
movies.append(input(" 4 movie : " ))
movies.append(input(" 5 movie : " ))
print(movies)"""

# given list is palindrome
list = [1,2,1]
list_copy = list.copy()
list_copy.reverse()
if(list_copy == list):
    print("this is  a palindrome")
else:
    print("not a palondrome")