from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

print(datetime.now() + re(days = 30))
print(datetime.now() + timedelta(days = 365))