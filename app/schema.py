# build a schema using pydantic
from pydantic import BaseModel

class Dummy(BaseModel):
   id  : int
   ballid :int
   seriesid:int
   inningNumber : int
   oversActual :float
   overNumber : int
   ballNumber : int
   totalRuns : int
   batsman : str
   bowler  : str
   batsmanRuns : int
   isFour : int
   isSix : int
   isWicket : int
   dismissalType :float
   byes : int
   legbyes : int
   wides : int
   noballs : int
   penalties : int
   Comment : str
   

   class Config:
       orm_mode = True

