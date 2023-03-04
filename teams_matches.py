class teamsMatches:
    def lcs_teams_matches_regular(self):
        teams = {
            "eg": 0,
            "c9": 0,
            "fly": 0,
            "gg": 0,
            "clg": 0,
            "tsm": 0,
            "tl": 0,
            "100": 0,
            "imt": 0,
            "dig": 0
        }
        teams_standings = {
            "eg": [9, 4],
            "c9": [10, 3],
            "fly": [11, 2],
            "gg": [8, 5],
            "clg": [7, 6],
            "tsm": [6, 7],
            "tl": [5, 8],
            "100": [5, 8],
            "imt": [3, 10],
            "dig": [1, 12]
        }
        matches = [
            ["tsm", "tl"], ["imt", "gg"],
            ["fly", "tl"], ["tsm", "imt"], ["eg", "c9"],
            ["gg", "100"], ["clg", "dig"], ["tl", "c9"],
            ["imt", "fly"], ["clg", "eg"], ["dig", "100"],
            ["tsm", "gg"], ["fly", "c9"], ["clg", "gg"],
            ["tsm", "100"], ["imt", "eg"], ["dig", "tl"],
            ["eg", "100"], ["tsm", "dig"], ["clg", "tl"],
            ["imt", "c9"], ["fly", "gg"], ["clg", "c9"],
            ["tsm", "fly"], ["tl", "eg"], ["dig", "gg"],
            ["imt", "100"]
        ]
        return teams, teams_standings, matches