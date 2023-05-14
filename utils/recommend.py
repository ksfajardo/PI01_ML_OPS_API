from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

sample_md=pd.read_csv('data/ML_Data.csv')
cv1 = CountVectorizer(stop_words='english')
cv_matrix1 = cv1.fit_transform(sample_md['text'])
cosine_sim1 = cosine_similarity(cv_matrix1,cv_matrix1)

def recomendaciones(titulo):
    try:
        # Getting the index of the movie that matches the title
        idx = sample_md[sample_md['title'] == str(titulo).lower()].index[0]
        # Getting the similarity scores
        sim_scores = list(enumerate(cosine_sim1[idx]))
        #Sorting the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Getting the top 5 recommendations
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        recommendations=list(sample_md['title'].iloc[movie_indices].str.title())
        return {'lista recomendada': recommendations} 
    except:
        return {'lista recomendada': ['Minions', 'Wonder Woman', 'Beauty and the Beast', 'Baby Driver', 'Big Hero 6']}