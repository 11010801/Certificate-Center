import webapp2
from google.appengine.api import users
from google.appengine.ext import db
from Crypto.PublicKey import RSA
class AdminKeys(db.Model):
    pubkey=db.TextProperty(default="pubkey")
    privkey=db.TextProperty(default="privkey")
class UserInfo(db.Model):
    User=db.UserProperty()
    CreateTime=db.DateTimeProperty(auto_now_add=True)
    LastModified=db.DateTimeProperty(auto_now=True)
    VerifyNum=db.IntegerProperty(default=0)
    Pubkey=db.TextProperty(default="pubkey")
class MainPage(webapp2.RequestHandler):
    def post(self):
        enctext=self.request.get('text')
        encinfo=self.request.get('info')
        centerk=AdminKeys.all().get()
        privkey=RSA.importKey(centerk.privkey)
        info=privkey.decrypt(encinfo)
        gmail=info[2:int(info[0:2])]
        msg=info[2+int(info[0:2]):]
        user=users.User(email=gmail)
        curuser=db.GqlQuery("SELECT * FROM UserInfo WHERE User = :1",user)
        userinfo=curuser.get()
        self.response.headers['Content-Type']='text/plain'
        resmsg="error"
        if userinfo:
            pubkey=RSA.importKey(userinfo.Pubkey)
            if pubkey.verify(msg,enctext):
               resmsg=msg
        self.response.write(resmsg)

app=webapp2.WSGIApplication([('/doverify',MainPage)],
                            debug=True)
