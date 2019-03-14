#newsapi.org Great Api
#https://newsapi.org/docs/endpoints/everything
from newsapi import NewsApiClient
# Init
newsapi = NewsApiClient(api_key='2b613eac07a2422996b431ce5b9c68fa')

#q is keyword
#format of date is yyyy-mm-dd
#one more good argument is sort_by "relevancy"
case = "india"
#Cant request more than one month old articles
def news_func():
    all_headlines = newsapi.get_everything(q=case,from_param='2019-03-11',to='2019-02-22',language='en')   
    #From Here Data with following things we need as key:
    #Title(Heading for us)
    #Description(Subheading for us)
    #url(More for us)
    #urlToImage(imageUrl for us)
    return all_headlines['articles']





