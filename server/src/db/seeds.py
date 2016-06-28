from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp
import json
import os

ENV = os.environ
user = ENV['metarift_user']
pwd = ENV['metarift_pwd']

champion_model = imp.load_source('champion', '../models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

# To use this locally, create a database called metariftdevelopment and
# replace "metarift:leagueofpidgeons" with "<username>:<password>" of a user with
# access to metariftdevelopment in the line below

# psql_url = "postgresql://metarift:leagueofpidgeons@localhost/metariftdevelopment"
psql_url = "postgresql://" + user + ":" + pwd + "@localhost/metariftdevelopment"

engine = create_engine(psql_url)

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
