class News:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,name,url):
        self.name = name 
        self.url = url

class Articles:
    '''
    Article class to define article Objects
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt