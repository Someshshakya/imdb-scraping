import requests, os, json
from bs4 import BeautifulSoup
from pprint import pprint

#collect first page of artists'list
def scrap_top_list():
	

	if os.path.exists("task.json"):
		# print("data from json file")
		with open('task.json','r') as d:
			mo=json.load(d)
			return mo
	else:
		# print("Data from web")
			
		page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
		soup = BeautifulSoup(page.text,'html.parser')
		# print(soup)
		#pull all text from the BodyText div
		tbody= soup.find(class_="lister-list")
		
		#pull text from all instaces of <a> tag within BodyText div
		trs=tbody.find_all("tr")

		rank_list=[]
		movie_name_list=[]
		year_list=[]
		url_list=[]
		ratting_list=[]

		for tr in trs:
			position=tr.find(class_="titleColumn").get_text().strip() # by this you will get each tr separated from the all the tr tags

			empty=""# Here what it does is it is to store the no. from the rest of the data 
			for value in position:
				if "." not in value:
					empty+=value
				else:
					break
			rank_list.append(empty)  
											#  ^  to get the specific data from any tag you need to write its name and then the text format
			name=tr.find(class_="titleColumn").a.get_text() # This will fetch you out all the name of the Movie from the rest of the data
			movie_name_list.append(name) # Here with movie_name_list is the variable which will store all the data of movie one by one 

			year=tr.find(class_="titleColumn").span.get_text()
			year_list.append(year)# Here your all year will store that in which year a specifc movie was released

			url=tr.find(class_="titleColumn").a["href"]
			url_list.append("https://www.imdb.com"+url)# From here you will get all the ling of each movie and which will store in the list
			
			ratting=tr.find(class_="ratingColumn imdbRating").strong.get_text()
			ratting_list.append(float(ratting))# The ratting_list name variable stores all the ratting part from each movie
		
		final_list = []
			

		for i in range(len(rank_list)):
			tem_dict = {"position":"","name":"","year":"","ratting":"","url":""}
			tem_dict["position"]=int(rank_list[i])
			tem_dict["name"]=str(movie_name_list[i])
			year_list[i]=year_list[i][1:5]
			tem_dict["year"]=int(year_list[i])
			tem_dict["ratting"]=float(ratting_list[i])
			tem_dict["url"]=url_list[i]
			final_list.append(tem_dict)

		# return final_list

		mo=json.dumps(final_list, indent=4)
		
		with open('task.json','w') as d:
			d.write(mo)
			return final_list


# pprint(scrap_top_list())


	
  