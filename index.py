from datetime import datetime
from faker import Faker

from teams import Teams

fake = Faker()
teams = Teams('url')

def __get_period():
    #now=fake.date_time()
    now=datetime.now()

    time=int(f'{now.hour}{str(now.minute).zfill(2)}')
    if time > 0000 and time <= 1200: return 'Bom dia'
    elif time > 1200 and time <= 1800: return 'Boa tarde'
    else: return 'Boa noite'

def calculateRangeDate(value, column1, column2):
    if 'nat' in [str(value[column1]).lower(), str(value[column2]).lower()] :
        return 0

    d2 = datetime.strptime(str(value[column1]), '%Y-%m-%d %H:%M:%S')
    d1 = datetime.strptime(str(value[column2]), '%Y-%m-%d %H:%M:%S')
    interval = abs((d2 - d1).days)

    return interval

period = __get_period()

message = f'{period}, tudo bem?'
teams.send_message(message)