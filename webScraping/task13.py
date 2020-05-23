from pprint import pprint
from task1 import scrap_top_list
from task12 import scrape_movie_cast
import os,json,time,random

##  This task contain Task 8,9  also

def movie_details(link):
	key = link[27:-1]
	file_name = key+".json"
	store = None
	random_sleep = random.randint(1,3)
	if os.path.exists("/home/somesh/Desktop/"+file_name):
		print("This the data from the file ")
		with open("/home/somesh/Desktop/web_data/"+file_name,"r") as d:
			data = d.read()
			store = json.loads(data)
			d.close()
			return store
	if store is None:
		time.sleep(random_sleep)
		# print("This is the data from the web ")
		from bs4 import BeautifulSoup
		import requests
		page = requests.get(link)
		data = BeautifulSoup(page.text,"html.parser")
	##This will store all the Details of the movie
		dict_of_dir = {"Directors":[],"Language":[],"Country":"","Runtime":"","Bio":"","genres":[],"poster_url":"",'name':"","cast":[]}#This will store All the details about the movie

	# #This wiill find the directors and store them in the main dictionary
		list_of_directors = data.find(class_="credit_summary_item")#.a.get_text()
		director = list_of_directors.find_all("a")
		key = list_of_directors.find("h4").get_text()
		for direc in director:
			dict_of_dir["Directors"].append(direc.get_text())
	# #It will store the country Name of the movie
		text2 = data.find(id="titleDetails")
		text3 = text2.find_all(class_="txt-block")
		for div in text3:
			if "Country:" in div.get_text():
				dict_of_dir["Country"]=div.a.get_text().strip()
	##This will find the runtime
			if "Runtime:" in div.get_text().strip():
				runTime = div.time.get_text().split()
				dict_of_dir["Runtime"]=int(runTime[0])
	##This will give you Name of languages:
			if "Language:" in div.get_text().strip():
				language = div.find_all ("a")
				for a in language:
					dict_of_dir["Language"].append(a.get_text().strip())
	##This will give The bio of the movie
		bio = data.find(class_="summary_text").get_text().strip()
		dict_of_dir["Bio"]=bio
	##This will you give you the genre of the movie
		plot= data.find('div',class_="subtext")
		attribute=plot.find_all('a')
		attribute.pop()
		dict_of_dir["genres"]=[i.get_text() for i in attribute]
	##This will give you Poster url 
		dict_of_dir["poster_url"] = "www.imdb.com"+data.find('div',class_='poster').a['href']
	##This will give name of the movie,
		dict_of_dir['name']=data.find('div',class_="title_wrapper").h1.get_text()[0:-8]


		## Adding cast to the same dict
		url5 = link+"fullcredits?ref_=tt_cl_sm#cast"
		cast = scrape_movie_cast(url5)
		dict_of_dir["cast"] = cast



	return dict_of_dir

		# open_file = open("/home/somesh/Desktop/"+file_name,'w+')
		# dum = json.dumps(dict_of_dir)
		# open_file.write(dum)
		# open_file.close()
		# return dict_of_dir

url = scrap_top_list()[0]["url"]
movie_detail = movie_details(url)
pprint(movie_detail)


