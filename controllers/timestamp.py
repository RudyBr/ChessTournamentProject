from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%d/%m/%Y à %H:%M")
