import tornado.ioloop
import tornado.web

htmlText = """
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <h2>收到post请求</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="请输入你的名字">
            <input type="submit" value="发送post请求">
        </form>
    </body>
</html>
"""
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        pass
        #self.write(htmlText)
    def post(self):
        name = self.get_argument('name',default='匿名',strip=True)
        self.write('Your name is %s'%name)


class InitHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/index.html")

app = tornado.web.Application([
    (r"/index",InitHandler),
    (r"/get", MainHandler),
],static_path='./')

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
