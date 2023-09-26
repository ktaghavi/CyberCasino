from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users_table'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    balance = Column(Float)

    user_games = relationship("PlayedGames", back_populates="user")

class PlayedGames(Base):
    __tablename__ = 'played_games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users_table.id'))
    game = Column(String)
    balance_change = Column(Float)

    user = relationship("Users", back_populates="user_games")

if __name__ == '__main__':
    engine = create_engine('sqlite:///casino.db')
    # Users.__table__.drop(engine)
    Base.metadata.create_all(engine)