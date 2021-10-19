from datetime import datetime
from teams import Teams

from config import URL_TEAMS


teams = Teams(URL_TEAMS)

def __get_period():
    #now=fake.date_time()
    now=datetime.now()

    time=int(f'{now.hour}{str(now.minute).zfill(2)}')
    if time > 0000 and time <= 1200: return 'Bom dia'
    elif time > 1200 and time <= 1800: return 'Boa tarde'
    else: return 'Boa noite'



period = __get_period()

message = f'{period}, tudo bem?'
teams.send_message(message)