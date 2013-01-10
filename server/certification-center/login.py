import webapp2

from google.appengine.api import users
from google.appengine.ext import db

class UserInfo(db.Model):
    User=db.UserProperty()
    CreateTime=db.DateTimeProperty(auto_now_add=True)
    LastModified=db.DateTimeProperty(auto_now=True)
    VerifyNum=db.IntegerProperty(default=0)
    Pubkey=db.TextProperty(default="pubkey")
class MainPage(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        curuser=db.GqlQuery("SELECT * FROM UserInfo WHERE User = :1",user)
        userinfo=curuser.get()
        if userinfo:
            self.response.headers['Content-Type']='text/plain'
	    self.response.write(userinfo.Pubkey)
       	else:
       	    self.redirect('/register')

app=webapp2.WSGIApplication([('/login',MainPage)],
                            debug=True)
