leagueIDs = {
    0: 'NBA',
    1: 'NHL',
    2: 'MLB',
    3: 'NFL',
    4: 'PL',
    5: 'IPL',
}


premierLeagueClubs = {
    'ARS': '359',
    'AST': '362',
    'BRE': '337',
    'BHA': '331',
    'BUR': '379',
    'CHE': '363',
    'PAL': '384',
    'EVE': '368',
    'LEE': '357',
    'LEI': '375',
    'LIV': '364',
    'MNC': '382',
    'MNU': '360',
    'NEW': '361',
    'NOR': '381',
    'SOT': '376',
    'TOT': '367',
    'WAT': '395',
    'WHU': '371',
    'WOL': '380',
}

class Team:
    '''Requires team abbreviation and leagueID (0 = NBA, 1 = NHL, 2 = MLB, 3 = NFL, 4 = Premier League, 5 = IPL)'''
    def __init__(self, abbr: str, leagueID: int):
        self.abbr = abbr
        self.league = leagueIDs.get(leagueID)
        if leagueID == 4:
            self.url = f'https://www.espn.com/soccer/team/fixtures/_/id/{premierLeagueClubs[self.abbr]}/'
        elif self.league == 'PL':
            self.url = self.url
        else:
            self.url = f'https://www.espn.com/{self.league.lower()}/team/schedule/_/name/{self.abbr.lower()}/'