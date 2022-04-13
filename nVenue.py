import csv
reach_map = {"X1", "X2", "X3", "HR", "BB", "HBP"}
def calculate_accuracy(file):
    total = 0
    correct = 0
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[6]:
                if float(row[6]) > 50:
                    if row[7] in reach_map:
                        correct += 1
                    total += 1
                
    return "The model's accuracy when predicting reach was {acc}%".format(acc=round((correct/total)*100, 2))

print(calculate_accuracy('sample_data.csv'))