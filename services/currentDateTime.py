from datetime import datetime

from services.timeToWords import printTime

h = datetime.now().hour
m = datetime.now().minute
time = printTime(h, m)
