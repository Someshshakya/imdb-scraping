from task1 import scrap_top_list
from task4 import movie_details
from pprint import pprint
from bs4 import BeautifulSoup
import requests,os,json



###########################################################################################################
													#Task 5 #
###########################################################################################################
def get_movie_list_details(movies):
	url_list = []
	ten_movie =movies
	# return ten_movie
	for url in ten_movie:
		url_list.append(url["url"])
	ten_movie_details = []
	for url1 in url_list:
		details = movie_details(url1)
		ten_movie_details.append(details)
	return ten_movie_details

# scrap_top = scrap_top_list()
# pprint(get_movie_list_details(scrap_top))


 ###########################################################################################################
													## Task 6 ##
###########################################################################################################
# def analyse_movies_language(movies):
# 	detail = movies
# 	Language_list = []
# 	for i in detail:
# 		for j in i["Language"]:
# 			Language_list.append(j)
		
# 	unique_language = {}
# 	for language in Language_list:
# 		if language in unique_language:
# 			unique_language[language]+=1
# 		else:
# 			unique_language[language]=1

# 	return unique_language

# scrap_top = scrap_top_list()
# get_movie_list = get_movie_list_details(scrap_top)
# pprint(analyse_movies_language(get_movie_list))


###########################################################################################################
													#Task 7 #
###########################################################################################################
##I have commented this code you can uncomment it when you need to run the code
# def analyse_movies_directors(movies):
# 	detail = movies
# 	directors_list = []
# 	for i in detail:
# 		for j in i["Directors"]:
# 			directors_list.append(j)
		
# 	# return Language_list
# 	final_directors_list = {}
# 	for director in directors_list:
# 		if director in final_directors_list:
# 			final_directors_list[director]+=1
# 		else:
# 			final_directors_list[director]=1
# 	return final_directors_list

# scrap_top = scrap_top_list()
# get_movie_list = get_movie_list_details(scrap_top)
# pprint(analyse_movies_directors(get_movie_list))


