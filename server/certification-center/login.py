import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>login</title>
            </head>
            <body>
                login page
            </body>
        </html>
        """)

app=webapp2.WSGIApplication([('/login',MainPage)],
                            debug=True)
