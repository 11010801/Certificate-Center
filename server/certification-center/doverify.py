import webapp2,logging
from google.appengine.api import users
from google.appengine.ext import db
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
import Crypto.Random
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
        try:
            enctext=eval(self.request.get('text'))
            encinfo=eval(self.request.get('info'))
        except Exception,data:
            logging.error(data)
            return
            
        centerk=AdminKeys.all().get()
        privkey=RSA.importKey(centerk.privkey)
        try:
            info=privkey.decrypt(encinfo)
            gmail=info[2:int(info[0:2])+2]
            msg=info[2+int(info[0:2]):]
            user=users.User(email=gmail)
            curuser=db.GqlQuery("SELECT * FROM UserInfo WHERE User = :1",user)
            userinfo=curuser.get()
        except Exception,data:
            logging.error(data)
            return
        
        if userinfo:
            pubkey=RSA.importKey(userinfo.Pubkey)
            
            if pubkey.verify(msg,enctext):
                resmsg=pubkey.encrypt(MD5.new(msg).digest(),32)
            else:
                resmsg=MD5.new(Crypto.Random.get_random_bytes(128)).digest()
                resmsg=pubkey.encrypt(MD5.new(resmsg).digest(),32)
        else:
            resmsg=MD5.new(Crypto.Random.get_random_bytes(128)).digest()
            resmsg=RSA.importKey(centerk.pubkey).encrypt(MD5.new(resmsg).digest(),32)

        self.response.headers['Content-Type']='text/plain'
        self.response.write(resmsg)

app=webapp2.WSGIApplication([('/doverify',MainPage)],
                            debug=True)
