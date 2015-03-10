__author__ = 'Panther'


class User:

    def __init__(self, id):
        self.id = id
        self.movie_votes = {}
        self.vote_value = 0
        self.vote_square = 0
        self.user_weights = {}

    def print_your_id(self):
        print(self.id)

    def add_movie(self, movie_id, vote):
        self.movie_votes[movie_id] = vote

    def ratings(self):
        print('ID: ' + str(self.id), end=': ')
        print(self.movie_votes)

    def compute_vote_value(self):
        no_of_movies_watched = len(self.movie_votes)
        vote_value = 0
        for each in self.movie_votes:
            vote_value += float(self.movie_votes[each])

        self.vote_value = float(vote_value/no_of_movies_watched)

    def compute_vote_square(self):
        vote_square = 0
        for each in self.movie_votes:
            vote_square += float(pow(float(self.movie_votes[each]), 2))

        self.vote_square = float(vote_square)

    def set_user_weight(self, user_id, weight_value):
        self.user_weights[user_id] = weight_value

    def get_user_weight(self, user_id):
        if self.user_weights.__contains__(user_id):
            return self.user_weights[user_id]
        else:
            return 0

    def get_my_movies(self):
        return [each for each in self.movie_votes]

    def get_vote(self, movie_id):
        if self.movie_votes.__contains__(movie_id):
            return float(self.movie_votes[movie_id])
        else:
            return 0

    def get_vote_square(self):
        return float(self.vote_square)

    def get_vote_value(self):
        return float(self.vote_value)