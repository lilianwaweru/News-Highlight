import unittest
from app.models  import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to the the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("bbc-sport","BBC Sport","The home of BBC Sport online. Includes live sports coverage, breaking news, results, video, audio and analysis on Football, F1, Cricket, Rugby Union, Rugby League, Golf, Tennis and all the main world sports, plus major events such as the Olympic Games","http://www.bbc.co.uk/sport","sports","gb")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()

