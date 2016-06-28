import falcon
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp

ENV = imp.load_source('keys', 'config/settings.py').keys
user = ENV['dbuser']
pwd = ENV['dbpwd']

champion_model = imp.load_source('champion', 'src/models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

psql_url = "postgresql://" + user + ":" + pwd + "@localhost/metariftdevelopment"

engine = create_engine(psql_url)

Session = sessionmaker(bind=engine)

class ChampionShow():

    def on_get(self, req, resp, name):
        show_session = Session()
        champion = show_session.query(Champion).filter(Champion.name == name).one_or_none()
        if champion == None:
            resp.body = "No such champion found"
        else:
            champion_object = {'id': champion.id,
                'name': champion.name,
                'role': champion.role,
                'win_rate': champion.win_rate,
                'ban_rate': champion.ban_rate,
                'pick_rate': champion.pick_rate,
                'image': champion.image_url
            }
            resp.data = json.dumps(champion_object)

class ChampionIndex():

    def on_get(self, req, resp):
        index_session = Session()
        champions_object = {}
        for champion in index_session.query(Champion).all():
            champion_object = {'id': champion.id,
                'name': champion.name,
                'role': champion.role,
                'win_rate': champion.win_rate,
                'ban_rate': champion.ban_rate,
                'pick_rate': champion.pick_rate,
                'image': champion.image_url
            }
            champions_object[champion.id] = champion_object

        resp.data = json.dumps(champions_object)
