import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        self.response.write("""
        <html>
            <head>
                <title>not found</title>
            </head>
            <body>
                not found
            </body>
        </html>
        """)

app=webapp2.WSGIApplication([('/*',MainPage)],
                            debug=True)
