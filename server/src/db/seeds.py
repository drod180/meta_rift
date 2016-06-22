from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp
import json

champion_model = imp.load_source('champion', '../models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

# To use this locally, create a database called metariftdevelopment and
# replace "metarift:leagueofpidgeons" with "<username>:<password>" of a user with
# access to metariftdevelopment in the line below

engine = create_engine("postgresql://metarift:leagueofpidgeons@localhost/metariftdevelopment")

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

raw = open("champions.json")

initial_parse = json.load(raw)

for champ_name in initial_parse['data']:
    champ_record = Champion(name=champ_name, win_rate=0, pick_rate=0, ban_rate=0)
    session.add(champ_record)


session.commit()
