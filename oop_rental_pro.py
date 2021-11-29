class property():
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cashflow = []
        self.roi = []
        self.income_1()

    def income_1(self):
        self.income = int(input("How much is your monthly income? "))
        print(f'Your monthly income is ${self.income}.')
        self.expenses_2()

    def expenses_2(self):
        self.expenses = int(input("How much is your monthly expenses? "))
        print(f'Your monthly expenses is ${self.expenses}.')
        self.cashflow_3()
    

    def cashflow_3(self):
        self.cashflow = int(self.income - self.expenses)
        print(f'Your monthly cash flow is ${self.cashflow}.')
        self.roi_4()

        

    def roi_4(self):
        down_payment = int(input("What is your down payment? "))
        print(f'Your down payment is ${down_payment}.')
        closing_costs = int(input("What is your closing costs? "))
        print(f'Your closing costs are ${closing_costs}.')
        rehab_budget = int(input("What is your rehab budget? "))
        print(f'Your rehab budget is ${rehab_budget}. ')
        total_invest = int(down_payment + closing_costs + rehab_budget)
        self.roi = format(self.cashflow*12/total_invest*100, '.2f')

        print(f'Your cash to cash ROI is {self.roi}%.')

my_stuff = property()


    