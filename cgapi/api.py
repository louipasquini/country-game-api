from datetime import datetime
from typing import List

from fastapi import FastAPI

from cgapi.core import get_players_from_database
from cgapi.database import get_session
from cgapi.models import Player
from cgapi.serializer import PlayerIn, PlayerOut

from sqlmodel import select

api = FastAPI(title="CGApi")


@api.get("/players/", response_model=List[PlayerOut])
async def list_players():
    players = get_players_from_database()
    return players


@api.post("/players/", response_model=PlayerOut)
async def add_player(player_in: PlayerIn):
    player_in = player_in.dict()
    local_player_in = Player(name=player_in["name"], points=player_in["points"])
    with get_session() as session:
        player = session.exec(select(Player).where(Player.name == local_player_in.name)).first()
        if player != None :
            player.points = local_player_in.points
            player.date = datetime.now()
            session.add(player)
            session.commit()
        elif player == None :
            newplayer = Player(name=local_player_in.name, points=local_player_in.points)
            session.add(newplayer)
            session.commit()
    ending_player = session.exec(select(Player).where(Player.name == local_player_in.name)).first()
    return ending_player
    
