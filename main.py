#!/usr/bin/env python
#
#from google.appengine.api import users
import webapp2, cgi, json, Except

from dnd.character.character import Character


################### Character ########################

class CharacterCreaterHandler(webapp2.RequestHandler):
    def post(self):
        try:
            character_data = json.loads(self.request.body)
            new_adventurer = Character(
                character_data['player_name'],
                character_data['character_name'],
                character_data['race'],
                character_data['character_class']
            )
            print new_adventurer.player_name
        except Exception:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('potato')

class CharacterAttributeHandler(webapp2.RequestHandler):
    def get(self):
        pass #some data
    def post(self):
        pass # tomato 

class CharacterStatsHandler(webapp2.RequestHandler):
    def get(self):
        pass #potatos
    def post(self):
        pass  #poTato

######################################################

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
    ('/api/createcharacter', CharacterCreaterHandler),
    #('/campaign', CampaignManager)
], debug=True)
