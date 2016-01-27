#!/usr/bin/env python -tt

# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    cash_money = []
    pct = 0.01
    
    for i in range(0, years):
    	
    	if i == 0:
    		last_year = 0
    	else:
    		last_year = cash_money[i - 1]

    	this_year = last_year * (1 + growthRate * pct) + salary * save * pct

    	cash_money.append(this_year)

    return cash_money


def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

# testNestEggFixed()

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    cash_money = []
    pct = 0.01
    
    for i in range(0, len(growthRates)):
    	
    	if i == 0:
    		last_year = 0
    	else:
    		last_year = cash_money[i - 1]

    	this_year = last_year * (1 + growthRates[i] * pct) + salary * save * pct

    	cash_money.append(this_year)

    return cash_money

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

# testNestEggVariable()

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    cash_money = []
    pct = 0.01

    for i in range(0, len(growthRates)):
    	
    	if i == 0:
    		last_year = savings
    	else:
    		last_year = cash_money[i - 1]

    	this_year = last_year * (1 + pct * growthRates[i]) - expenses
    	cash_money.append(this_year)

    return cash_money



def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

testPostRetirement()
#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]

    minimum_expenses = 0
    maximum_expenses = savings

    expense_approx = (minimum_expenses + maximum_expenses) / 2
    death_bed = postRetirement(savings, postRetireGrowthRates, expense_approx)[-1]

    while abs(death_bed) > epsilon:
    	if death_bed > 0:
    		minimum_expenses = expense_approx
    		expense_approx = expense_approx = (minimum_expenses + maximum_expenses) / 2
    	else:
    		maximum_expenses = expense_approx
    		expense_approx = expense_approx = (minimum_expenses + maximum_expenses) / 2
    	death_bed = postRetirement(savings, postRetireGrowthRates, expense_approx)[-1]

    return expense_approx


def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

testFindMaxExpenses()
    # TODO: Add more test cases here.