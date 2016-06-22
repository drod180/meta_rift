from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import validates

Base = declarative_base()

def rate_check(num):
    return (num == None) or (num >= 0 and num <= 1)

class Champion(Base):
    __tablename__= 'champions'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    role = Column(Integer, default=0)
    win_rate = Column(Float)
    pick_rate = Column(Float)
    ban_rate = Column(Float)
    image_url = Column(String)

    @validates('win_rate')
    def validate_win_rate(self, key, value):
        assert rate_check(value)
        return value

    @validates('pick_rate')
    def validate_pick_rate(self, key, value):
        assert rate_check(value)
        return value

    @validates('ban_rate')
    def validate_ban_rate(self, key, value):
        assert rate_check(value)
        return value

    @validates('role')
    def validates_role(self, key, value):
        assert value >= 0 and value <= 31
        return value

    def __repr__(self):
        return "<Champion(name='%s', role='%s', win%='%s')>" % (
            self.name, self.role, self.win_rate
        )
