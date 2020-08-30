import os
import csv
total = 0
csvpath = os.path.join('Resources', 'election_data.csv')
candidates = {}
win_votes = 0
with open(csvpath, 'r') as file:
    read = csv.reader(file, delimiter = ',')
    next(read)
    for row in read:
        total += 1
        if row[2] not in candidates:
            candidates.update({row[2] : 0})
        if row[2] in candidates:
            candidates[row[2]] += 1
out_path = os.path.join('Resources', 'output.txt')
with open(out_path, 'w') as out_file:
    for c in candidates:
        votes = candidates[c]
        if candidates[c] > win_votes:
            win_votes = candidates[c]
            winner = c
        print(f"{c}: % {round((candidates[c]/total)*100, 4)} ({str(candidates[c])})")
        out_file.write(f"{c}: % {round((candidates[c]/total)*100, 3)} ({str(candidates[c])})\n")
    print(f"Winner: {winner}")
    out_file.write(f"Winner: {winner}")
        
