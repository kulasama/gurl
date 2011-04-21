from urlparse import urlparse  
import unittest    
import re

 
IP_RE =re.compile('\d+.\d+.\d+.\d+')
class Url(object):   
    
    def __init__(self,url):          
        if not url.startswith('http'):
            url = 'http://'+url  
        self._url = url
        self.o = urlparse(url)
    
    def __str__(self):
        return self.url
         
    @property 
    def domain(self):
        _netloc = self.o.netloc 
        matched = IP_RE.match(_netloc)
        if matched:
            return _netloc           
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
    @property
    def url(self):                
        if self.o.path.find('.') == -1:
            if self._url[-1] != '/':
                self._url = '%s/' % self._url
        return self._url
 
class gurlTestCase(unittest.TestCase):
    
    def testgurl(self):
        url = Url('http://www.hr125.com/') 
        self.assertTrue('http://www.hr125.com/',str(url))
     
        
    def testdomain(self):
        url = Url('http://www.sina.com.cn/test.html')  
        self.assertEqual(url.domain,'sina.com.cn')  
        
    def testdomain1(self):
        url = Url('http://10.1.1.21/test.html')
        self.assertEqual(url.domain,'10.1.1.21')  
    
    def testurl1(self):
        url = Url('http://www.sina.com.cn/cn')
        self.assertEqual(url.url,'http://www.sina.com.cn/cn/')
    
    def testurl2(self):
        url = Url('http://www.sina.com.cn/cn/index.php')
        self.assertEqual(url.url,'http://www.sina.com.cn/cn/index.php')
    
if __name__ == '__main__':
    unittest.main()
        

        
        
    