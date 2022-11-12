import csv
import os

#`Date` and `Profit/Losses

months= []
PL = 0
BV= int(0) #Traks of biggest increase value
LV= int(0) #Traks of Lowest increase value
BR= int(0) #Tracks biggeest increse month
LR= int(0) #Tracks lowest increse month
CI= int(1) #current iteration
BI= int(0) #Coordinate of biggest iteration

with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    for row in csvreader:
                months.append(row[0])
                CV = int(row[1])
                PL= PL + CV
                CI = CI + 1
                x, y= row

                if CV >= int(BV):
                        BV = y
                        BR = x
                        BI = CI #Coordinate of biggest iteration
                
                if CV <= int(LV):
                        LV = y
                        LR = x

                        
LM= len(months)
total= round(PL/len(months),2)
data1= ["Financial Analysis", "----------------------------", "Total Months: ", "Total: ", "Average  Change: ", "Greatest Increase in Profits: ", "Greatest Decrease in Profits: "]
data2= [ "", "", LM, "$" + str(PL), total, BR+" ($" + BV + ")", LR+" ($" + LV + ")"]
dataresult = zip(data1, data2)

csvresults= open("analisis_results.csv", "w", newline='')
writer= csv.writer(csvresults)
writer.writerows(dataresult)

print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {LM}')
print(f'Total: ${PL}')
print(f'Average  Change: ${total}')
print(f'Greatest Increase in Profits: {BR} (${BV}) at row {BI}')
print(f'Greatest Decrease in Profits: {LR} (${LV})')
print("----------------------------")

