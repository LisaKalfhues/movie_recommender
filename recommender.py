'''Implements functions for making predictions'''
import random
from utils import MOVIES

# MOVIES = [
#     'Avatar',
#     'The Great Beauty',
#     'Star Wars',
#     'Interstelar',
#]

def random_recommender():
    random.shuffle(MOVIES)
    top_two = MOVIES[0:2]
    return top_two

def cos_sim():
    pass

def NMF():
    pass
