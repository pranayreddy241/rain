from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Dummy (Base):
   __tablename__ = 'dummy'
   id  = Column(Integer)
   ballid = Column(Integer, primary_key=True, index=True)
   seriesid = Column(Integer)
   inningNumber = Column(Integer)
   oversActual = Column(Float)
   overNumber = Column(Integer)
   ballNumber  =Column(Integer)
   totalRuns = Column(Integer)
   batsman = Column(String)
   bowler  = Column(String)
   batsmanRuns =Column(Integer)
   isFour = Column(Integer)
   isSix  = Column(Integer)
   isWicket =Column(Integer)
   dismissalType = Column(Float)
   byes = Column(Integer)
   legbyes =Column(Integer)
   wides =Column(Integer)
   noballs =Column(Integer)
   penalties = Column(Integer)
   Comment = Column(String)
   
