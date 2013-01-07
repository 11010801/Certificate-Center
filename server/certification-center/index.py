import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>certification center</title>
            </head>
            <body>
                <h1 align="center">Certification Center</h1>
                <a href="login">login</a>
                <a href="register">register</a>
            </body>
        </html>
        """)

app=webapp2.WSGIApplication([('/',MainPage)],
                            debug=True)
