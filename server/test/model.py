from model import Base
from model import Champion
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest

# to be able to run the following tests, create a user in Postgres
# called 'metarifttester' and a database called 'metarifttest' to which
# metarifttester has access


engine = create_engine("postgresql://falcontester:metarifttester@localhost/metarifttest")

Session = sessionmaker(bind=engine)

class ModelTestMethods(unittest.TestCase):

    def test_createchampion(self):
        test_session = Session()
        fake_champion = Champion(name="Fake", role="11011")
        session.add(fake_champion)
        test_champion = session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(fake_champion is test_champion)
