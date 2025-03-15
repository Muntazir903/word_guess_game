from sqlalchemy.orm import session
import models,schemas

def play_game(db: session, user_input: schemas.User_Input):
    score = save_score(user_input)  
    db_score = models.Score(name=user_input.name, guessed_word=user_input.guessed_word, score=score )
    db.add(db_score)
    db.commit()
    db.refresh(db_score)

    return {"message": f"Word '{db_score.guessed_word}' saved with score {db_score.score} sucessfully!"}

def save_score(user_input: schemas.User_Input):
    return len(user_input.guessed_word) 

def get_user_scores(db:session):
    return db.query(models.Score).all()
    
def delete_player(db:session, player_id):
    player = db.query(models.Score).filter(models.Score.id==player_id).first()
    if player:
        db.delete(player)
        db.commit()
        
        return {"message": f"Player with id {player_id} is removed sucessfully!"}
    
    return {"error": f"Player not found!"}
   
def modify_player(db:session, player_id ,player_update:schemas.Update_Player):
    player = db.query(models.Score).filter(models.Score.id==player_id).first()

    if player_update.name is not None:
        player.name = player_update.name
    if player_update.guessed_word is not None:
        player.guessed_word = player_update.guessed_word
       
        db.commit()    
        db.refresh(player)
        
        return {"message": f"Player with id {player_id} is updated sucessfully!"}
    
    return {"error": f"Player not found!"}      