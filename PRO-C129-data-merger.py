import csv

dataset_1 = []
dataset_2 = []

with open('brightest_star_data.csv',"r") as f:
    csv_reader = csv.reader(f)
    for r in csv_reader:
        dataset_1.append(r)

with open('dwarfs.csv',"r") as f:
    csv_reader = csv.reader(f)
    for r in csv_reader:
        dataset_2.append(r)

header1 = dataset_1[0]
star_data1 = dataset_1[1:]

header2 = dataset_2[0]
star_data2 = dataset_2[1:]

header = header1 + header2

star_data = []

for i, data_row in enumerate(star_data1):
    star_data.append(star_data1[i]+star_data2[i])

with open('final.csv',"a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(star_data)