from datetime import datetime, timedelta


def get_weekend_date(input_date):
    start_date = datetime.strptime(input_date, '%Y-%m-%d')
    # Convert string to datetime

    seventh_date = start_date + timedelta(days=6)
    return seventh_date.strftime('%Y-%m-%d')
