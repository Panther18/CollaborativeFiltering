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
        with open(training_file_path, "r", encoding='utf-8') as train_file:
            # Read each entry of the line
            delimiter = ","
            for record in train_file:
                try:
                    split = record.split(delimiter)  # Order is Movie, User and the vote value
                    movie_id = split[0]
                    user_id = 'user_' + split[1]  # Append user_ to the user id
                    vote = split[2].strip('\n')
                    vote.strip(" ")
                except ValueError:
                    continue
                except IndexError:
                    continue
                # Check if the movie is already see, if not, add it to the dictionary
                if not movie_list.__contains__(hash(movie_id)):
                    movie_list[hash(movie_id)] = movie_id  # Add this movie to the movie_list
                # Check if the user is already seen, if not, create a new user object
                if not user_list.__contains__(hash(user_id)):
                    new_user = User.User(user_id)  # Create a new user and assign him an ID
                    new_user.add_movie(movie_id, vote)  # Add this movie to his list and the corresponding vote value
                    user_list[hash(user_id)] = new_user  # Add this user to the user_list
                else:
                    user_list[hash(user_id)].add_movie(movie_id, vote)

    except FileNotFoundError:
        print("Training file not found. Please give the right path")


def intersection(user1_movies, user2_movies):
    return list(set(user1_movies) & set(user2_movies))


def compute_weight(user1, user2):
    user1_movies = user1.get_my_movies()  # Get the list of movies voted by user1
    user2_movies = user2.get_my_movies()  # Get the list of movies voted by user2
    common_movies = intersection(user1_movies, user2_movies)  # Find the common movies between user1 and user2
    if len(common_movies) == 0:  # These two users have no movies in common
        return 0
    else:  # Find the weight between them
        total_sum = 0
        for each in common_movies:
            total_sum += (user1.get_vote(each) * user2.get_vote(each))

        total_sum = total_sum / user1.get_vote_square() / user2.get_vote_square()
        return total_sum


def predict_vote(movie_id, user_id):
    if not user_list.__contains__(hash(user_id)):
        print('Sorry, cannot predict the behavior of new users')
        return
    elif not movie_list.__contains__(hash(movie_id)):
        print('Sorry, cannot predict votes for a new movie')
        return
    else:
        active_user_object = user_list[hash(user_id)]  # Get access to user object
        active_user_hash = hash(user_id)  # Get the hash value of the user
        predicted_vote_value = active_user_object.get_vote_value()  # Add the active users vote value to prediction
        for each in user_list:
            if each != active_user_hash:  # If these two users are different, find the weight between them
                second_user_object = user_list[each]  # Get access to the other(second) user object
                weight = compute_weight(active_user_object, second_user_object)
                if weight == 0:
                    continue
                else:
                    dummy = second_user_object.get_vote(movie_id)  # Get second users vote on this movie
                    dummy -= second_user_object.get_vote_value()  # Get second users vote value
                    dummy *= weight  # Multiply with the weight between second and active user
                    predicted_vote_value += dummy  # Add this to the total sum
            else:
                continue

        return predicted_vote_value

def find_accuracy(test_file_path):
    try:
        with open(test_file_path, "r", encoding='utf-8') as test_file:
            # Read each entry of the line
            delimiter = ","
            hit_sum = 0
            for record in test_file:
                try:
                    split = record.split(delimiter)  # Order is Movie, User and the vote value
                    movie_id = split[0]
                    user_id = 'user_' + split[1]  # Append user_ to the user id
                    vote = split[2].strip('\n')
                    vote.strip(" ")
                    # Predict the vote value of this user on this movie
                    dummy = predict_vote(movie_id, user_id)
                    if dummy == vote:
                        hit_sum += 1
                        print(hit_sum)

                except ValueError:
                    continue
                except IndexError:
                    continue

            print('Final hit sum is: ' + str(hit_sum))

    except FileNotFoundError:
        print("Test file not found. Please give the right path")



if __name__ == '__main__':
    # Read the file and store the user, item and the vote value of user on this vote
    #  User_list and movie_list are used to store the user details and movie details respectively
    user_list = {}
    movie_list = {}
    #  Load the training data and store them
    start_time = time.time()
    load_training_data(sys.argv[1])
    end_time = time.time()
    print(str(end_time - start_time) + ' seconds')

    # Print the list of movies

    print('Move list: ' + str(movie_list.values()))
    # Print the each user details
    for each in user_list:
        user_list[each].ratings()

    """
    Let each user calculate its vote square value
    """
    for each in user_list:
        user_list[each].compute_vote_value()
        user_list[each].compute_vote_square()

    """
    Given an user and a movie, predict the vote value of the user on this movie
    """
    find_accuracy(sys.argv[2])