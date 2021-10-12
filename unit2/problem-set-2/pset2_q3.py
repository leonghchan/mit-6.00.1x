""" 
Problem set 2 - Problem 3 - Using Bisection Search to Make the Program Faster

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

To recap the problem:
We are searching for the smallest monthly payment such that we can pay off the entire balance within a year.

What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that.
If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance,
so we must pay at least this much every month.
One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year.
What we ultimately pay must be greater than what we would've paid in monthly installments,
because the interest was compounded on the balance we didn't pay off each month.
So a good upper bound for the monthly payment would be one-twelfth of the balance,
after having its interest compounded monthly for an entire year.

In short:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent
such that we can pay off the debt within a year. 
"""


def minimum_payment(balance, annual_interest_rate, months=12):
    """
    returns the minimum monthly payment required for the remaining balance to be within
    0.01 of 0 after 12 months of repayment given the parameters using the bisection search
    method.
    """
    monthly_interest_rate = annual_interest_rate / 12.0
    lower_bound = balance / 12.0
    upper_bound = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
    while True:
        remaining_balance = balance
        monthly_payment = (lower_bound + upper_bound) / 2.0
        for month in range(months):
            unpaid_balance = remaining_balance - monthly_payment
            remaining_balance = unpaid_balance + unpaid_balance * monthly_interest_rate
        if abs(remaining_balance) <= 0.01:  # remaining balance within range (0.01) of 0
            return round(monthly_payment, 2)
        elif remaining_balance > 0:  # need to increase monthly payment
            lower_bound = monthly_payment
        elif remaining_balance < 0:  # need to decrease monthly payment
            upper_bound = monthly_payment


print(minimum_payment(balance=320000, annual_interest_rate=0.2, months=12))
print(minimum_payment(balance=999999, annual_interest_rate=0.18, months=12))

