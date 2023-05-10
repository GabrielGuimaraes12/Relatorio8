from database import Database
from game_database import Game

db=Database("bolt://44.193.3.186:7687", "neo4j", "remainder-ground-turbine")
db.drop_all()

game_db = Game(db)


# cria um novo jogador
game_db.create_player("Guima")
game_db.create_player("Kayky")

# atualiza o nome do jogador com id 0 para "Bob"
game_db.update_player(0, "Bob")

# recupera todos os jogadores do banco de dados
players = game_db.get_players()
print("Jogadores cadastrados:")
for player in players:
    print(player["name"])

# cria uma partida com os jogadores com id 0 e 1 e com resultado "Empate"
game_db.create_match([0, 1], "Empate")

# recupera todas as partidas do banco de dados
matches = game_db.get_matches()
print("Partidas registradas:")
for match in matches:
    print("Resultado: {}".format(match["result"]))

# recupera todas as partidas em que o jogador com id 0 participou
player_matches = game_db.get_player_matches(0)
print("Partidas do jogador com id 0:")
for match in player_matches:
    print("Resultado: {}".format(match["result"]))

# deleta o jogador com id 0
game_db.delete_player(0)

# fecha a conexão com o banco de dados
db.close()