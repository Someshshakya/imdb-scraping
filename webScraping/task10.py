from task5 import get_movie_list_details
from  task1 import scrap_top_list
from pprint import pprint
def analyse_language_and_directors(list_movies_details):
	movie_details = list_movies_details
	dict_Of_Directors = {}
	for movie in movie_details:
		for director in movie["Directors"]:
			dict_Of_Directors[director]={}
	for i in range (len(movie_details)):
		for director in dict_Of_Directors:
			if director in movie_details[i]["Directors"]:
				for language in movie_details[i]['Language']:
					dict_Of_Directors[director][language]=0
	for i in range (len(movie_details)):
		for director in dict_Of_Directors:
			if director in movie_details[i]["Directors"]:
				for language in movie_details[i]['Language']:
					dict_Of_Directors[director][language]+=1
	return dict_Of_Directors
scrap_top = scrap_top_list()
movie_details = get_movie_list_details(scrap_top)
pprint(analyse_language_and_directors(movie_details))

