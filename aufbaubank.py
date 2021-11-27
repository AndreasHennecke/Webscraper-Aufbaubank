import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

#Value to see the whole entry
pd.set_option('display.max_colwidth', None)

def getMainSite(url):
    ### Create DataSet
       
    dfJobList = pd.DataFrame(columns=['title','url'])
    
    ### Start webscraping

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")
    i = 0
    for articel in soup.find_all(class_="mobi-link", href=True):
        dfJobList = dfJobList.append({'title':articel['title'], 'url':articel['href']}, ignore_index=True)
        
        
      
    return (dfJobList)


if __name__=='__main__':
    dfJobList = getMainSite("https://www.aufbaubank.de/Karriere")
    print('----------------------------------------------------------------\n')
    print('Found the new Joblist \n')
    print(dfJobList)
      
    df1 = pd.read_excel(r'c:\temp\lastSearch.xlsx')
    print('----------------------------------------------------------------\n')
    print('Compare to the older one \n')
    print('----------------------------------------------------------------\n')
    difference= pd.concat([dfJobList,df1]).drop_duplicates(keep=False)
    if difference.empty == True:
        print('nothing new')
        print('----------------------------------------------------------------\n')
    else:
        print(difference)
        print('----------------------------------------------------------------\n')
    
    print('Save the new List \n')
    dfJobList.to_excel(r'c:\temp\lastSearch.xlsx', index=False, header=True)
    print('----------------------------------------------------------------\n')
    print('Done')
    print('----------------------------------------------------------------\n')
    
    
    


