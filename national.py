#Question 2 - Create an application that will give a 10% profit every 24hours

#investment app that returns interest every 24hours
#import time modules
import time
import datetime
profit_percentage = 10
 # user enter name of the investor
name_of_investor = input("enter your name: ")
print('welcome', name_of_investor, 'to cohort4 investment')
  
 #  user enterss the amount to invest
wallet = int(input('enter amount to invest: ')) 
transaction_time = datetime.datetime.now()

while True:
  #  application return 10% on capital
  interest_calc = wallet * profit_percentage / 100
  wallet_balance = wallet + interest_calc 
  text ="{} your account has been credited with the sum of: N{:,.2f} with a 10% profit on your capital")
  print( text.format(name_of_investor, wallet, time_of_transaction))
   #  Add interest every 24hrs

  time.sleep(24)
