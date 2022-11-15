import pandas as pd
from datetime import date


today = date.today()
today_less_month = (date.today().replace(month=today.month - 1))

# print(today)
# print(today_less_month)

last_month = pd.date_range(today_less_month, today)

for day in last_month:
    print(day.strftime('%Y-%m-%d'))