#!/usr/bin/env python
#
#from google.appengine.api import users
import webapp2, cgi, json, Except

from character.handler import CreateHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('potato')
        #user = users.get_current_user()

        #if user:
            #self.response.write('Hello ' + user.nickname())
        #else:
            #self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api/character/create', CreateHandler),
    #('/campaign', CampaignManager)
], debug=True)
