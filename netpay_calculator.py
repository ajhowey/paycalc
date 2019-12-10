#!/usr/bin/env python

H1 = 0
OT1 = 0
print("\n\n")
for x in [1, 2]:
    Hours = float(input("Enter the number of hours worked in week" + str(x) + ":  "))
    if Hours > 40:
        OverTime = Hours - 40
        Hours = Hours - OverTime
    else:
        OverTime = 0
    H1 += Hours
    OT1 += OverTime
Hours = H1
OverTime = OT1
# print(str(Hours), str(OverTime))
TotalHours = Hours + OverTime
PayRate = float(input("Enter your pay rate per hour:  "))
OverTimePayRate = PayRate * 1.5
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
print("\n\nTotal Hours for this two week period:\t" + str(TotalHours) + "\n\tRegular Hours:\t\t\t" + str(Hours) + "\n\tOvertime Hours:\t\t\t" + str(OverTime) + "\n\nGross Pay:\t\t\t\t" + str(GrossPay) + "\n\tRegular Pay:\t\t\t" + str(RegularPay) + "\n\tOvertime Pay:\t\t\t" + str(OverTimePay) + "\n\nFederal Income Tax:\t\t\t" + str(FedTax) + "\nState Income Tax:\t\t\t" + str(StateTax) + "\nFICA Tax:\t\t\t\t" + str(FicaTax) + "\nUnemployment Insurance:\t\t\t" + str(SUI_SDI)  + "\n\nNet Pay:\t\t\t\t" + str(NetPay) + "\n\n")
