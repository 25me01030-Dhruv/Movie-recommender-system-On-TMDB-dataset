{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cb52801-4739-4f47-9d38-dd9bd905c3d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
import pickle
import subprocess
import json
import streamlit as st
import pandas as pd
import numpy as np

import requests

TMDB_API_KEY = "449e1a76b768d89c84fce8bc515256ca"

@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_l = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movie = []
    recommended_movie_poster = []

    for i in movie_l:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie, recommended_movie_poster


similarity = pickle.load(open("similarity.pkl", "rb"))
st.title("Movie recommender system : :green[By Dhruv Barnwal]", anchor=None, help=None, width="stretch",
         text_alignment="center")

movies = pickle.load(open("movies.pkl", "rb"))
movie_list = movies['title'].tolist()

selected_movie = st.selectbox('Please select a movie', movie_list)

if st.button("Recommend"):
    recommended_movies, recommended_movie_posters = recommend(selected_movie)
    row1 = st.columns(5)
    for i in range(5):
        with row1[i]:

         poster = recommended_movie_posters[i]
         if (poster):
           st.image(poster)
         else :
            st.write('No poster available for this movie :(')
         st.button(recommended_movies[i], key=f"row1_btn_{i}")

    row2 = st.columns(5)
    for i in range(5,10):
        with row2[i-5]:

         poster = recommended_movie_posters[i]
         if (poster):
            st.image(poster)
         else :
            st.write('No poster available for this movie :(')
         st.button(recommended_movies[i], key=f"row2_btn_{i}")
    st.write(":green[Recommendation completed!]")