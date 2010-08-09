from urlparse import urlparse
class Url(object):   
    
    def __init__(self,url):
        if not url.startswith('http'):
            url = 'http://'+url
        self.o = urlparse(url)
         
    @property 
    def domain(self):
        return self.o.netloc 
                   
    @property    
    def scheme(self):
        return self.o.scheme
        
    @property
    def hostname(self):
        return self.o.hostname
    
    @property    
    def path(self):
        return self.o.path  
        
    @property
    def query(self):
        return self.o.query
        
        
    @property
    def hostisip(self):
        return False
        
        
    