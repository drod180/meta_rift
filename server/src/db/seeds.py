from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp
import json
import os

ENV = imp.load_source('keys', '../../config/settings.py').keys
user = ENV['dbuser']
pwd = ENV['dbpwd']

champion_model = imp.load_source('champion', '../models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

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
