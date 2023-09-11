from pathlib import Path
from auth import get_access_token
from calendar_processing import get_raw_events, raw_events_to_calendar
from datetime import date, timedelta
import argparse

def get_calendar(login, password, start, end, output):
    token = get_access_token(login, password)
    events = get_raw_events(token, start, end)
    calendar = raw_events_to_calendar(events)
    with open(output, 'w') as file:
        file.write("\n".join(map(str.strip, calendar)))

def check_dates(dates):
    try:
        converted_date = date.fromisoformat(dates)
        return dates
    except Exception:
        raise argparse.ArgumentTypeError('Date was not supplied with format YYYY-MM-DD')

if __name__ == '__main__':
    today = date.today()
    day = timedelta(days=1)
    half_year = timedelta(days=180)
    def_day_from = date.isoformat(today - day)
    def_day_until = date.isoformat(today + half_year)
    parser = argparse.ArgumentParser(
            prog='my.itmo.ru schedule to iCal converter',
            description='Name explains it')
    parser.add_argument('login')
    parser.add_argument('password')
    parser.add_argument('-o', '--output', default='my.itmo.ics',
                        help='Path to the file to save the calendar to')
    parser.add_argument('-s', '--start', default=def_day_from,
                        type=check_dates,
                        help='Where to start calendar events from. Provide date as YYYY-MM-DD. Defaults to yesterday.')
    parser.add_argument('-e', '--end', default=def_day_until,
                        type=check_dates,
                        help='Where to end calendar events. Provide date as YYYY-MM-DD. Defaults to 180 days ahead of today.')
    args = parser.parse_args()
    get_calendar(**vars(args))
