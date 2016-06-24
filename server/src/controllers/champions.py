import falcon
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp

champion_model = imp.load_source('champion', 'src/models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

# To use this locally, create a database called metariftdevelopment and
# replace "metarift:leagueofpidgeons" with "<username>:<password>" of a user with
# access to metariftdevelopment in the line below

psql_url = "postgresql://metarift:leagueofpidgeons@localhost/metariftdevelopment"

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
