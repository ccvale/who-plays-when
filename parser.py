import bs4 as bs
import urllib.request
from getdate import getDate
from Team import Team

gameList = []

def getSchedule(*teams: Team):
    for team in teams:
        req = urllib.request.Request(team.url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urllib.request.urlopen(req)
        soup = bs.BeautifulSoup(source,'lxml')

        #zip
        abbrList = []
        dateList = []
        opponentList = []
        timeList = []

        abbrList.append(team.abbr)
        
        #date list
        if team.league == 'PL':
            for row in soup.select('.matchTeams'):
                dateList.append(row.get_text()[5:].strip())
        else:
            for row in soup.select('.bb--none~ .Table__even+ .Table__even .Table__TD:nth-child(1) span'):
                dateList.append(row.get_text()[5:].strip())

        #time list
        if team.league == 'PL':
            for row in soup.select('.Table__TD > .AnchorLink'):
                timeList.append(row.get_text().strip())
        else:
            for row in soup.select('.bb--none~ .Table__even .Table__TD~ .Table__TD+ .Table__TD span .AnchorLink'):
                timeList.append(row.get_text().strip())

        #opponent list
        if team.league == 'PL':
            for row in soup.select('.AnchorLink.Table__Team'):
                opponentList.append(row.get_text().strip())
        else:
            for row in soup.select('.bb--none~ .Table__even .tc+ span .AnchorLink'):
                if row.get_text() != ' ':
                    opponentList.append(row.get_text().strip())

        gameDay = zip(abbrList, dateList, timeList, opponentList)

        for game in gameDay:
            if game[1] == getDate():
                gameList.append(game)    

    return gameList