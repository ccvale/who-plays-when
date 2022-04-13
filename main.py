from Team import Team
from parser import getSchedule
from mail import sendEmail
from config import *


if __name__ == '__main__':
    sendEmail(getSchedule(*configuredTeams()))
    
