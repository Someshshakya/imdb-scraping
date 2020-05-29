from pprint import pprint
from task13 import movie_details
from task1 import scrap_top_list
from task12 import scrape_movie_cast
# {
#   "nm0004435": {
#     "name": "Rajesh Khanna",
#     "frequent_co_actors": [
#       {
#         "imdb_id": "nm0000821",
#         "name": "Amitabh Bachan"
#         "num_movies": 2
#       }
#     ]
#   },
#   "nm0000821": {
#     "name": "Amitabh Bachan",
#     "frequent_co_actors": [
#       {}, {}, {}
#     ]
#   }
# }
def analyse_co_actors(list_of_movies):

	final = []
	for movie in list_of_movies:
		# return movie["cast"]
		c=0
		
		
		for i in range(len(movie["cast"])):
			tem = {}
			dic_of_co = {}
			# return movie["cast"][i]["imdb_id"]
			# return movie["cast"][i+1]
			dic_of_co[movie["cast"][i]["imdb_id"]]={}
			dic_of_co[movie["cast"][i]["imdb_id"]]["name"] = movie["cast"][i]["name"]
			dic_of_co[movie["cast"][i]["imdb_id"]]["frequent_co_actors"]=[]

			## This will store the frequent co actors in tem dictionay
			tem["imdb_id"]=movie["cast"][i+1]["imdb_id"]

			tem["name"]=movie["cast"][i+1]["name"]
			# return tem
			#This will store number of movies 
			tem["num_movies"]=0
			dic_of_co[movie["cast"][i]["imdb_id"]]["frequent_co_actors"].append(tem)
			c+=1

			final.append(dic_of_co)
			# print("c",c)
			if c==5:
				return final
				break
	# return dic_of_coc





			# return tem


			# dic_of_co[cast["imdb_id"]]["frequent_co_actors"].apend(tem)



			# return dic_of_co
	# return list_of_movies






list_of = []
scrap = scrap_top_list()
for ur in scrap:
	url = ur["url"]
	movie_detail = movie_details(url)
	list_of.append(movie_detail)
print(analyse_co_actors(list_of))