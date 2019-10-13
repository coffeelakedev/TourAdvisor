import tornado.ioloop
import tornado.web

import backend
import pprint

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("signin.html")

class PlanHandler(tornado.web.RequestHandler):
    def get(self):
        print(self)
        account = backend.add_plan(self.get_argument('plan'))
        pprint.pprint(account)
        feedHtml = open('feed.html', 'w')
        feedHtml.write('')
        feedHtml.close()
        feedHtml = open('feed.html', 'a')
        feedHtml.write("""
        <!DOCTYPE html>
        <html>
            <head>
            <!--Import Google Icon Font-->
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <!--Import materialize.css-->
            <!-- Compiled and minified CSS -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
            <!--Let browser know website is optimized for mobile-->
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            </head>
            <body>
            <!-- Compiled and minified JavaScript -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
""")
        for i in account:
            CARD = """
<div class="row">
    <div class="col s12 m7">
        <div class="card">
            <div class="card-image">
                <img src="images/sample-1.jpg">
                <span class="card-title">Card Title</span>
            </div>
            <div class="card-content">
                <p>""" + i[0] + """</p>
            </div>
            <div class="card-action">
                <a href="#">Book</a>
            </div>
        </div>
    </div>
</div>
"""
            feedHtml.write(CARD)
        feedHtml.write('</body></html>')
        feedHtml.close()
        self.render('dashboard.html')
        #self.redirect('dashboard.html')

class SignInHandler(tornado.web.RequestHandler):
    def get(self):
        print(self)
        email = self.get_argument('email')
        pwd = self.get_argument('pwd')
        if email != '' and pwd != '':
            self.write('Please wait....')
            if backend.user_auth(email, pwd):
                self.redirect("dashboard.html")
            else:
                self.redirect('signin.html')
                self.alert('Invalid Credentials!')
        self.redirect('signin.html')

class SignUpHandler(tornado.web.RequestHandler):
    def get(self):
        print(self)
        email = self.get_argument('email')
        pwd = self.get_argument('pwd')
        cpwd = self.get_argument('cpwd')
        
        if email != '' and pwd != '' and cpwd != '':
            self.write('Please wait....')
            if backend.user_register(email, pwd, cpwd):
                self.redirect("dashboard.html")
            else:
                self.redirect('signin.html')
        self.redirect('signup.html')

def CreateApp():
    return tornado.web.Application([
        (r"/", MainHandler), (r"/signin", SignInHandler), (r"/signup", SignUpHandler),
        (r"/plan", PlanHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path':'./'})
    ])

if __name__ == "__main__":
    app = CreateApp()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
