class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=c1647e6198d248cbb88f2ef5b0d0b3ab'
    

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
     Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
