"""
Now in this segment of code, what we are trying to do is that :-
 We are creating a class, where we will be importing the prediction files,
 that we already have pre-processed beforehand. And using that we are going
 to recommend some movie to the users, and based on a movie, recommend some
 users too for the movie.
"""

import csv

class recommend:
    def __init__(self):
        self.movies_file = open("C:/Users/hp/Desktop/PROJECT/MOVIES DATASET/recommend_movies.csv", "r")
        self.users_file = open("C:/Users/hp/Desktop/PROJECT/MOVIES DATASET/recommend_users.csv", "r")
        self.read_movies = csv.reader(self.movies_file, delimiter = ',')
        self.read_users = csv.reader(self.users_file, delimiter = ',')

    def recommend_movies(self, user):
        for i, rows in enumerate(self.read_movies):
            print(i, end = " ")
            if i == user:
                rows_copy = rows
                # rows_copy.pop(0)
                """
                itr = 1
                for movie in rows_copy:
                    print(itr, end = ". ")
                    print(movie)
                    itr += 1
                # This block is for if you want to print here
                # otherwise to use that information anywhere else, I will return the list of movies
                """
                return rows_copy

    def recommend_users(self, movie):
        for rows in self.read_users:
            if rows[0] == "movie_Name":
                continue
            elif rows[0] == movie:
                rows_copy = rows
                rows_copy.pop(0)
                """
                itr = 1
                for user in rows_copy:
                    print(itr, end = ". ")
                    print(user)
                    itr += 1
                # This block is for if you want to print here
                # otherwise to use that information anywhere else, I will return the list of users to recommend
                """
                return rows_copy
                break
            
    def __del__(self):
        self.movies_file.close()
        self.users_file.close()


"""
First we need to choose :-
 If we want to know, which users can be recommended any selected movie
 Or we want to recommend some movies to any user
 For the first option, we need to choose 1 else we would choose 2 
"""

option = int(input())
if option == 1:
    # Now we need to ask for the movie_name
    movie = input()
    rec = recommend()
    movie_list = rec.recommend_users(movie)
    print (movie_list)

elif option == 2:
    # Now we need to ask for the user_ID
    user = int(input())
    rec = recommend()
    user_list = rec.recommend_movies(user)
    print (user_list)
