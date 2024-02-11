#here are the standarized tax laws
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000

#user puts their dependents and income
gross_income = float(input("Enter gross income: "))
num_dependents = int(input("Enter number of dependents: "))

#actual deduction of taxes + dependents
taxable_income = gross_income - STANDARD_DEDUCTION - (num_dependents * DEPENDENT_DEDUCTION)

# combines with the tax rate
income_tax = taxable_income * TAX_RATE

# prints it
print(f"Income tax: ${income_tax:.2f}")
