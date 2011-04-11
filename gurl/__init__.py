from urlparse import urlparse  
import unittest
class Url(object):   
    
    def __init__(self,url):          
        if not url.startswith('http'):
            url = 'http://'+url  
        self.url = url
        self.o = urlparse(url)
    
    def __str__(self):
        return self.url
         
    @property 
    def domain(self): 
        _netloc = self.o.netloc
        array = _netloc.split('.') 
        _netloc = '.'.join(array[1:])
        return _netloc
                   
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
    def port(self):
        return self.o.port
        
    @property
    def fragment(self):
        return self.o.fragment 
    
    @property
    def username(self):
        return self.o.username
        
    @property
    def password(self):
        return self.o.password
        
        
    @property
    def hostisip(self):
        return False     
 
class gurlTestCase(unittest.TestCase):
    
    def testgurl(self):
        url = Url('http://www.hr125.com/') 
        self.assertTrue('http://www.hr125.com/',str(url))
        
    def testdomain(self):
        url = Url('http://www.sina.com.cn/test.html')  
        self.assertEqual(url.domain,'sina.com.cn')
    
if __name__ == '__main__':
    unittest.main()
        

        
        
    