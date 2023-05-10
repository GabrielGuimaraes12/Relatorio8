class Game:
    def _init_(self, database):
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

    def create_match(self, players):
        query = "CREATE (m:Match) RETURN id(m) as match_id"
        result = self.db.execute_query(query)

        match_id = result.single()["match_id"]

        for player in players:
            query = "MATCH (p:Player) WHERE id(p) = $player_id CREATE (m)-[:PARTICIPATED_BY]->(p)"
            parameters = {"match_id": match_id, "player_id": player["id"]}
            self.db.execute_query(query, parameters)

        return match_id

    def update_match(self, match_id, result):
        query = "MATCH (m:Match) WHERE id(m) = $match_id SET m.result = $result"
        parameters = {"match_id": match_id, "result": result}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN id(p) as id, p.name as name"
        result = self.db.execute_query(query)

        players = []
        for record in result:
            player = {"id": record["id"], "name": record["name"]}
            players.append(player)

        return players

    def get_match(self, match_id):
        query = "MATCH (m:Match) WHERE id(m) = $match_id RETURN id(m) as id, m.result as result"
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)

        match = None
        if result:
            record = result.single()
            match = {"id": record["id"], "result": record["result"]}

        return match

    def get_player_matches(self, player_id):
        query = "MATCH (m:Match)-[:PARTICIPATED_BY]->(p:Player) WHERE id(p) = $player_id RETURN id(m) as id, m.result as result"
        parameters = {"player_id": player_id}
        result = self.db.execute_query(query, parameters)

        matches = []
        for record in result:
            match = {"id": record["id"], "result": record["result"]}
            matches.append(match)

        return matches