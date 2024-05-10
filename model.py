import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

class Recommender:
    def __init__(self, ratings_file):
        self.ratings_df = pd.read_csv(ratings_file)
        self.model = None

    def preprocess_data(self):
        self.ratings_matrix = self.ratings_df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
        self.user_movie_matrix = self.ratings_matrix.values
        self.user_ids = list(self.ratings_matrix.index)
        self.movie_ids = list(self.ratings_matrix.columns)

    def train_model(self, n_components=50):
        svd = TruncatedSVD(n_components=n_components)
        self.model = svd.fit_transform(self.user_movie_matrix)
        self.similarity_matrix = cosine_similarity(self.model)

    def recommend(self, user_id, top_n=10):
        user_index = self.user_ids.index(user_id)
        similarity_scores = list(enumerate(self.similarity_matrix[user_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        top_users = [self.user_ids[i[0]] for i in similarity_scores[1:top_n+1]]
        return top_users