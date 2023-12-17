from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_base.bd import DataBase as database


class Investor(database.Base):
    __tablename__ = 'investors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    login = Column(String, unique=True)
    password = Column(String)
    stocks = relationship('Stock', back_populates='investor')
