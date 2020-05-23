from pprint import pprint
from task1 import scrap_top_list
from task5 import get_movie_list_details
def analyse_movies_genre(movie_details):
	genre_dict = {}
	for movie in movie_details:
		for genre in movie['genres']:
			if genre in genre_dict:
				genre_dict[genre]+=1
			else:
				genre_dict[genre]=1
	return genre_dict


scrap_top = scrap_top_list()
movie_details = get_movie_list_details(scrap_top)
pprint(analyse_movies_genre(movie_details))
