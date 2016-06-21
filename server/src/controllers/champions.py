import falcon
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp

champion_model = imp.load_source('champion', 'src/models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

engine = create_engine("postgresql://metarift:leagueofpidgeons@localhost/metariftdevelopment")

Session = sessionmaker(bind=engine)

class ChampionShow():

    def on_get(self, req, resp, name):
        show_session = Session()
        hero = show_session.query(Champion).filter(Champion.name == name).one_or_none()
        if hero == None:
            resp.body = "No such hero found"
        else:
            hero_object = {'id': hero.id,
                           'name': hero.name,
                           'role': hero.role,
                           'win_rate': hero.win_rate,
                           'ban_rate': hero.ban_rate,
                           'pick_rate': hero.pick_rate,
                           'image': hero.image_url
                           }
            resp.data = json.dumps(hero_object)
