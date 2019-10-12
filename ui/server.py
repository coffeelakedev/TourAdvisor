import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://touradvisorapp.web.app/dashboard.html")

def CreateApp():
    return tornado.web.Application([(r"/", MainHandler), ])

if __name__ == "__main__":
    app = CreateApp()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()