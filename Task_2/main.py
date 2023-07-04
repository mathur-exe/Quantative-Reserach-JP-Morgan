from datetime import date
import math

def price_contract(in_dates, in_prices, out_dates, out_prices, rate, storage_cost_rate, total_vol, injection_withdrawal_cost_rate):
    volume = 0
    buy_cost = 0
    cash_in = 0
    last_date = min(min(in_dates), min(out_dates))

    # Ensure dates are in sequence
    all_dates = sorted(set(in_dates + out_dates))
    for i in range(len(all_dates)):
    # processing code for each date
        start_date = all_dates[i]
        if start_date in in_dates:
        # Inject on these dates and sum up cash flows
            if volume + rate <= total_vol:
                volume += rate
                # Cost to purchase gas
                buy_cost += rate * in_prices[in_dates.index(start_date)]

                # Injection cost
                injection_cost = rate * injection_withdrawal_cost_rate
                buy_cost += injection_cost
                print(f'Injected gas on {start_date} at a price of {in_prices[in_dates.index(start_date)]}')
            else:
                # can't inject cuz curr_vol + rate > total_vol
                print(f'Injection is not possible on date {start_date} as there is insufficient space in the storage facility')
        elif start_date in out_dates:
            #Withdraw on these dates and sum cash flows
            if volume >= rate:
                volume -= rate
                cash_in += rate * out_prices[out_dates.index(start_date)]
                # Withdrawal cost
                withdrawal_cost = rate * injection_withdrawal_cost_rate
                cash_in -= withdrawal_cost
                print(f'Extracted gas on {start_date} at a price of {out_prices[out_dates.index(start_date)]}')
            else:
                # can't withdraw cuz curr_vol < rate
                print(f'Extraction is not possible on date {start_date} as there is insufficient volume of gas stored')
    
    store_cost = math.ceil((max(out_dates) - min(in_dates)).days // 30) * storage_cost_rate
    return cash_in - store_cost - buy_cost

in_dates = [date(2022, 1, 1), date(2022, 2, 1), date(2022, 2, 21), date(2022, 4, 1)] 
in_prices = [20, 21, 20.5, 22]
out_dates = [date(2022, 1, 27), date(2022, 2, 15), date(2022, 3, 20), date(2022, 6, 1)] 
out_prices = [23, 19, 21, 25] 

rate = 100000  # rate of gas in cubic feet per day
storage_cost_rate = 10000  # total volume in cubic feet
injection_withdrawal_cost_rate = 0.0005 
max_storage_volume = 500000 # max_capacity of storage facility in cubic feet
result = price_contract(in_dates, in_prices, out_dates, out_prices, rate, storage_cost_rate, max_storage_volume, injection_withdrawal_cost_rate)
print()
print(f"The value of the contract is: ${result}")

'''
1. The function first ensures that all the dates are in sequence and sorted in ascending order. 
2.Then, it iterates over all the dates and calculates the cash flows on each date. 
    - If the current date is an injection date 
        --> injects gas into the storage facility and 
        --> calculates the cost to store the gas, 
        --> the cost to purchase the gas,
        --> and the injection cost
    - If the current date is a withdrawal date
        --> withdraws gas from the storage facility and
        --> calculates the cash inflow from selling the gas, 
        --> the cost to store the remaining gas, 
        --> and the withdrawal cost.

3. function returns the net profit or loss by 
    --> selling_the_gas - storage_cost - cost_to_purchase_gas
'''
