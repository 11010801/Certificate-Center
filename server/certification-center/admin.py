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
        if not k:
            new_keys=AdminKeys(pubkey="public key",privkey="privkey")
            new_keys.put()
        elif k.privkey=="privkey":
            k.privkey="private key"
            k.pubkey ="public key"
            k.put()
        k=keys.get()
        self.response.write(k.privkey)
app=webapp2.WSGIApplication([('/admin',MainPage)],
                            debug=True)
