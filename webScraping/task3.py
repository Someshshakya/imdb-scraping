# Task 3
# Task 2 mein humne movies ko year ke hisaab se group karne ka code toh likh liya. Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. Jaise:

# 1960 se 1969 tak ke beech ke saare saal 1960s ke decade mein aate hain.
# 1970 se 1979 tak ke beech ke saare saal 1970s ke decade mein aate hain.
# 1980 se 1989 tak ke beech ke saare saal 1980s ke decade mein aate hain.
# 2000 se 2009 tak ke beech ke saare saal 2000s ke decade mein aate hain.

# from task import scrap_top_list
from pprint import pprint

# by_year=group_by_year()
# pprint(by_year)

def group_by_decades():
	from task2 import group_by_year
	group_by_year = group_by_year() 

	decade_list = []
	for d in group_by_year:
		mod=d%10      # It will return you the last value  Example if the value comes 1956 so it will return you 6 
		year = d-mod # Here it will subtract that value from the real one Ex.  1956 so your result will be 1950 

		if year not in decade_list: # It will check weather the incoming year is there or not and if not it will store the year in the List
			decade_list.append(year)
	decade_list.sort()
	
	dic = {} # This the main dictionary where year will arrange by decades

	for decade in decade_list:
		dic[decade]=[] # It will create list in of each key as value

	for key in decade_list: #[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
		add = key+9
		for year in group_by_year:
			
			if year>=key and year<=add:
				dic[key].append(group_by_year[year][0]) # Here one by one my all the list will store in the dic 
	return dic	


pprint(group_by_decades())