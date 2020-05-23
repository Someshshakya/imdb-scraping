from task1 import scrap_top_list
from task4 import movie_details
from task5 import get_movie_list_details
from bs4 import BeautifulSoup
import requests,json,os,random,time
from pprint import pprint
def scrape_movie_cast(link_of_cast):

	link = link_of_cast[27:-31]
	file_name = ""
	file_name = str(link)+"_cast"
	## This will get you the data from the json file stored there by sending request
	if os.path.exists("/home/somesh/Desktop/cast_id/"+file_name+".json"):
		# print("data from the json file")
		with open("/home/somesh/Desktop/cast_id/"+file_name+".json") as d:
			store = d.read()
			data = json.loads(store)
			d.close()
			return data
	else:
		# print("data from the web")
		random_sleep = random.randint(1,3)
		time.sleep(random_sleep)

		page = requests.get(link_of_cast)
		soup = BeautifulSoup(page.text,"html.parser")
		table = soup.find("table",class_="cast_list")
		trs = table.find_all("td",class_="")

		cast_list = []

		for td in trs:
			dic_of_cast = {}
			dic_of_cast["imdb_id"]= td.find("a")["href"][6:-1]
			dic_of_cast["name"]= td.find("a").get_text()[:-2]
			cast_list.append(dic_of_cast)
	## This will store your data in the json file so that if you have it before you can access it by loading it 
	with open("/home/somesh/Desktop/cast_id/"+file_name+".json","w") as d:
		dum = json.dumps(cast_list)
		d.write(dum)
		d.close()
		return cast_list

# pprint(scrape_movie_cast('https://www.imdb.com/title/tt0079221/fullcredits?ref_=tt_cl_sm#cast'))

# # #################################################################################################3
   ## This loop will get you cast and id for all the 250 movies by using loop ##
#################################################################################################
# scrap_top_lis = scrap_top_list()
# see_full_url_list = []
# for movie in scrap_top_lis:
# 	url = movie["url"]+"fullcredits?ref_=tt_cl_sm#cast"
# 	see_full_url_list.append(url)
# # pprint (see_full_url_list)
# for url in see_full_url_list:
# 	cast1 = scrape_movie_cast(url)
# 	pprint(cast1)
	# print(url)
