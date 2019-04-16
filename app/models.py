class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    '''
    class to the define the articles objects
    '''

    def __init__(self,author,title,url,urlToImage,description,publishedAt):
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt