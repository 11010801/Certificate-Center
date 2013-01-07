import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>register</title>
            </head>
            <body>
                register page
            </body>
        </html>
        """)

app=webapp2.WSGIApplication([('/register',MainPage)],
                            debug=True)
