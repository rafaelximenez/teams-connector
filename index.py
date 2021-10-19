from datetime import datetime
from faker import Faker

fake = Faker()

def __get_period():
    #now=fake.date_time()
    now=datetime.now()

    time=int(f'{now.hour}{str(now.minute).zfill(2)}')
    if time > 0000 and time <= 1200: return 'dia'
    elif time > 1200 and time <= 1800: return 'tarde'
    else: return 'noite'


for i in range(20):
    period = __get_period()
    input('---------------------')