from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Champion(Base):
    __tablename__= 'champions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    pick_rate = Column(Float)
    ban_rate = Column(Float)
    image_url = Column(String)

    def __repr__(self):
        return "<Champion(name='%s', role='%s')>" % (
            self.name, self.role
        )
