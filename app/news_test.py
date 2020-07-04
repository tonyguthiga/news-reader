import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to  test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News()