from pydantic import BaseModel
from typing import List, Optional


class PokemonData(BaseModel):
    id: int
    name: str
    types: List[str]
    height: float
    weight: float
    abilities: List[str]
    evolution_url: Optional[str] = None
    img:str
