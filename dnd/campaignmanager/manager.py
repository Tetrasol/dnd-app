#!/usr/bin/python
import webapp2

## The CampaignManager is a web request handler for users trying to
## create/edit a DND campaign
class CampaignManager(webapp2.RequestHandler):

    def get(self):
        self.response.write('This is the CampaignManager')
