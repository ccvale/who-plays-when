from email.message import EmailMessage
import smtplib
from getdate import *

def gmailInfo():
    '''0 index = from address, 1 index = from pwd, 2 index = to address'''
    with open('gmail.txt', 'r') as txt:
        lines = txt.readlines()
        gmailTokens = []
        for token in lines:
            gmailTokens.append(token.rstrip('\n'))
    return gmailTokens
    

def sendEmail(gameData: list):
    '''Formulate and send email if list contains games played on a given day'''
    '''Handle if list is none also'''

    emailBody = '''Here are the following games:\n'''
    gmail = gmailInfo()
    
    for game in gameData:
        emailBody += f'{game[0]} -> {game[1]} - {game[2]} vs {game[3]}\n'
    
    message = EmailMessage()
    message.set_content(emailBody)
    message['Subject'] = f'Sports Schedule for {getDate()}'
    message['From'] = gmail[0]
    message['To'] = gmail[2]

    with smtplib.SMTP('smtp.gmail.com', 587) as mailServer:
        mailServer.starttls()
        mailServer.login(gmail[0], gmail[1])
        mailServer.send_message(message)
        mailServer.quit()
