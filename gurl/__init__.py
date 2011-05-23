from urlparse import urlparse  
import unittest    
import re

 
IP_RE =re.compile('\d+.\d+.\d+.\d+')

DOMAIN_LIST = [
'com.cn',
'net.cn',
'edu.cn',
'org.cn',
'gov.cn',
'co.jp',
'co.uk',
'com',
'net',
'me',
'cn',
'li',
'edu',
'gov',
]
class Url(object):   
    
    def __init__(self,url=None):
        if url:
            url = unicode(url)        
            self._url = url
            self.o = urlparse(url)   
            self._empty = False            
        else:
            self._empty = True   
        
    def __str__(self):  
        return self.url
            
    def empty(self):   
        if self:
            return self._empty
        else:
            return True
             
    @property 
    def domain(self):
        
        _host = self.o.hostname 
        
        if _host is None:
            return ''

        for domain in DOMAIN_LIST:
            endpoint = '.'+domain
            if _host.endswith(endpoint):
                prefix = _host[0:_host.rfind(endpoint)]
                prefixs = prefix.split('.')
                _domain = prefixs[-1]+endpoint
                return _domain     
        
        matched = IP_RE.match(_host)
        if matched:
            return _host 
        _domain = _host

        return None
                   
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
    
    def resolve(self,endfix):
        if isinstance(endfix,unicode):
            endfix = endfix.encode('utf8')
        return '%s://%s/%s' % (self.scheme,self.o.netloc,endfix)
            
        
        pass
 
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
        
    def test_domain(self):
        url = Url('sina.com.cn')
        self.assertEqual(url.domain,'')
        
    def test_concn_domain(self):
        url = Url('com.cn')
        self.assertEqual(url.domain,'')
        url = Url('www.sina.com.cn')
     

class TestUrl(unittest.TestCase):
    def testConstructor(self):
        self.assertEquals("http://www.google.com/", str(Url("http://www.google.com")))

        self.assertEquals("http://www.google.com/", str(Url(u"http://www.google.com")))

        url = Url("http://www.google.com")

        self.assertEquals(str(url), str(Url(url)))

    def atestNonzeroAndEmpty(self):
        url = Url("http://www.google.com")

        self.assert_(url)
        self.assertFalse(url.empty())

        url = Url("invalid url")
        self.assertFalse(url)
        self.assert_(url.empty())

        url = Url()

        self.assertFalse(url)
        self.assert_(url.empty())

    def testResolve(self):
        url = Url("http://www.google.com/index.htm")

        self.assertEquals("http://www.google.com/ad.js", str(url.resolve("ad.js")))
        self.assertEquals("http://www.google.com/ad.js", str(url.resolve(u"ad.js")))

    def testProperties(self):
        url = Url("http://user:pass@www.google.com:8080/index.htm?id=1234#tag")

        self.assertEquals("http", url.scheme)
        self.assertEquals("user", url.username)
        self.assertEquals("pass", url.password)
        self.assertEquals("www.google.com", url.hostname)
        self.assertEquals(8080, url.port)
        self.assertEquals("/index.htm", url.path)
        self.assertEquals("id=1234", url.query)
        self.assertEquals("tag", url.fragment)
    
    
if __name__ == '__main__':
    unittest.main()
        

        
        
    