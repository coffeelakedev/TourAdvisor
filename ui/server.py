import tornado.ioloop
import tornado.web

import backend

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("signin.html")

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
        (r"/(.*)", tornado.web.StaticFileHandler, {'path':'./'})
    ])

if __name__ == "__main__":
    app = CreateApp()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
