
import webapp2

MESSAGES = '/tmp/messages.txt'

class HelloHandler(webapp2.RequestHandler):
  def get(self):
    msg = 'hello %s' % self.request.headers.get('X-AppEngine-Country', 'world')
    with open(MESSAGES, 'a') as f: f.write(msg)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(msg)

class MessagesHandler(webapp2.RequestHandler):
  def get(self):
    with open(MESSAGES, 'r') as f:
      for msg in f: self.response.out.write(msg)

app = webapp2.WSGIApplication([('/', HelloHandler),
                               ('/messages', MessagesHandler)],
                               debug=True)

