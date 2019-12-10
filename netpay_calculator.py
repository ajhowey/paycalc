#!/usr/bin/env python


# import only system from os 
from os import system, name 
  
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
# now call function we defined above 
clear() 

####
# collects information about amount of time worked
####
H1 = 0
OT1 = 0
for x in [1, 2]:
	Days = int(input("\nEnter the number of days worked in week" + str(x) + ":  "))
	for day in range(Days):
		Hours = int(input("\tEnter the number of hours worked in day" + str(day+1) + ":  "))
		### determines whether there is any overtime hours
		if Hours > 8:
			OverTime = Hours - 8
			Hours = Hours - OverTime
		else:
			OverTime = 0
		### Increments regular time and overtime hours
		H1 += Hours
		OT1 += OverTime
Hours = H1
OverTime = OT1
TotalHours = Hours + OverTime

####
# Sets the rate of pay
####
PayRate = float(input("\nEnter your pay rate per hour:  "))
OverTimePayRate = PayRate * 1.5

####
# Calculates Base Pay, Gross Pay, required taxes, and Net Pay
####
RegularPay = Hours * PayRate
OverTimePay = OverTime * OverTimePayRate
GrossPay = RegularPay + OverTimePay
FedTaxPercent = .24
StateTaxPercent = .093
FicaTaxPercent = .0765
SUI_SDI_Percent = .0095
FedTax = round(GrossPay * FedTaxPercent,2)
StateTax = round(GrossPay * StateTaxPercent,2)
FicaTax = round(GrossPay * FicaTaxPercent,2)
SUI_SDI = round(GrossPay * SUI_SDI_Percent,2)
NetPay = round(GrossPay - FedTax - StateTax - FicaTax - SUI_SDI, 2)

####
# Displays the final results of the calculations
####
print("\n\nTotal Hours for this two week period:\t" + str(TotalHours) + "\n\tRegular Hours:\t\t\t" + str(Hours) + "\n\tOvertime Hours:\t\t\t" + str(OverTime) + "\n\nGross Pay:\t\t\t\t" + str(GrossPay) + "\n\tRegular Pay:\t\t\t" + str(RegularPay) + "\n\tOvertime Pay:\t\t\t" + str(OverTimePay) + "\n\nFederal Income Tax:\t\t\t" + str(FedTax) + "\nState Income Tax:\t\t\t" + str(StateTax) + "\nFICA Tax:\t\t\t\t" + str(FicaTax) + "\nUnemployment Insurance:\t\t\t" + str(SUI_SDI)  + "\n\nNet Pay:\t\t\t\t" + str(NetPay) + "\n\n")
