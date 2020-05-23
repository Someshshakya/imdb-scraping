from task1 import scrap_top_list
from pprint import pprint
# pprint(task.scrap_top_list())


def group_by_year():
	movies_list=scrap_top_list()
	uniqueList
	for movie in movies_list:
		# print(c,movie["year"])
		if movie["year"] not in uniqueList:
			# return movie["year"]
			uniqueList.append(movie["year"])


	final_dict={i:[] for i in uniqueList}

	tem_list=[]
												
	for value in movies_list:
		first=value["year"]
		for unique in uniqueList:
			if str(first)==str(unique):
				final_dict[unique].append(value)
	return final_dict
	##################################################################################333\
	# we have another way too to group movies list by year
	# dict1={}
	# for i in movies_list:
	# 	if i['year'] not in dict1:
	# 		dict1[i['year']]=[]
	# 		dict1[i['year']].append(i)
	# 	else:
	# 		dict1[i['year']].append(i)


	# return dict1

# pprint(group_by_year())
#################################################################################3
# a=int(input("Enter 1st no.  "))
# b=int(input("Enter 2nd no.  "))
# c=int(input("Enter 3rd no.  "))

# if a>b:
# 	if a>c:
# 		print("this is the second max",a)
# elif b>c:
# 	print("This is the second max",b)
# else:
# 	print("This is the second max",c)