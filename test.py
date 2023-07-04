from datetime import date
import math

in_dates = [date(2022, 1, 1), date(2022, 2, 1), date(2022, 2, 21), date(2022, 4, 1)] #injection dates
in_prices = [20, 21, 20.5, 22]#prices on the injection days

for i in range(len(in_dates)):
    y = in_dates.index(date(2022, 2, 21))
    # x = in_prices[in_dates.index(date(2022, 1, 1))]
    print(y)