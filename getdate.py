import datetime

monthDict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec',
}

def getDate():
    '''Returns a formatted date that matches schedule parser format'''
    date = datetime.datetime.now()

    month = monthDict[int(str(date)[5:7])]
    day = str(date)[8:10]
    if day[0] == '0':
        day = day[1]

    return f'{month} {day}'


def convertDate(date):
    '''Assumes date is in format DD MON'''
    d = date.split()
    if len(d) == 2:  
        if d[0].startswith('0'):
            d[0] = d[0][1:]
        return f'{d[1].capitalize()} {d[0]}'