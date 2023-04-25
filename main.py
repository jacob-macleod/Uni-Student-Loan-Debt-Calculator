yearsToPay = 40

# Costs: 27000 plus inflatipn - 0.03 ^ 30
# Plus 30000 living cost money although not everything is a loan

def calculateYearlySalary(yearlySalary):
    upperSalary = 25000

    deductableMoney = yearlySalary - upperSalary
    moneyTaxed = deductableMoney * 0.09
    moneyPaid = 0
    universityMoneyPaid = 27000 + 30000

    for i in range(0, 30):
        moneyPaid = moneyPaid + moneyTaxed
        universityMoneyPaid = universityMoneyPaid

    print ("Money paid is " +str( moneyPaid))
    print ("University Money Paid is " + str(universityMoneyPaid))
    if moneyPaid > universityMoneyPaid:
        print ("DEAL MADE: NO")
    else:
        print ("DEAL MADE: YES")

    print ("---------------")

i = 30000
while i < 100000:
    i = i + 5000
    print ("Salary is " + str(i))
    calculateYearlySalary(i)
