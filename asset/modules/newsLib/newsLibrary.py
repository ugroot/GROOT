#newsapi.org Great Api
#https://newsapi.org/docs/endpoints/everything
import random
from newsapi.newsapi_client import NewsApiClient
from datetime import datetime,timedelta
import random
# Init
newsapi = NewsApiClient(api_key='2b613eac07a2422996b431ce5b9c68fa')

#q is keyword
#format of date is yyyy-mm-dd
#one more good argument is sort_by "relevancy"


#Cant request more than one month old articles
def news_func():
    keyWords = ['India','Delhi','March','Work','Life','World','USA','Elections','Cricket','Sports','Finance','Economy']
    case = keyWords[random.randint(0,len(keyWords))-1]
    today = str(datetime.now().date())
    period = datetime.now() - timedelta(15)
    lastday = str(period.date())

    all_headlines = newsapi.get_everything(q=case,from_param=today,to=lastday,language='en')   
    #From Here Data with following things we need as key:
    #Title(Heading for us)
    #Description(Subheading for us)
    #url(More for us)
    #urlToImage(imageUrl for us)
    return all_headlines['articles']

# def headLines():
#     keyWords = ['India','Delhi','March','Work','Life','World','USA','Elections','Cricket','Sports','Finance','Economy']
#     allHeadlines = []
#     for words in keyWords:
#         top_headlines = newsapi.get_top_headlines(q=words,language='en', country='in')
#         allHeadlines.append(top_headlines['articles'])
    
#     for headLines in allHeadlines[0]:
#         print(headLines)

# headLines()

