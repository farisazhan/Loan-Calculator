import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if len(sys.argv) < 4 or args.type != ("diff" and "annuity"):
    print("Incorrect parameters")
if args.interest is None:
    print("Incorrect parameters")
    exit(0)
def overpayment(total_paid, principal):
    sum_paid = total_paid - principal
    print(f'Overpayment = {sum_paid}')
    return sum_paid

def diff_payment(principal, periods, interest):
    total_payment = 0
    for i in range(1, periods + 1):
        nominal_i = interest / (12 * 100)
        dm = math.ceil((principal / periods) + nominal_i * (principal - (principal * (i - 1)) / periods))
        print(f'Month {i}: payment is {dm}')
        total_payment += dm
    return total_payment

def x_periods(principal, payment, interest):
    nominal_i = interest / (12 * 100)
    x = (payment / (payment - (nominal_i * principal)))
    num_month = math.ceil(math.log(x, nominal_i + 1))
    total_payment = num_month * payment
    month_conversion = num_month % 12
    year = math.floor(num_month / 12)
    if month_conversion == 0:
        print(f'It will take {year} years to repay this loan!')
    else:
        print(f'It will take {year} years and {month_conversion} months to repay this loan!')
    return total_payment

def x_payment(principal, periods, interest):
    nominal_i = interest / (12 * 100)
    annuity = math.ceil(principal * (nominal_i * (math.pow(1 + nominal_i, periods))) / ((math.pow(1 + nominal_i, periods)) - 1))
    total_payment = annuity * periods
    print(f'Your annuity payment = {annuity}!')
    return total_payment

def x_principal(payment, periods, interest):
    nominal_i = interest / (12 * 100)
    principal = math.ceil(payment / (nominal_i * (math.pow(1 + nominal_i, periods)) / ((math.pow(1 + nominal_i, periods)) - 1)))
    print(f'Your loan principal = {principal}!')
    return principal
    
if args.type == 'diff':
    overpayment(diff_payment(args.principal, args.periods, args.interest), args.principal)
else:
    if not args.periods:
        overpayment(x_periods(args.principal, args.payment, args.interest), args.principal)
    elif not args.payment:
        overpayment(x_payment(args.principal, args.periods, args.interest), args.principal)
    elif not args.principal:
        total = args.periods * args.payment
        print(f'Overpayment = {total - x_principal(args.payment, args.periods, args.interest)}')
