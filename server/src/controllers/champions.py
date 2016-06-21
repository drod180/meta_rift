import falcon
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import imp

champion_model = imp.load_source('champion', '../models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base
