import time
from datetime import datetime, timedelta, date
import pytz


def get_current_ist_timestamp():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist_timezone)


def get_todays_date():
    return get_current_ist_timestamp()


def get_current_time_millis():
    return int(time.time_ns() / 1000000)  # milli seconds


def date_to_str(request_date: date):
    return str(request_date.strftime('%Y-%m-%d'))


def readable_timestamp():
    return str(get_current_ist_timestamp().strftime('%Y-%m-%d %H:%M:%S'))


def readable_timestamp_till_hours():
    return str(get_current_ist_timestamp().strftime('%Y-%m-%d %H'))


def get_current_date_str():
    return str(get_current_ist_timestamp().strftime('%Y-%m-%d'))


def get_current_timestamp():
    return get_current_ist_timestamp()


def get_previous_date_str(date_str):
    datetime_object = datetime.strptime(date_str, "%Y-%m-%d")
    time_delta = timedelta(days=1)
    return str((datetime_object - time_delta).strftime('%Y-%m-%d'))


def get_readable_timestamp():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    return str(get_current_ist_timestamp().strftime('%Y-%m-%d %H:%M:%S'))


def get_ist_timestamp():
    return get_current_ist_timestamp()


def to_ist(utc_timestamp):
    ist_timezone = pytz.timezone('Asia/Kolkata')
    return utc_timestamp.astimezone(ist_timezone)


def str_to_datetime(request_date_str: str, request_timezone=pytz.timezone('Asia/Kolkata')):
    datetime_obj = datetime.strptime(request_date_str, "%Y-%m-%d %H:%M:%S")
    datetime_ist = request_timezone.localize(datetime_obj)
    return datetime_ist


def str_to_date(request_date_str: str, request_timezone=pytz.timezone('Asia/Kolkata')):
    datetime_obj = datetime.strptime(request_date_str, "%Y-%m-%d")
    datetime_ist = request_timezone.localize(datetime_obj)
    return datetime_ist.date()


def get_previous_date(request_date: datetime):
    request_date_str = str(request_date.strftime('%Y-%m-%d'))
    prev_date_str = get_previous_date_str(request_date_str)
    prev_date = datetime.strptime(prev_date_str, "%Y-%m-%d")
    return prev_date
