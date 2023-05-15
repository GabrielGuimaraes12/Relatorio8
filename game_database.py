class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, name):
        query = "MATCH (p:Player) WHERE id(p) = $player_id SET p.name = $name"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player) WHERE id(p) = $player_id DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN id(p) as id, p.name as name"
        result = self.db.execute_query(query)

        players = []
        for record in result:
            player = {"id": record["id"], "name": record["name"]}
            players.append(player)

        return players

    def get_matches(self, id):
        query = "MATCH (p:Player)<-[:POSSUI]-(m:Match) WHERE m.id = $id RETURN p.name AS name, m.result AS match_result"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["match_result"]) for result in results]

    def get_player_matches(self, player_name):
        query = "MATCH (p:Player)<-[:POSSUI]-(m:Match) WHERE p.name = $player_name RETURN m.result AS match_result"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result["match_result"]) for result in results]

    def update_match(self, id, new_result):
        query = "MATCH (m:Match {id: $id}) SET m.result = $new_result"
        parameters = {"id": id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    def insert_match_player(self, match_id, player_names):
        query = "MATCH (m:Match {id: $match_id}) MATCH (p:Player) WHERE p.name IN $player_names CREATE (m)-[:POSSUI]->(p)"
        parameters = {"match_id": match_id, "player_names": player_names}
        self.db.execute_query(query, parameters)

    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id})-[:POSSUI]->(p:Player) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    def create_match(self, id, result):
        query = "CREATE (:Match {id: $id, result: $result})"
        parameters = {"id": id, "result": result}
        self.db.execute_query(query, parameters)