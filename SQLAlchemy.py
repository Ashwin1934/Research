# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:55:53 2020

@author: ashud
"""

import pandas as pd
import numpy as np
import matplotlib as mp

import sqlalchemy as alchemy
#import mysqlclient as client
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
print(alchemy.__version__)



class User(Base):
    __tablename__ = "person"
    
    id = Column('id', Integer, primary_key = True)
    username = Column('username', String, unique = True)

#engine = create_engine('pymysql://root:Research2020@localhost:3306/MyDatabase', echo = True)
#engine = create_engine('mysql+pymysql://root:Research2020@localhost:3306/MyDatabase')
engine = create_engine('mysql://root:Research2020@localhost', echo = True)
engine.execute("CREATE DATABASE newDataBase")
engine.execute("USE newDataBase")

connection = engine.connect()
Base.metadata.create_all(bind=engine)
    
#trying to connect to a database from SQL workbench
print("Database created in MySQL Workbench")
dbTest = pysql.connect(host="localhost",user= "root", passwd = "Research2020", db = "MyDatabase")
current = dbTest.cursor()
current.execute("INSERT INTO sample_data(firstnames) VALUES('VARUN')")
current.execute("SELECT * FROM sample_data")
for row in current.fetchall() :
    print(row[0], " ", row[1])

print()
print("Database created from SQL command line")

# after creating database from sql cmd line, retrieve the data in python
db = pysql.connect(host="localhost",user= "root", passwd = "Research2020", db = "database125")
curr = db.cursor()
curr.execute("SELECT * FROM examples")
for row in curr.fetchall() :
    print (row[0], " ", row[1])
