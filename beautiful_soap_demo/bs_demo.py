import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
import logging
import numpy as np


def LOG(msg):
    logging.basicConfig(filename='html_file.txt',filemode='w+',level=logging.INFO,format='%(asctime)s %(message)s')
    logging.info(msg)



url='https://www.naukri.com/data-scientist-python-jobs-in-bengaluru?k=data%20scientist%20python&l=bengaluru'


page=requests.get(url)
#print(page.text)


driver=webdriver.Chrome(r'D:\ML\Project_1\chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html5lib')
#LOG(soup.prettify())

driver.close()


df=pd.DataFrame(columns=['Title','Company','Ratings','Reviews'])

results = soup.find(class_='list')

#LOG(results)

job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
#LOG(job_elems)

#skill_elems=results.find_all('ul',class_='tags has-description')

#LOG(skill_elems)

job_title=[]
company=[]
requirements=[]
reviews=[]

for job_elem in job_elems:
    job_title.append(job_elem.find('a',class_='title fw500 ellipsis').get('title'))
    company.append(job_elem.find('a', class_='subTitle ellipsis fleft').get('title'))
    requirement=job_elem.find(class_='job-description fs12 grey-text')
    requirements.append(requirement.text)
    review=job_elem.find(class_='starRating fleft dot')
    if review is None:
        reviews.append('NA')
    else:
        reviews.append(review.text)
    #df.append({})







#LOG(job_title)
#LOG(company)
#LOG(requirements)
#LOG(reviews)

data=dict()

data={'Title':job_title,'Company':company,'Ratings':reviews}

df=pd.DataFrame(data=data)

df.drop


LOG(df.head())

df.to_csv('data.csv')






