from database import Database
from game_database import GameDatabase

db=Database("bolt://44.204.103.222:7687", "neo4j", "jacket-slit-byte")
db.drop_all()

game_db = GameDatabase(db)

# Criar um jogador
game_db.create_player("Vitinho")
game_db.create_player("Kayky")
game_db.create_player("Luis")
# Atualizar o nome de um jogador
game_db.update_player(1, "Guima")

# Deletar um jogador
game_db.delete_player(2)

# Obter a lista de jogadores
players = game_db.get_players()
print("Players:")
for player in players:
    print(player)
# Criar partidas
game_db.create_match(1, "Guima Ganhou")
game_db.create_match(2, "Kayky Ganhou")
game_db.create_match(3, "Empate")


game_db.insert_match_player(1, ["Kayky", "Guima"])
game_db.insert_match_player(2, ["Kayky", "Luis"])
game_db.insert_match_player(3, ["Guima", "Luis"])

# Atualizando resultado da partida
game_db.update_match(1, "Guima wins")

# Deletando uma partida
game_db.delete_match(3)

# Mostra partida selecionada
print("Partida:")
print(game_db.get_matches(2))

# Imprime historico de partidas de um jogador

print("Partidas:")
print(game_db.get_player_matches("Kayky"))


# Fechar a conexão com o banco de dados Neo4j
db.close()