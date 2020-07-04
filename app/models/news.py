class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,title,description,urlToImage,publishedAt,content):
        self.name = name
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content