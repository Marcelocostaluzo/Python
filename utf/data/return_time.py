from datetime import datetime

def data_update():
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M")
    return current_time
