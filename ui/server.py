import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://localhost:8000/signin.html")

class SignInHandler(tornado.web.RequestHandler):
    def get(self):
        print(self)

def CreateApp():
    return tornado.web.Application([(r"/", MainHandler), (r"#signin", SignInHandler)])

if __name__ == "__main__":
    app = CreateApp()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
    