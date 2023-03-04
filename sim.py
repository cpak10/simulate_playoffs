import random
import copy
import pandas as pd


class chanceMakePlayoffs:

    def __init__(self, teams, teams_standings, matches):
        self.teams = teams
        self.teams_standings = teams_standings
        self.matches = matches

    def run_regular_season(self, n_sim: int, n_slots: int, team_win_all: str = None):
        """
        Run the rest of regular season. Teams, standings, and matches are defined in teams_matches.py.

        Parameters
        ----------
        n_sim : int
            number of times to run simulation
        n_slots : int
            number of teams that make playoffs
        team_win_all : str
            simulate odds if a team wins every single game

        Outputs
        -------
        df_teams : dataframe
            dataframe of teams and their odds of making playoffs
        
        """

        for i in range(n_sim):

            # simulate the future matches
            teams_standing_dup = copy.deepcopy(self.teams_standings)
            for match in self.matches:
                if team_win_all in match:
                    index = match.index(team_win_all)
                    teams_standing_dup[match[index]][0] += 1
                    if index == 1:
                        teams_standing_dup[match[0]][1] += 1
                    else:
                        teams_standing_dup[match[1]][1] += 1
                else:
                    index = random.randint(0, 1)
                    teams_standing_dup[match[index]][0] += 1
                    if index == 1:
                        teams_standing_dup[match[0]][1] += 1
                    else:
                        teams_standing_dup[match[1]][1] += 1

            teams_standing_dup_srt = [(k, v) for k, v in sorted(teams_standing_dup.items(), key = lambda item: item[1][0], reverse = True)]
            
            # tie break the playoffs teams
            list_teams_playoffs = []
            index_curr = 0
            while len(list_teams_playoffs) < n_slots:
                list_holding = []
                win_prev = None
                if len(list_holding) == 0:
                    list_holding.append(teams_standing_dup_srt[index_curr][0])
                    win_prev = teams_standing_dup_srt[index_curr][1]
                    index_curr += 1
                while win_prev == teams_standing_dup_srt[index_curr][1]:
                    list_holding.append(teams_standing_dup_srt[index_curr][0])
                    index_curr += 1
                if len(list_holding) <= (n_slots - len(list_teams_playoffs)):
                    list_teams_playoffs = list_teams_playoffs + list_holding
                else:
                    list_index = random.sample(range(0, len(list_holding)), (n_slots - len(list_teams_playoffs)))
                    for i in list_index:
                        list_teams_playoffs.append(list_holding[i])

            for i in list_teams_playoffs:
                self.teams[i] += 1

        for key, item in self.teams.items():
            self.teams[key] = round((item / n_sim) * 100, 2)

        df_teams = pd.DataFrame.from_dict(self.teams, orient = "index", columns = ["Playoffs Chance"]).sort_values("Playoffs Chance", ascending = False)
        return df_teams