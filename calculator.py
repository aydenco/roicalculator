class Roicalc():
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.total_invest = 0
        self.roi = 0


    def findcosts(self):
        tax =  float(input("How much do you pay in taxes? $"))
        insurance = float(input("How much do you pay for insurance? $"))
        utilities = float(input("How much do you pay for utilities? $"))
        hoa = float(input("How much do you pay toward the HOA? $"))
        landscape = float(input("How much do you pay for landscaping? "))
        vacancy = float(input("How much do you set aside for vacancy? (Recommended 5 percent of rental income) $"))
        repairs = float(input("How much do you set aside for repairs? (Recommended $50 a month per unit) $"))
        capex = float(input("How much do you set aside for capital expenses? (Recommended $50 a month per unit) $"))
        prop_manage = float(input("How much do you pay for property management? $"))
        mortgage = float(input("How much is your monthly mortgage? $"))
        self.expenses= tax + insurance + utilities + hoa + landscape + vacancy + repairs + capex + prop_manage + mortgage
        print(f"Your total monthly expenses is ${self.expenses}. ")

    def findinvestments(self):
        down_payment = float(input("How much was the down payment? $"))
        closing_costs = float(input("How much were the closing costs? $"))
        rehab_budget = float(input("How much were the initial repairs? $"))
        misc_invest = float(input("Please enter any other investment costs. If there were none, enter 0. $"))
        self.total_invest = down_payment + closing_costs + rehab_budget + misc_invest
        print(f"Your total investment is ${self.total_invest}")
    
    def returnoninvest(self):
        self.income = float(input("How much do you recieve in income from this property? $"))
        cash_flow = self.income - self.expenses
        print(f"Your monthly cash flow is ${cash_flow} ")
        acf = cash_flow * 12
        self.roi = acf / self.total_invest * 100
        print(f"Your cash-on-cash return is {'%.2f' % self.roi}%. ")

    def run(self):
        self.findcosts()
        self.findinvestments()
        self.returnoninvest()

duplex = Roicalc()

duplex.run()