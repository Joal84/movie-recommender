import pandas as pd
import numpy as np
from joblib import load
from fuzzywuzzy import process
from tmdbv3api import TMDb
from tmdbv3api import Movie


# API Auth
tmdb = TMDb()
tmdb.api_key = '9f81e2a078b09eefd55e3618c30ee8b1'
tmdb.language = 'en'
tmdb.debug = True

# DF Merging
movies_df = pd.read_csv(
    "../data/movies.csv", index_col=0)
links = pd.read_csv(
    "../data/links.csv", index_col=0)
ratings = pd.read_csv(
    "../data/ratings.csv", index_col=1)

merged_df = pd.merge(movies_df, ratings, left_index=True, right_index=True)
merged_df = pd.merge(merged_df, links, left_index=True, right_index=True)

merged_df.isna().sum()
merged_df["tmdbId"] = merged_df["tmdbId"].fillna(0)
merged_df.reset_index()

# DF Pivoted
wide_df = pd.pivot_table(merged_df, values="rating",
                         index="userId", columns="title")
wide_df.dropna(axis=1, thresh=20, inplace=True)
wide_df.fillna(wide_df.mean(), inplace=True)

model = load("./static/model/model")

Q = model.components_
movies_name_list = wide_df.columns


def get_recommendation(user_rating):

    new_dic = {}
    empty_list = [np.nan]*len(movies_name_list)
    empty_dic = dict(zip(movies_name_list, empty_list))

    for movie_name, rate in user_rating.items():
        best_match, score = process.extractOne(movie_name, movies_name_list)
        if score > 70:
            new_dic[best_match] = int(rate)

    for movie, rate in new_dic.items():
        empty_dic[movie] = int(rate)

    new_user_df = pd.DataFrame(
        list(empty_dic.values()), index=movies_name_list)
    new_user_df.fillna(0, inplace=True)
    new_user_df = new_user_df.T

    P = model.transform(new_user_df)

    prediction = np.dot(P, Q)
    recommendations = pd.DataFrame(prediction, columns=wide_df.columns)

    user = list(new_dic.keys())

    recommendations.drop(user, axis=1, inplace=True)
    recommendations = recommendations.T

    recommendations.columns = ["predicted_rating"]

    return recommendations.sort_values(by="predicted_rating", ascending=False)[:8]


def get_movie_data(recommendation_list):
    database = Movie()
    movie_dic = {}
    for movie in recommendation_list:
        id = int(merged_df.loc[merged_df["title"] == movie]["tmdbId"].iloc[0])
        m = database.details(id)
        movie_dic[movie] = [m.title,
                            m.overview,
                            m.poster_path]
    return movie_dic
