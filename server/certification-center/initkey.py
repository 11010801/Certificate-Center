import webapp2
from google.appengine.api import users
class MainPage(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        if(not users.is_current_user_admin()):
            users.create_logout_url("/")
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>init keys</title>
            </head>
            <body>
                <h1 align="center">Certification Center</h1>
                <form action="initkey" method="post">
                    <input type="submit" value="generate keys"/>
                </form>
            </body>
        </html>
        """)
    def post(self):
        if(not users.is_current_user_admin()):
            users.create_logout_url("/")
        self.response.headers['Content-Type']='text/plain'
        self.response.write('post method')
app=webapp2.WSGIApplication([('/initkey',MainPage)],
                            debug=True)
