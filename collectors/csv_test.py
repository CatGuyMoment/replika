path = 'private/dataset.csv'

import csv

data = [
    ['hi','hello']

]

with open(path,'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)