import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to  test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('bbc-news','https://www.nationalgeographic.com/animals/2020/07/covid-vaccine-needs-horseshoe-crab-blood.html')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
