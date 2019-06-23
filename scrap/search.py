
from bs4 import BeautifulSoup
import requests
import csv
from .models import Index


def doSearch(index):
    
	
	
	#index = Index.objects.all().order_by('-pub_date')[0]

	

	url=index.site_url

	url='https://www.dgtit.com/blogs/'

	index.site_url = index.site_url + '('+ url+ ')'


	search_string = index.search_text

	print(index)

	source = requests.get(url).text

	soup = BeautifulSoup(source, 'lxml')



	row_num=1
	found_row =[]


	for article in soup.find_all('article'):
		headline = article.h2.a.text

		desc = article.find('div').p.text	

		user= article.find_all('div', class_="article-metadata")[0].a.text


		str1=' {} {} {}'.format(headline, desc, user)

		i=str1.lower().find(search_string.lower())

	

		search_status='The word '+ search_string + ' is NOT found for this row'

		if (i>=0):
			found_row=found_row+[row_num]
			search_status='The word '+ search_string + ' is found for this row'

			
		index.results_set.create(sl_no=row_num, title=headline, paragraph=desc, searched_status= search_status )
		row_num +=1 


	index.save()

	if found_row ==[]:

		print('*********Sreach String not found ')
		return('Sreach String not found ')
	else:
		print('*****the string found at row '+ str(found_row))
		return('the string found for row(s) '+ str(found_row))


		

	

