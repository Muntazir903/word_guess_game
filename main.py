import crud,models,schemas
from sqlalchemy.orm import session
from database import local_session,engine,Base
from fastapi import FastAPI,Depends,HTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/play/",response_model=dict)
def play_game(user_input: schemas.User_Input, db: session=Depends(get_db)):
    
    return crud.play_game(db,user_input)             

@app.get("/scores/",response_model=list[schemas.Score_Response])
def get_all_score(db: session=Depends(get_db)):
    
    return crud.get_user_scores(db)

@app.delete("/player/{player_id}")
def delete_player(player_id:int, db: session=Depends(get_db)):
    result = crud.delete_player(db,player_id)
    if "error" in result:
        raise HTTPException(status_code=404,detail=result["error"])
    return result

@app.put("/player/{player_id}")
def modify_player(player_id, player_update:schemas.Update_Player, db: session=Depends(get_db)):
    result = crud.modify_player(db,player_id,player_update)
    if "error" in result:
        raise HTTPException(status_code=404,detail=result["error"])
    return result   