from datetime import datetime

# to_datetime converts str dates to datetime objects
def to_datetime(value: str) -> datetime:
    return datetime.strptime(value[:19], '%Y-%m-%d %H:%M:%S')

# delta_in_seconds returns the diference beween value and fisrt in seconds 
def delta_in_seconds(value: datetime, first: datetime) -> int:
    delta = value - first
    return int(delta.total_seconds())