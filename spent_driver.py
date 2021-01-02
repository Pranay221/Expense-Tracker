usage = '''
   
   Expense Tracker CLI.
   
   Usage:
     spent_driver.py init
     spent_driver.py view [<view_category>]
     spent_driver.py <amount> <category> [<message>]
   
   '''

from docopt import docopt
from expense import *
from tabulate import tabulate

args = docopt(usage)

#print(args)

if args['init']:
    init()
    print("User Profile generated")

if args['view']:
    category = args['<view_category>']
    amount, results= view(category)
    print("Total amount = ",amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount=float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print(usage)

