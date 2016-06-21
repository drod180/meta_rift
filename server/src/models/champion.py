from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Champion(Base):
    __tablename__= 'champions'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    role = Column(String)
    win_rate = Column(Float)
    pick_rate = Column(Float)
    ban_rate = Column(Float)
    image_url = Column(String)

    def __repr__(self):
        return "<Champion(name='%s', role='%s', win%='%s')>" % (
            self.name, self.role, self.win_rate
        )
