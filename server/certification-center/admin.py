import webapp2

from google.appengine.ext import db

class AdminKeys(db.Model):
    pubkey = db.TextProperty(default="pubkey")
    privkey= db.TextProperty(default="privkey")
class MainPage(webapp2.RequestHandler):
    def get(self):
        keys=AdminKeys.all()
        k=keys.get()
        privkey="none"
        if k:
            privkey=k.privkey
        self.response.headers['Content-Type']='text/html'
        htmltext="""
        <html>
            <head>
                <title>certification center</title>
            </head>
            <body>
                <h1 align="center">Certification Center</h1>
                <h3>private key</h3>"""
        htmltext=htmltext+privkey
        htmltext=htmltext+"""
                <form action=/admin method=POST>
                    <h3>private key</h3>
                    <textarea name=privkey rows=20 cols=40></textarea>
                    <h3>public key</h3>
                    <textarea name=pubkey  rows=20 cols=40></textarea>
                    <P>
                    <input type=submit>
                </form>
            </body>
        </html>"""
        self.response.write(htmltext)
    def post(self):
        keys=AdminKeys.all()
        k=keys.get()
        if not k:
            new_keys=AdminKeys(pubkey=self.request.get("pubkey"),privkey=self.request.get("privkey"))
            new_keys.put()
        else:
            k.privkey = self.request.get("privkey")
            k.pubkey  = self.request.get("pubkey")
            k.put()
        self.redirect(self.request.uri)
app=webapp2.WSGIApplication([('/admin',MainPage)],
                            debug=True)
