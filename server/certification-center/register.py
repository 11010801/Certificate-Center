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
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>register</title>
            </head>
            <body>
                <h1 align="center">Certification Center</h1>
                <form action=/register method=POST>
                    <h3>public key</h3>
                    <textarea name=pubkey  rows=30 cols=60></textarea>
                    <p>
                    <input type=submit>
                </form>
            </body>
        </html>
        """)
    def post(self):
    	user=users.get_current_user()
        curuser=db.GqlQuery("SELECT * FROM UserInfo WHERE User = :1",user)
        userinfo=curuser.get()
        if userinfo:
            userinfo.Pubkey=self.request.get('pubkey')
            userinfo.put()
       	else:
            newuser=UserInfo(User=user,Pubkey=self.request.get('pubkey'))
            newuser.put()
       	self.redirect('/login')

app=webapp2.WSGIApplication([('/register',MainPage)],
                            debug=True)
