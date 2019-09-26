from datetime import datetime


def ubah(date):
    d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%b - %Y')
    return d