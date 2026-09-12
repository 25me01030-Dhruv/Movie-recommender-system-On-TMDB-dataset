# Movie-recommender-system-On-TMDB-dataset
I have built a movie recommender system for displaying the list of movies a customer would like to watch if certain features are matching from its pjreviously watched movies.

Dataset: TMDB 5000 movie review dataset
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Goal: 
1. If user select a movie name from the options he will get 10 recommended movies which will share the common features as the selected movie.
2. For example: If my chosen movie is Iron man :
    Top 5 recommendations maybe:  1. Iron Man 2
                                  2. Avengers: Infinity wars
                                  3. Spider man
                                  4. Batman
                                  5. Superman
   
Approach:
1. After getting the movie dataset we will separate out the deciding factors that usually will be a description of the movie:
                It will include its genre, cast and crew, reviews, story, etc.

2. After getting those features we will combine them to create a semantic description of a movie.
3. We will vectorize the semantic description we will calculate the cosine similarity of a movie and will output the top 10 most cosine similar movies to the user

4. The main tech stack are :
              . Numpy
              . Pandas
              . Sklearn
              . Text vectorizers (Bag of words, Tfidf vectorizer or the Word2vec model)
              . Streamlit (for the website)
