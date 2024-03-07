from typing import List

from sqlmodel import select

from cgapi.database import get_session
from cgapi.models import Player


def add_player_to_database(name: str, points: int) -> bool:
    with get_session() as session:
        try:
            player = session.exec(select(Player).where(Player.name == name)).first()
            print(player)
            if player != None :
                player.points = points
                session.add(player)
                session.commit()
            elif player == None :
                newplayer = Player(name=name, points=points)
                session.add(newplayer)
                session.commit()
        except:
            return False
    return True


def get_players_from_database() -> List[Player]:
    with get_session() as session:
        sql = select(Player)
        return list(session.exec(sql))
