import os
import csv
num_months = 0
total_pl = 0
great_inc = 0
great_dec = 0
prev_pl = 0
avg_change_total = 0
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as file:
    read = csv.reader(file, delimiter = ',')
    next(file)
    for row in read:
        cur_pl = int(row[1])
        if num_months >= 1:
            avg_change_total += (cur_pl - prev_pl)
        if ((cur_pl - prev_pl) > great_inc):
            great_inc = cur_pl-prev_pl
            inc_mon = row[0]
        elif ((cur_pl - prev_pl) < great_dec):
            great_dec = cur_pl-prev_pl
            dec_mon = row[0]
            
        num_months += 1
        total_pl += int(row[1])
        prev_pl = int(row[1])
        
        
    avg_pl = avg_change_total/(num_months-1)
    print("Total Months: " + str(num_months))
    print("Total: " + str(total_pl))
    print('Average Change: ' + str(avg_pl))
    print('Greatest Increase in Profits: ' + inc_mon + ' ' + str(great_inc))
    print('Greatest Decrease in Profits: ' + dec_mon + ' ' +  str(great_dec))

out_path = os.path.join('Resources', 'out_put_path.txt')
with open(out_path, 'w') as out_file:
    out_file.writelines(["Total Months: " + str(num_months), "\nTotal: " + str(total_pl), '\nAverage Change: ' + str(avg_pl), '\nGreatest Increase in Profits: ' + inc_mon + ' ' + str(great_inc), '\nGreatest Decrease in Profits: ' + dec_mon + ' ' +  str(great_dec)])
    