import requests
from bs4 import BeautifulSoup
import datetime
import os


def scrappedData(url, date):

    newURL = url + date.strftime('%d-%m-%Y')
    r = requests.get(newURL)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, "html.parser")
    if len(soup.find_all(class_='list-text')) == 0:
        scrappedData(url, date-datetime.timedelta(1))
    else:
        for links in soup.find_all(class_='list-text'):
            OneLiner(links.find('a').get('href'),links.find('a').get_text() ,date.strftime('%d-%m-%Y'))


def OneLiner(topic, filename ,date):
    
    r = requests.get(topic)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, "html.parser")
    tag = soup.find(class_='posted-on').find('a').get_text()
    oneline = soup.find_all('div',class_='page-content')
    for a in oneline:
        for p in a.find_all('p'):
            appendOneliner(tag, p.get_text()+'\n', filename, date)


def appendOneliner(tag, content, filename, date):
    
    if os.path.isdir('StudyIQ'):
        if os.path.isdir('StudyIQ/'+ date):
            if os.path.isdir('StudyIQ/'+ date + '/' + tag):
                ap = open('StudyIQ/' + date + '/' + tag + '/' + filename + '.txt', 'at+')
                ap.write(content)
                ap.close()
            else:
                os.mkdir('StudyIQ/'+ date + '/' + tag)
        else:
            os.mkdir('StudyIQ/' + date)
    else:
        os.mkdir('StudyIQ')
        appendOneliner(tag, content, filename, date)


if __name__ == "__main__":

    url = "https://currentaffairs.studyiq.com/daily/"
    currentDate = datetime.datetime.today().date()
    scrappedData(url,currentDate)
