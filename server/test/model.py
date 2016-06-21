from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest
import imp


champion_model = imp.load_source('champion', '../src/models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

# to be able to run the following tests, create a user in Postgres
# called 'metarifttester' and a database called 'metarifttest' to which
# metarifttester has access, then replace 'password' with the user's password


engine = create_engine("postgresql://metarifttester:password@localhost/metarifttest")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

test_session = Session()

class ModelTestMethods(unittest.TestCase):

    def test_createchampion(self):
        fake_champion = Champion(name="Fake", role="11011")
        test_session.add(fake_champion)
        test_champion = test_session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(fake_champion is test_champion)

    def test_updatewinrate(self):
        test_champion = test_session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(test_champion.win_rate == None)
        test_champion.win_rate = .65
        test_champion2 = test_session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(test_champion2.win_rate == .65)





if __name__ == '__main__':
    unittest.main()
    Base.metadata.drop_all(engine)
