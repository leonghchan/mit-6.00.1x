""" 
Problem set 2 - Question 1

Each month, a credit card statement will come with the option for you to pay a minimum amount of your 
charge, usually 2% of the balance due. However, the credit card company earns money by charging interest 
on the balance that you don't pay. So even if you pay credit card payments on time, interest is still 
accruing on the outstanding balance.

Problem set 2 - Question 1 - Paying Debt off in a Year


Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annual_interest_rate - annual interest rate as a decimal
monthly_payment_rate - minimum monthly payment rate as a decimal

So your program only prints out one thing:
the remaining balance at the end of 12 months in the format:
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
"""


def remaining_balance(balance, annual_interest_rate, monthly_payment_rate, months):
    """
    returns the remaining outstanding balance given the balance, annual interest rate, 
    monthly payment rate and number of months defined in the parameters. 
    """
    for i in range(months):
        balance -= balance * monthly_payment_rate
        balance += (annual_interest_rate / 12.0) * balance
        print(f"Month {i + 1} Remaining balance: {round(balance, 2)}")
    print(f"Remaining balance: {round(balance, 2)}")
    return round(balance, 2)


print(remaining_balance(3329, 0.2, 0.04, 12))

# Alternative solution - using while loop
# def remaining_balance(months):
#     no_of_months = 1
#     balance = 484
#     annual_interest_rate = 0.2
#     monthly_payment_rate = 0.04
#     while no_of_months <= months:
#         monthly_payment = balance * monthly_payment_rate
#         unpaid_balance = balance - monthly_payment
#         balance = unpaid_balance + (annual_interest_rate / 12.0) * unpaid_balance
#         # print(f"Month {no_of_months} Remaining balance: {round(balance, 2)}")
#         no_of_months += 1
#     return round(balance, 2)

# print(remaining_balance(12))

