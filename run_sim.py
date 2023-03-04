from teams_matches import teamsMatches
from sim import chanceMakePlayoffs

if __name__ == "__main__":
    format = teamsMatches()
    teams, teams_standings, matches = format.lcs_teams_matches_regular()

    to_playoffs = chanceMakePlayoffs(teams, teams_standings, matches)
    df_team_odds = to_playoffs.run_regular_season(100000, 6)

    print("\n", df_team_odds, "\n")