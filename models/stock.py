from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data_base.bd import DataBase as database


class Stock(database.Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String)
    price = Column(Float)
    purchase_date = Column(DateTime, default=datetime.utcnow)

    # Связь с инвестором
    investor_id = Column(Integer, ForeignKey('investors.id'))
    investor = relationship('Investor', back_populates='stocks')
