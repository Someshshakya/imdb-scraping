from task1 import scrap_top_list
from task4 import movie_details
from task5 import get_movie_list_details
from bs4 import BeautifulSoup
import requests,json,os
from pprint import pprint
def scrape_movie_cast(link_of_cast):
	scrap_top_lis = scrap_top_list()
	for movie in scrap_top_lis:
		url = movie["url"]
		pagee = requests.get(url)
		soup = BeautifulSoup(pagee.text,"html.parser")
		main = soup.find("div",id="titleCast")
		data = main.find("div",class_="see-more")
		a = data.find("a")['href']
		# for i in data:
		# 	pprint(i.find("a").get_text().strip())

		return a

	# link = link_of_cast[27:-31]
	# file_name = ""
	# file_name = str(link)+"_cast"
	# if os.path.exists("/home/somesh/Desktop/cast_id/"+file_name+".json"):
	# 	with open("/home/somesh/Desktop/cast_id/"+file_name+".json") as d:
	# 		store = d.read()
	# 		data = json.loads(store)
	# 		d.close()
	# 		return data
	# else:
	# 	page = requests.get(link_of_cast)
	# 	soup = BeautifulSoup(page.text,"html.parser")
	# 	table = soup.find("table",class_="cast_list")
	# 	trs = table.find_all("td",class_="")

	# 	cast_list = []
	# 	for td in trs:
	# 		dic_of_cast = {}
	# 		dic_of_cast["imdb_id"]= td.find("a")["href"][6:-1]
	# 		dic_of_cast["name"]= td.find("a").get_text()[:-2]
	# 		cast_list.append(dic_of_cast)
	

	# with open("/home/somesh/Desktop/cast_id/"+file_name+".json","w") as d:
	# 	dum = json.dumps(cast_list)
	# 	d.write(dum)
	# 	d.close()
	# 	return "hello !"


	
	


# movie_detail = scrap_top_list()
# get_movie_list_detail = get_movie_list_details(movie_detail)
# for movie in get_movie_list_detail:
# 	pprint(movie)

pprint(scrape_movie_cast('https://www.imdb.com/title/tt0079221/fullcredits?ref_=tt_cl_sm#cast'))