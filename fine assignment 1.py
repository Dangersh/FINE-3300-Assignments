# This is the section where inputs will be taken
principal =float(input(('Enter the starting Principal for Balance Balance the Mortgage')))
mortgage_rate = float(input(('Enter the mortgage rate')))
amortization = float(input(('Enter the amortiization period')))

# 1. Convert rate given into a relevant rate, 2 Get amortization input, 3. calculating payment 
def mortgage_payments(principal, mortgage_rate,amortization):
    adj_rate = mortgage_rate/100
    #print (adj_rate)
    monthly_periods = amortization * 12 
    semi_monthly_periods = amortization * 24
    bi_weekly_periods = amortization * 26
    weekly_periods = amortization * 52 

    monthly_rate = (((1+ adj_rate/2) ** (2/12))-1)
    semi_monthly_rate = (((1+ adj_rate/2) ** (2/24))-1)
    bi_weekly_rate = (((1+ adj_rate/2) ** (2/26))-1)
    weekly_rate = (((1+ adj_rate/2) ** (2/52))-1)

    monthly_payment = ((((monthly_rate*(1+monthly_rate)**monthly_periods))/(((1+monthly_rate)**monthly_periods)-1)))*principal
    semi_monthly_payment = ((((semi_monthly_rate*(1+semi_monthly_rate)**semi_monthly_periods))/(((1+semi_monthly_rate)**semi_monthly_periods)-1)))*principal
    bi_weekly_payment = ((((bi_weekly_rate*(1+bi_weekly_rate)**bi_weekly_periods))/(((1+bi_weekly_rate)**bi_weekly_periods)-1)))*principal
    weekly_payment = ((((weekly_rate*(1+weekly_rate)**weekly_periods))/(((1+weekly_rate)**weekly_periods)-1)))*principal
    accelerated_biweekly_payment = (monthly_payment/2) 
    accelerated_weekly_payment = (monthly_payment/4) 
    # Printing Output 
    
    print("Monthly Payment:$",round(monthly_payment,2))
    print("semi_monthly_payment:$",round(semi_monthly_payment,2))
    print("bi_weekly_payment:$",round(bi_weekly_payment,2))
    print("weekly_payment:$",round(weekly_payment,2))
    print("accelerated_biweekly_payment",round(accelerated_biweekly_payment,2))
    print("accelerated_weekly_payment",round(accelerated_weekly_payment,2))

mortgage_payments(principal, mortgage_rate, amortization) 