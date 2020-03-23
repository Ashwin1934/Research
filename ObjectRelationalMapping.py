# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:20:48 2020

@author: ashud
"""

import sqlalchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#root@127.0.0.1:3306

database_URI = 'mysql+pymysql://root:@localhost:3306/MyDatabase'
engine = create_engine(database_URI, echo=True)
base = declarative_base()

session = sessionmaker(bind=engine)()



class Stock(base):
    __tablename__ = "StockPrices"
    ticker = Column('Ticker', String(5), primary_key = True)
    price = Column('Price', Integer)
    volume = Column('Volume', Integer)
    
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price
        
    def __repr__(self):
        return repr(self.ticker + ':' + str(self.price)) 
        
base.metadata.create_all(engine, checkfirst=True)


#base.metadata.drop_all(engine)
        

        
#Stock.__table__.create(bind=engine, checkfirst=True)

#using inspector to detect if table already exists
from sqlalchemy.engine.reflection import Inspector
#engine is declared above
inspector = Inspector.from_engine(engine)
print(inspector.get_table_names())

tables = inspector.get_table_names()
tablename = "stockprices"


#adding to volume column

stocks = session.query(Stock).all()

for stock in stocks:
    volume = 10000
    stock.volume = volume
    session.add(stock)
    
    session.commit()
    session.close()






        
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
#session.close()

"""

#accessing attributes from the objects
print(Microsoft.price)


#inserting multiple objects at once
Nvidia = Stock("NVID",295)
Micron = Stock("MU", 58)
TSM = Stock("TSM", 55)

#session.bulk_save_objects([Nvidia, Micron, TSM])
#session.commit()

#making a query and printing out the entire list
stocks = session.query(Stock).all()
print(stocks)

#alternate way of accessing the objects
for stock in session.query(Stock):
    print(stock)
    
#can print out the attributes as tuples
print(session.query(Stock.ticker, Stock.price).first())

#ordering the objects by a certain attribute (ascending order)
stockList = session.query(Stock).order_by(Stock.price)
for stock in stockList:
    print(stock)
    
#allows you to calculate the sum of a certain column (such as prices)
equity = session.query(func.sum(Stock.price)).scalar()
print(equity)

#putting a lable onto a total or sum
query = session.query(func.sum(Stock.price).label('Equity')).first()
print(query.Equity)

"""


    




    













    


