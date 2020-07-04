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
        self.new_news = News('Nairametrics','Top Nigerian FinTech Apps that are leading the competition - Nairametrics','It is estimated that there are about 210-250 fintech operators/companies operating in the Nigerian space.','"https://i0.wp.com/nairametrics.com/wp-content/uploads/2018/01/FIntech.jpeg?resize=1000%2C600&ssl=1','2020-07-04T07:06:39Z','Financial technology is one of the new waves of disruptions in the financial sector, that is fuelled by the internet of things and the increasing digitalisation of the world. In the last decade, the … [+10027 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()