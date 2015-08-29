#!/usr/bin/python
################### Character ########################

class CreateHandler(webapp2.RequestHandler):
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

class AttributeHandler(webapp2.RequestHandler):
    def get(self):
        pass #some data
    def post(self):
        pass # tomato

class StatsHandler(webapp2.RequestHandler):
    def get(self):
        pass #potatos
    def post(self):
        pass  #poTato
