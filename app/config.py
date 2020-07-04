class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-04&sortBy=publishedAt&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True