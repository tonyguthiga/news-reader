import unittest
from app.models import News, Articles


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

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to  test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('Robert Frank','The billionaires and country clubs that received small business loans from the government - CNBC','Billionaires, country clubs, private jet companies and Kanye West all received millions in government funding under the Paycheck Protection Program, according to filings.','https://www.cnbc.com/2020/07/07/the-billionaires-and-country-clubs-that-received-ppp-loans.html','https://image.cnbcfm.com/api/v1/image/106605723-1594130645953preview.jpg?v=1594130678','2020-07-07T14:18:15Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))
