# %% codecell
import numpy as np
import pandas as pd
import pandas_datareader as dr
from urllib.request import urlopen
from bs4 import BeautifulSoup
import seaborn as sb

import requests
import urllib.request as urllib
from datetime import datetime
import csv
# %% codecell
fecha = '20220129' ###

##########################  Expansion  #######################################
# %% codecell
url = "https://www.expansion.com/mercados.html?intcmp=MENUHOM24101&s_kw=mercados"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="mod-title normal")
#coverpage_news_lista=[e for e in coverpage_news]
#coverpage_news_norep = [e for e in coverpage_news if e not in (coverpage_news_dia)]
#len(coverpage_news_lista)
#coverpage_news[0].get_text()

article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]
len(article_href)
#article_href_norep = [e for e in article_href if e not in (list_links)]
#len(article_href_norep)

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # only news articles (there are also albums and other things)
    #if "inenglish" not in coverpage_news[n].find('a')['href']:
    #    continue
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    #body = soup_article.find_all('div', class_='')
    body = soup_article.find_all('p', class_="")
    #x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df1 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df1['Seccion'] ="Mercados"
df1['Fecha'] = datetime.now().date()
# %% codecell

######################### Expansion AHORRO  ################################
# %% codecell
url = "https://www.expansion.com/ahorro.html?intcmp=MENUHOM24101&s_kw=ahorro"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # only news articles (there are also albums and other things)
    #if "inenglish" not in coverpage_news[n].find('a')['href']:
    #    continue
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    #body = soup_article.find_all('div', class_='')
    #body = soup_article.find_all('p', class_="ue-c-article_standfirst")
    body = soup_article.find_all('p', class_="")
    #x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df2 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df2['Seccion'] ="Ahorro"
df2['Fecha'] = datetime.now().date()
# %% codecell

#################### Expansion EMPRESA  ###########################
# %% codecell
url = "https://www.expansion.com/empresas.html?intcmp=MENUHOM24101&s_kw=empresas"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # only news articles (there are also albums and other things)
    #if "inenglish" not in coverpage_news[n].find('a')['href']:
    #    continue
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    #body = soup_article.find_all('div', class_='')
    #body = soup_article.find_all('p', class_="ue-c-article_standfirst")
    body = soup_article.find_all('p', class_="")
    #x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df3 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df3['Seccion'] ="Empresa"
df3['Fecha'] = datetime.now().date()
# %% codecell



#################### Expansion ECONOMIA  ###########################
# %% codecell
url = "https://www.expansion.com/economia.html?intcmp=MENUHOM24101&s_kw=economia"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # only news articles (there are also albums and other things)
    #if "inenglish" not in coverpage_news[n].find('a')['href']:
    #    continue
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    #body = soup_article.find_all('div', class_='')
    #body = soup_article.find_all('p', class_="ue-c-article_standfirst")
    body = soup_article.find_all('p', class_="")
    #x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df4 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df4['Seccion'] ="Economia"
df4['Fecha'] = datetime.now().date()
# %% codecell
len(article_href)

#################### Expansion EMPLEO  ###########################
# %% codecell
url = "https://www.expansion.com/expansion-empleo.html?intcmp=MENUHOM24101&s_kw=exp-empleo"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('h2', class_="ue-c-cover-content__headline")
article_href = [ tag.find('a').get('href','') if tag.find('a') else '' for tag in coverpage_news]

# Scraping the first 5 articles
number_of_articles = len(article_href)
# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []
list_links_dia=list_links

for n in np.arange(0, number_of_articles):
    # only news articles (there are also albums and other things)
    #if "inenglish" not in coverpage_news[n].find('a')['href']:
    #    continue
    # Getting the link of the article
    #link = coverpage_news[n].find('a')['href']
    link = article_href[n]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    #body = soup_article.find_all('div', class_='')
    #body = soup_article.find_all('p', class_="ue-c-article_standfirst")
    body = soup_article.find_all('p', class_="")
    #x = body[0].find_all('p')

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        #paragraph = x[p].get_text()
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    news_contents.append(final_article)

df_links = pd.DataFrame(list_links , columns=['link'])
df = pd.DataFrame(news_contents, columns=['contenido'])
df_titles = pd.DataFrame(list_titles, columns=['titulo'])
df = pd.merge(df_titles, df ,right_index=True, left_index=True, how='left')
df5 = pd.merge(df, df_links ,right_index=True, left_index=True, how='left')
df5['Seccion'] ="Empleo"
df5['Fecha'] = datetime.now().date()
# %% codecell
len(article_href)

df_total = df1
df_total = df_total.append(df2)
df_total = df_total.append(df3)
df_total = df_total.append(df4)
df_total = df_total.append(df5)
len(df_total)

# contenido relacionado con Seguros
df_filter = df_total[df_total['contenido'].str.contains('pyme|autonomo|insurtech|singularcover', case=False)]
df_filter['link']
df_filter_list = df_filter['link'].tolist()

#df_total.to_csv('expansion_'+fecha+'_total.csv')
df_total.to_excel('expansion_'+fecha+'_total.xlsx')
