from database import Database
from game_database import Game
db=Database("bolt://44.193.3.186:7687", "neo4j", "remainder-ground-turbine")
db.drop_all()

game_db = Game(db)

# Cria dois jogadores
game_db.create_player("João")
game_db.create_player("Maria")

# Cria uma partida com os jogadores criados
players = ["João", "Maria"]
game_db.create_match(players)

# Registra o resultado da partida
scores = {"João": 10, "Maria": 5}
game_db.update_match_result(1, scores)

# Busca informações sobre a partida
match_info = game_db.get_match_info(1)
print(match_info)

# Busca o histórico de partidas do jogador "João"
player_history = game_db.get_player_history("João")
print(player_history)

# Atualiza o nome do jogador "Maria"
game_db.update_player_name(2, "Mariana")

# Deleta a partida criada
game_db.delete_match(1)

# Fecha a conexão com o banco de dados
db.close()
