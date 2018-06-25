import webbrowser

#this will open url asked to opned by user 
def openweb(url):
        urls='http://'+url
        webbrowser.open(urls, new=2)
