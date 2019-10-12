import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("signin.html")

class SignInHandler(tornado.web.RequestHandler):
    def get(self):
        print(self)

def CreateApp():
    return tornado.web.Application([(r"/", MainHandler), (r"/test", SignInHandler), (r"/(.*)", tornado.web.StaticFileHandler,{'path':'./'})])

if __name__ == "__main__":
    app = CreateApp()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
