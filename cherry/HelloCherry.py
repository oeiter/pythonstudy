'''
Created on May 31, 2014

@author: yangqig
'''
import cherrypy

class AnotherPage(object):
    @cherrypy.expose
    def index(self):
        return "another page"   
    
    
class OnePage(object):
    another = AnotherPage()
    @cherrypy.expose
    def index(self):
        return "onepage"
    
 
class HelloWorld(object):
    onepage = OnePage()
    
    def index(self):
        return "Hello World!"
    index.exposed = True
    
    @cherrypy.expose
    def test(self):
        return "test page"

cherrypy.quickstart(HelloWorld())
