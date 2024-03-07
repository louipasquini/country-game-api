from cgapi.core import get_players_from_database, add_player_to_database


def test_add_player_to_database():
    assert add_player_to_database("Loui", 82)


def test_get_players_from_database():
    add_player_to_database("Loui", 82)
    results = get_players_from_database()
    assert len(results) > 0

def test_update_players_from_database():
    add_player_to_database("Loui", 82)
    add_player_to_database("Loui", 85)
    results = get_players_from_database()
    assert len(results) == 1
