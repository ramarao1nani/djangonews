from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def globalnews():
    inshorts_r = requests.get("https://www.inshorts.com/en/read/world")
    inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')
    inshorts_headings = inshorts_soup.find_all('span',itemprop="headline")
    body = inshorts_soup.find_all('div',itemprop="articleBody")
    inshorts_body=[]
    inshorts_news=[]
    for th in inshorts_headings:
        inshorts_news.append(th.text)
    for tb in body:
        inshorts_body.append(tb.text)
    newss={"inshorts_body":inshorts_body,"inshorts_news":inshorts_news}
    return newss

def tech():
    inshorts_r = requests.get("https://www.inshorts.com/en/read/technology")
    inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')
    inshorts_headings = inshorts_soup.find_all('span',itemprop="headline")
    body = inshorts_soup.find_all('div',itemprop="articleBody")
    inshorts_body=[]
    inshorts_news=[]
    for th in inshorts_headings:
        inshorts_news.append(th.text)
    for tb in body:
        inshorts_body.append(tb.text)
    newss={"inshorts_body":inshorts_body,"inshorts_news":inshorts_news}
    return newss

def businessnew():
    inshorts_r = requests.get("https://www.inshorts.com/en/read/business")
    inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')
    inshorts_headings = inshorts_soup.find_all('span',itemprop="headline")
    body = inshorts_soup.find_all('div',itemprop="articleBody")
    inshorts_body=[]
    inshorts_news=[]
    for th in inshorts_headings:
        inshorts_news.append(th.text)
    for tb in body:
        inshorts_body.append(tb.text)
    newss={"inshorts_body":inshorts_body,"inshorts_news":inshorts_news}
    return newss

def national():
    inshorts_r = requests.get("https://www.inshorts.com/en/read/national")
    inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')
    inshorts_headings = inshorts_soup.find_all('span',itemprop="headline")
    body = inshorts_soup.find_all('div',itemprop="articleBody")
    inshorts_body=[]
    inshorts_news=[]
    for th in inshorts_headings:
        inshorts_news.append(th.text)
    for tb in body:
        inshorts_body.append(tb.text)
    newss={"inshorts_body":inshorts_body,"inshorts_news":inshorts_news}
    return newss

def coronavirusdetails():
    my_dict={"cases":"","deaths":"","recovered":""}
    covidurl = requests.get("https://www.worldometers.info/coronavirus/#countries")
    covidsoup = BeautifulSoup(covidurl.content, 'html.parser')
    result = covidsoup.find_all('div',{"class":"maincounter-number"})
    my_dict["cases"]=result[0].find('span').text
    my_dict["deaths"]=result[1].find('span').text
    my_dict["recovered"]=result[2].find('span').text
    return my_dict

def headlines():
    r = requests.get("https://timesofindia.indiatimes.com/briefs")
    soup = BeautifulSoup(r.content, 'html.parser')
    headings = soup.find_all('h2')
    briefs=soup.find_all('p')
    briefs=briefs[8:-2]
    headings = headings[2:-12] # removing footer links
    story=[]
    news=[]
    for i in briefs:
        story.append(i.text)
    for i in headings:
        news.append(i.text)
    newss={"news":news,"body":story}
    return newss

def home(request):
    covid=coronavirusdetails()
    topnews=headlines()
    headings=topnews["news"]
    summary=topnews["body"]
    news=zip(headings,summary)
    return render(request, 'briefs/home.html',{'news':news,'cases':covid["cases"],'deaths':covid["deaths"],'recovered':covid["recovered"]})

def india(request):
    indiannews=national()
    headings=indiannews["inshorts_news"]
    summary=indiannews["inshorts_body"]
    news=zip(headings,summary)
    return render(request, 'briefs/india.html',{'news':news})

def technology(request):
    technews=tech()
    headings=technews["inshorts_news"]
    summary=technews["inshorts_body"]
    news=zip(headings,summary)
    return render(request, 'briefs/technology.html',{'news':news})
def business(request):
    businessnews=businessnew()
    headings=businessnews["inshorts_news"]
    summary=businessnews["inshorts_body"]
    news=zip(headings,summary)
    return render(request, 'briefs/business.html',{'news':news})
def world(request):
    worldnews=globalnews()
    headings=worldnews["inshorts_news"]
    summary=worldnews["inshorts_body"]
    news=zip(headings,summary)
    return render(request, 'briefs/world.html',{'news':news})

