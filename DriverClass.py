__author__ = 'Panther'

import User
import sys
import time

"""
Colloborative Filtering:
How to predict the vote of a user 'A' on an item 'j'
P(a,j) = vbar + (summation over all users) (k)(w(a,i))(v(i,j)-VIBar)
W(a,i) = (summation over all j)(V(a,j)V(i,j))/(sqrt(k summation over X(V(a,k)^2))(sqrt(k summation over Y(V(i,k)^2))
j --> All items over which both A and I has voted
X --> All items on which 'a' has voted
Y --> All items on which 'i' has voted
For the given training set, calculate the Weight between each users.
Steps to calculate the weight between each users:
    Find the common items between the users. Common items are those items which has been voted by both the users
    Find the V(a,k)^2 for each user, where K is each item that has been voted by an user

How to predict the vote? V(a,j) --> Predicting the vote of user a on item j
    Pre-calculated variables:
        W(a,i) -- weight between each user and 'a'
        Vote of user 'i' on item 'j'
        V(i) --> Votes of user 'i'

How should the data structure support?
    Given an user, find all the items over which he has voted
    Given two users, find all the common items between them
    Given an user and an item, find the value of the corresponding vote
    Weight between each pair of users
"""

def load_training_data(training_file_path):
    try:
        with open(training_file_path, "r") as train_file:
            # Read each entry of the line
            delimiter = ","
            for i in range(1, 300000):
                # For record in train_file:
                record = train_file.readline()
                try:
                    split = record.split(delimiter)  # Order is Movie, User and the vote value
                    movie_id = split[0]
                    user_id = 'user_' + split[1]  # Append user_ to the user id
                    vote = split[2].strip('\n')
                    vote.format()
                except ValueError:
                    continue
                except IndexError:
                    continue
                # Check if the movie is already see, if not, add it to the list
                # Get the index position of the movie
                if movie_list.__contains__(movie_id):
                    movie_index = movie_list.index(movie_id)
                else:
                    movie_list.append(movie_id)
                    movie_index = movie_list.index(movie_id)
                # Check if the user is already seen, if not, create a new user object
                match = [each for each in user_list if each['user_id'] == user_id]
                if len(match) > 0:
                    match[0]['object'].add_movie(movie_index, vote)
                    # user_list[user_index]['object'].add_movie(movie_index, vote)
                else:
                    new_user = User.User(user_id)
                    # Add this movie to the user's list of movies rated
                    new_user.add_movie(movie_index, vote)
                    user_list.append({'user_id': user_id, 'object': new_user})

    except FileNotFoundError:
        print("Training file not found. Please give the right path")




if __name__ == '__main__':
    # Read the file and store the user, item and the vote value of user on this vote
    #  User_list and movie_list are used to store the user details and movie details respectively
    user_list = []
    movie_list = []
    #  Load the training data and store them
    start_time = time.time()
    load_training_data(sys.argv[1])
    end_time = time.time()
    print(str(end_time - start_time) + ' seconds')

    # Print the list of movies
    """
    print('Move list: ' + str(movie_list))
    # Print the each user details
    for each in user_list:
        each['object'].ratings()
    """
    """
    Predict the vote value for the test data
    """
