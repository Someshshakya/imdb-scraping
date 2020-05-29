from pprint import pprint
from task13 import movie_details
from task1 import scrap_top_list
import os,json


def analyse_actors(movie_liss):
	if os.path.exists("task15.josn"):
		with open("task15.json","r") as file_open:
			data = file_open.read()
			store = json.loads(data)
			file_open.close()
			return store
	else:
		dict_of_actor = {}
		for i in range (len(movie_liss)):
			for d in range(len(movie_liss[i]["cast"])):
				c=0
				a = movie_liss[i]["cast"][d]["name"]
				# return a
				for j in movie_liss:
					for k in j['cast']:
						if a==k["name"]:
							s = k
							c+=1
				
				dict_of_actor[s["imdb_id"]]={}
				dict_of_actor[s["imdb_id"]]["name"]=s["name"]
				dict_of_actor[s["imdb_id"]]["num_movies"]=c

		# return dict_of_actor
		with open("task15.json","w+") as file_open:
			dum = json.dumps(dict_of_actor)
			file_open.write(dum)
			file_open.close()
			return "Done!"
	




lissi = []
scrap_top = scrap_top_list()
scrap = scrap_top_list()
for ur in scrap:
	url = ur["url"]
	movie_detail = movie_details(url)
	lissi.append(movie_detail)

pprint(analyse_actors(lissi))

# scrap = scrap_top_list()[0]["url"]
# pprint(analyse_actors(movie_details(scrap)))

