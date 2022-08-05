from pathlib Path
from datetime import datetime


def logg(head='INFO', body='Start program'):
    logg_path = Path('data', 'logging.txt')
    logg_time = datetime.now().strftime("%Y-%M-%d | %H:%M:%S | ")
    with open(log_path, 'a') as log:
        text = f'{(head + ":"):7}{log_time:30}{body}\n'
        log.write(text)
