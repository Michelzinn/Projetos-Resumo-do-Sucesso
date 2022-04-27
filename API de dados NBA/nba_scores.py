from requests import get

BASE_URL = "http://data.nba.net"  # variavel global, consegue ser utilizada dentro da função
ALL_JSON = "/prod/v1/today.json"


def get_links():
    response = get(BASE_URL + ALL_JSON).json()
    return response["links"]


def get_currentScoreboard():
    response = get(BASE_URL + get_links()["currentScoreboard"]).json()
    games = response["games"]
    for game in games:
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        clock = game["clock"]
        period = game["period"]

        print("******************************************\n")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} x {away_team['score']}")
        print(f"{clock} (Time) - {period['current']} (Period) \n")





def get_teams_stats():
    stats = get_links()["leagueTeamStatsLeaders"]
    data = get(BASE_URL + stats).json()
    teams = data["league"]["standard"]["regularSeason"]["teams"]

    teams = list(filter(lambda x: x["name"] != "Team", teams))
    teams.sort(key=lambda x: int(x["ppg"]["rank"]))

    for team in teams:
        team_name = team["name"]
        nickname = team["nickname"]
        ppg_avg = team["ppg"]["avg"]
        rank = team["ppg"]["rank"]

        print(f"RANK: {rank} | {team_name} - {nickname} | Average Points Per Game (PPG): {ppg_avg} ")





while True:
    print ('********************************\n')
    print ('Confira os dados da NBA!\n')
    print ('Digite 1 para ver os jogos\n')
    print ('Digite 2 para ver o Ranking dos times (PPG)\n')
    print ('Digite 3 para encerrar o programa\n')

    user_choice = input("Opção: ")

    if user_choice == "1":
        get_currentScoreboard()

    elif user_choice == "2":
        get_teams_stats()

    elif user_choice == "3":
        print("Programa Encerrado!")
        quit()

    elif user_choice != "1" or "2" or "3":
        print("Opção invalida")
        print("Digite uma opção válida!")


