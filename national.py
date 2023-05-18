#Question 2 - Create an application that will give a 10% profit every 24hours

#investment app that returns interest every 24hours
#import time modules
import time
profit_percentage = 10

def investment_timer():
    # user enter name of the investor

 name_of_investor = "nimah"
 print('welcome', name_of_investor, 'to cohort4 application')

#  user enterss the amount to invest
 wallet = 10000
 
#  application return 10% on capital
 interest_calc = wallet * profit_percentage / 100
 wallet_balance = wallet + interest_calc
 print(name_of_investor, 'your wallet has been credited with the sum of:', 'N', wallet_balance,"with a 10% interest on your capital")
 

#  Add interest every 24hrs
while True:
  investment_timer()
  time.sleep(24)
