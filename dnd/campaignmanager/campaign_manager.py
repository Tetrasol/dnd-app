import cgi
import webapp2
class CampaignManager(webapp2.RequestHandler):
    def post(self):
        self.response.out.write(cgi.escape(self.request.get('content')))

    def get(self):
        self.response.write('This is the CampaignManager')
