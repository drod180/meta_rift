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

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

test_session = Session()

def create_champ_with_name(str):
    fake_champion = Champion(name=str)
    return fake_champion

ali = create_champ_with_name("Muhammad Ali")
test_session.add(ali)
test_session.commit()

class ModelTestMethods(unittest.TestCase):

    def test_createchampion(self):
        fake_champion = create_champ_with_name("Fake")
        test_session.add(fake_champion)
        test_champion = test_session.query(Champion).filter_by(name="Fake").first()
        self.assertTrue(fake_champion is test_champion)
        self.assertTrue(test_champion.role == 0)

    def test_updatewinrate(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        ali.win_rate = .65
        new_ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        self.assertTrue(new_ali.win_rate == .65)

    def test_updatepickrate(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        ali.pick_rate = .42
        ali2 = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        self.assertTrue(ali2.pick_rate == .42)

    def test_updatebanrate(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        ali.ban_rate = .20
        ali2 = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        self.assertTrue(ali.ban_rate == .20)

    def test_updaterole(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        ali.role = 31
        ali2 = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        self.assertTrue(ali2.role == 31)

    def test_updateimageurl(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        ali.image_url = "http://www.someimage.com/38429.jpg"
        ali2 = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        self.assertTrue(ali2.image_url == "http://www.someimage.com/38429.jpg")

    def test_winrate_validation(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        with self.assertRaises(AssertionError):
            ali.win_rate = 1.01

    def test_pickrate_validation(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        with self.assertRaises(AssertionError):
            ali.pick_rate = 1.01

    def test_banrate_validation(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        with self.assertRaises(AssertionError):
            ali.ban_rate = 1.01

    def test_rolevalidation(self):
        ali = test_session.query(Champion).filter_by(name="Muhammad Ali").first()
        with self.assertRaises(AssertionError):
            ali.role = 42
        with self.assertRaises(AssertionError):
            ali.role = -1


if __name__ == '__main__':
    unittest.main()
    Base.metadata.drop_all(engine)
