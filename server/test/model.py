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

class ModelTestMethods(unittest.TestCase):

    def test_createchampion(self):
        test_session = Session()
        fake_champion = Champion(name="Fake", role="11011")
        test_session.add(fake_champion)
        test_champion = test_session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(fake_champion is test_champion)




if __name__ == '__main__':
    unittest.main()
