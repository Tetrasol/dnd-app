#!/usr/bin/env python
#
from google.appengine.api import users
import campCampaignManager
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.write('Hello ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/campaign', CampaignManager)
], debug=True)
