import webapp2

from google.appengine.ext import db

class AdminKeys(db.Model):
    pubkey = db.TextProperty(default="pubkey")
    privkey= db.TextProperty(default="privkey")

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/plain'
        keys=AdminKeys.all()
        k=keys.get()
        if k:
            self.response.write(k.pubkey)

app=webapp2.WSGIApplication([('/publickey',MainPage)],
                            debug=True)
