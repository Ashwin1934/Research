# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:20:48 2020

@author: ashud
"""

import sqlalchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#root@127.0.0.1:3306

database_URI = 'mysql+pymysql://root:Research2020@localhost:3306/MyDatabase'
engine = create_engine(database_URI, echo = True)
base = declarative_base()

session = sessionmaker(bind=engine)()


class Stock(base):
    __tablename__ = "StockPrices"
    ticker = Column('Ticker', String(5), primary_key = True)
    price = Column('Price', Integer)
    
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price
        
    def __repr__(self):
        return repr(self.ticker + ':' + str(self.price)) 
        
base.metadata.create_all(engine)
        
Microsoft = Stock("MSFT", 189)
Facebook = Stock("FB", 210)
AMD = Stock("AMD", 50)
TSLA = Stock("TSLA", 820)

#session.add(Microsoft)       #already entered msft into the database
#session.commit()
#session.add(Facebook)
#session.add(AMD)
#session.add(TSLA)
#session.commit()

#accessing attributes from the objects
print(Microsoft.price)


#inserting multiple objects at once
Nvidia = Stock("NVID",295)
Micron = Stock("MU", 58)
TSM = Stock("TSM", 55)

#session.bulk_save_objects([Nvidia, Micron, TSM])
#session.commit()





    













    


