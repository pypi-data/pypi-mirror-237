from datetime import datetime


def format(dt: datetime = datetime.now(), format: str = "%Y-%m-%dT%H:%M:%S.%f"):
    return dt.strftime(format)


def parse(dt_str: str, format: str = "%Y-%m-%dT%H:%M:%S.%f"):
    return datetime.strptime(dt_str, format)
