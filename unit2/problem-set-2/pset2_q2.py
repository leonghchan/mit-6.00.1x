""" 
Problem set 2 - Question 2 - Paying Debt off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. By a fixed monthly payment, we mean a single 
number which does not change each month, but instead is a constant amount that will be paid 
each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annual_interest_rate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt
in under 1 year, for example:
Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the 
month (after the payment for that month is made). The monthly payment must be a multiple of 
$10 and is the same for all months. Notice that it is possible for the balance to become 
negative using this payment scheme, which is okay. A summary of the required math is found 
below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
 """


def minimum_payment(balance, annual_interest_rate, months=12):
    """
    returns the minimum fixed monthly payment required to achieve a balance of 0 at the 
    end of 12 months. 
    """
    initial_balance = balance
    min_monthly_payment = 10
    while True:
        for month in range(months):
            balance -= min_monthly_payment
            balance += (annual_interest_rate / 12.0) * balance
        if balance <= 0:
            print(f"Lowest payment: {min_monthly_payment}")
            return min_monthly_payment
        else:
            balance = initial_balance
            min_monthly_payment += 10


print(minimum_payment(balance=3329, annual_interest_rate=0.2, months=12))
print(minimum_payment(balance=4773, annual_interest_rate=0.2, months=12))
print(minimum_payment(balance=3926, annual_interest_rate=0.2, months=12))

