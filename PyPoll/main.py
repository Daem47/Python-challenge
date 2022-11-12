import csv
import os
from collections import Counter

data = open("election_data.csv") #`Voter ID`, `County`, and `Candidate`
dataread = csv.reader(data)
next(dataread, None)
Voter_id= []
County= []
Candidates= []
for row in dataread:
    Voter_id.append(row[0])
    County.append(row[0])
    Candidates.append(row[2])
    
result = Counter(Candidates)

    
print("Election Results")
print("-------------------------")
print(f'Total Votes: {int(len(Voter_id))}')
print("-------------------------")
for row in result:
    print(f'{row}: {round((result[row])*100/int(len(Voter_id)),2)}% ({result[row]})')
print("-------------------------")

for row in result:
    print(f'Winner: {row}')
    break
print("-------------------------")
xd= Counter(Candidates).most_common(1)
res = str(xd)[3:-2]
res,_ = res.split("',")
print(f'Winner: {res}')

  #Election Results
  #-------------------------
  #Total Votes: 3521001             * The total number of votes cast
  #-------------------------
  #Khan: 63.000% (2218231)            * A complete list of candidates who received votes
  #Correy: 20.000% (704200)               * The percentage of votes each candidate won
  #Li: 14.000% (492940)                       * The total number of votes each candidate won
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan                           * The winner of the election based on popular vote.
  #-------------------------
