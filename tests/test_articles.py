import unittest
from app.models  import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to the the behaviour of the Articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.articles_articles = Articles("Rachel England","Square will offer","https://www.engadget.com","https://www.engadget.com","Payments startup Square is turning its attention to cryptocurrency.","2019-03-21T12:21:00Z")
    def test_instance(self):
        self.assertTrue(isinstance(self.articles_articles,Articles))


if __name__ == '__main__':
    unittest.main()
