import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.schema import Dummy as SchemaDummy


from app.schema import Dummy


from app.models import Dummy as ModelDummy


import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
   return {"message": "hello world"}


@app.post('/dummy/', response_model=SchemaDummy)
async def dummy(dummy: SchemaDummy):
   db_dummy = ModelDummy(series_id = dummy.series_id,match_id=dummy.match_id,ball_id=dummy.ball_id,inningNumber=dummy.inningNumber,oversActual = dummy.oversActual,overNumber =dummy.overNumber,ballNumber=dummy.ballNumber,totalRuns=dummy.totalRuns,batsman=dummy.batsman,bowler=dummy.bowler,batsmanRuns=dummy.batsmanRuns,isFour=dummy.isFour,isSix=dummy.isSix,isWicket=dummy.isWicket,dismissalType=dummy.dismissalType,byes=dummy.byes,legbyes=dummy.legbyes,wides=dummy.wides,noballs=dummy.noballs,penalties=dummy.penalties,Comment=dummy.Comment)
   db.session.add(db_dummy)
   db.session.commit()
   return db_dummy

@app.get('/dummy/')
async def dummy():
   dummy = db.session.query(ModelDummy).all()
   return dummy


# To run locally
if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)