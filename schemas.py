from pydantic import BaseModel,ConfigDict
from typing import Optional

class User_Input(BaseModel):
    name : str
    guessed_word : str
    
class Score_Response(BaseModel):
    id : int
    name : str
    guessed_word : str
    score: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class Update_Player(BaseModel):
    name : Optional[str] = None      
    guessed_word : Optional[str] = None 