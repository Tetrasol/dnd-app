#!/usr/bin/env python
#
from campaignmanager.manager import CampaignManager
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/campaign', CampaignManager)
], debug=True)
